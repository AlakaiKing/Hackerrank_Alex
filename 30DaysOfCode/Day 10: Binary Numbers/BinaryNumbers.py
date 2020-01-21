#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    num_of_ones = 0
    maximum = 0

    while n>0:
        if n%2 ==1:
            num_of_ones += 1
            if num_of_ones>maximum:
                maximum = num_of_ones

        else:
            num_of_ones = 0

        n//=2

    print (maximum)
