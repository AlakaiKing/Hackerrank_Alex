# test_str = "BANANA"
#
# # Get all substrings of string
# # Using list comprehension + string slicing
# res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
# print (res)
# #
# # for k in range(len(test_str)):
# #     for l in range(k + 1, len(test_str)+1):
# #         print (k)
# #         print (l)
# #         print (test_str[k:l])
# #         print ('-----------')
# kevin = 0
# staurt = 0
#
# for p in res:
#     if p[0] in ('a','e','i','o','u','A','E','I','O','U'):
#         kevin += 1
#     else:
#         staurt += 1
#
# print (staurt)
# print (kevin)
#
# if (kevin < staurt):
#     print ("Stuart {}".format(staurt))
# elif (kevin > staurt):
#     print ("Kevin {}".format(kevin))
# else:
#     print ("Draw")


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
