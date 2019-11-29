# Enter your code here. Read input from STDIN. Print output to STDOUT.
import sys
ph = {}
n = int(input())
for _ in range(n):
    inp = input().split()
    ph[inp[0]] = inp[1]
    inp = []

query = sys.stdin.readline().strip()
while query:
    if query in ph:
        print (query + "=" + ph[query])
    else:
        print ("Not found")
    query = sys.stdin.readline().strip()
