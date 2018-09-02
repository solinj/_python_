
# sstr = "Www.HackerRank.com"
# strr = ""
# for i in range(len(sstr)):
#     if sstr[i].isupper():
#         print(sstr[i])
#         sstr[i].islower()
#         print(sstr[i])
#     # print(strr)
def swap_case(s):
    newStr = ""
    for ss in s:
        if ss.islower():
            newStr+=ss.upper()
        elif ss.isupper():
            newStr+=ss.lower()
        else:
            newStr+=ss
    return newStr


main()
