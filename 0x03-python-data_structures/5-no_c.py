#!/usr/bin/python3
def no_c(my_string):
    char = []
    buf = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            char.append(x)
    return buf.join(char)
