#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for row in matrix:
       for col in range(len(row)):
           print("{:d}".format(row[col]),
               end = ' ' if col < len(row) -1 else ' ')
            print()
