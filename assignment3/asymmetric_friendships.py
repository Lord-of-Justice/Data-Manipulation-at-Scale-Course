import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    friend = record[0]
    person = record[1]
    mr.emit_intermediate(friend, person)
    mr.emit_intermediate(person, friend)


def reducer(key, list_of_values):
    #print(key, list_of_values)
    not_friends = []
    for friend in list_of_values:
        if friend not in not_friends:
            not_friends.append(friend)
        else:
            not_friends.remove(friend)

    for person in not_friends:
        mr.emit((key, person))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
