import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    for order in list_of_values:
        if order[0] == "order":
            list_of_values.remove(order)
            for line_item in list_of_values:
                mr.emit(order + line_item)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
