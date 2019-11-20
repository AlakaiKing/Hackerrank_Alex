#this is solution to hackkerank problem named "capitalize"

import string

#basically what we are doing is
# we split each word at space and applying string.capitalize and then
def capitalize(a):
    print (' '.join(map(string.capitalize, a.split(' '))))

capitalize("1 2 3 4 r t 6")
