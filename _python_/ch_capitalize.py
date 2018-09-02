#!/usr/bin/env python3
# coding: utf-8

strg = "one name"
strg1 = ""
strg2 = ""
listed = strg.split()
strg1 = listed[0]
strg2 = listed[1]
new_strg1 = ""
new_strg2 = ""
for i in range(len(strg1)):
    if i == 0:
        strg1[0].upper()
    new_strg1 += strg1[i]


print(new_strg1)
#print(strg2)
