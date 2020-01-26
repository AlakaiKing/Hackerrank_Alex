#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
num_of_swaps = 0
temp = 0
for i in range (n):
    for j in range (n-1):
        if (a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            num_of_swaps +=1

print ("Array is sorted in "+ str(num_of_swaps)+ " swaps.")
print ("First Element: " + str(a[0]))
print ("Last Element: " + str(a[n-1]))
