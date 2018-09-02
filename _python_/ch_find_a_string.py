from math import *
print("lolo")
# PARSE STRING REVERSE MODE
sstr = "AbBaAbBaAbBa"
# sstr = sstr[::-1]
# for i in str:
#     print(i)
substr = "Ab"

def ss(string, substring):
    # string, substring = (input().strip(), input().strip())
    val = sum([ 1 for i in range(len(string)-len(substring)+1)if string[i:i+len(substring)] == substring])
    print(val)
    return val

print(ss(sstr, substr))

# def ss(st, sub):
#     n = 0
#     if len(sstr) in range(1, 201):
#         for i in sstr:
#             for j in substr:
#                 # print(substr[0])
#                 # print(j)
#                 if ord(substr[0]) == ord(j):
#                     # print("T")
#                     if ord(i) == ord(j):
#                         n = n + 1
#                         print("final " + str(n))
#         # print(n)
#         if n > 1:
#             print("n > 1")
#             floating = (float(n) / float(len(substr)))
#             print(floating)
#             val = int(ceil(floating))
#             # print("if " + str(val))
#             return val
#         elif n < 0:
#             print("n < 0")
#             return 0
#         else:
#             print("n entre 0 et 1")
#             floating = (float(n) / float(len(substr)))
#             # print(floating)
#             val = int(ceil(floating))
#             # print("else " + str(val))
#             return val
# print(ss(sstr, substr))


def count_substring(string, sub_string):
    count=0
    # 5
    # 2
    # i = 3 => n'aille pas jusq'uau bout de la chaine. s'arrêter à str len - substr len
    for i in range(0, len(string)-len(sub_string)+1): i = 0 -- 3
        if string[i] == sub_string[0]: #morceau de chaîne de caractères
            flag=1
            for j in range (0, len(sub_string)): #valeur maximale longueur substr len
                if string[i+j] != sub_string[j]: #étudie morceau de chaîne de caractère de string
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

print('-------------------------')
print(count_substring(sstr, substr))


# a = 2.3659
# print(int(ceil(a)))

# for i in range(0, len(s)):
#     print (s[i])
# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# String letters are case-sensitive.
# :-1
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Constraints
# Each character in the string is an ascii character.
#
# Output Format
#
# Output the integer number indicating the total number of occurrences of the substring in the original string.
#
# def count_substring(string, sub_string):
#     return
#
#
# len(string) in range(1, 201)
#
#
#
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
