# Enter your code here. Read input from STDIN. Print output to STDOUT


for _ in range (int(input())):
    odd = ""
    even = ""
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print (even + " " + odd)
