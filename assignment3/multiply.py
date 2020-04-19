import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    matrix = record[0]
    if matrix == "a":
        for i in range(5):
            mr.emit_intermediate((record[1], i), record)
    else:
        for i in range(5):
            mr.emit_intermediate((i, record[2]), record)


def reducer(key, list_of_values):
    matrix = [[0] * 2 for i in range(5)]
    for element in list_of_values:
        if element[0] == "a":
            matrix[element[2]][0] += 1
            matrix[element[2]][1] += int(element[3])
        else:
            matrix[element[1]][0] += 1
            matrix[element[1]][1] *= int(element[3])

    result = 0
    for el in matrix:
        if el[0] == 2:
            result += el[1]
    mr.emit((key[0], key[1], result))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
