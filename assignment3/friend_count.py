import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    result = 0
    for v in list_of_values:
        result += v
    mr.emit((key, result))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
