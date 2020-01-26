
test_str = "BANANA"
l = len(test_str)

kevin = 0
stuart = 0

for i in range(l):
    if test_str[i] in ('A','E','I','O','U'):
        kevin += l - i
    else:
        stuart += l - i

if (kevin < stuart):
    print ("Stuart {}".format(stuart))
elif (kevin > stuart):
    print ("Kevin {}".format(kevin))
else:
    print ("Draw")
