#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ks = list(a_dictionary)
    ks.sort()
    for i in ks:
        print("{}: {}".format(i, a_dictionary[i]))
