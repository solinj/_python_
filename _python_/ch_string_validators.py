# You are given a string .
# Your task is to find out if the string s contains:
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# s entre 0 et 1000 exclus
#
# n the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

def string_validator_isalnum(stringg):
    flag = 0
    for i in stringg:
        if i.isalnum():
            flag = 1
        else:
            flag = 0
    if flag > 0:
        print("True")
    else:
        print("False")

def string_validator_isalpha(stringg):
    flag = 0
    for i in stringg:
        if i.isalpha():
            flag = flag + 1
        else:
            flag = flag + 0
    if flag > 0:
        print("True")
    else:
        print("False")

def string_validator_islower(stringg):
    flag = 0
    for i in stringg:
        if i.islower():
            flag = flag + 1
        else:
            flag = flag + 0
    if flag > 0:
        print("True")
    else:
        print("False")

def string_validator_isupper(stringg):
    flag = 0
    for i in stringg:
        if i.isupper():
            flag = flag + 1
        else:
            flag = flag + 0
    if flag > 0:
        print("True")
    else:
        print("False")


def string_validator_isdigit(stringg):
    flag = 0
    for i in stringg:
        if i.isdigit():
            flag = flag + 1
        else:
            flag = flag + 0
    if flag > 0:
        print("True")
    else:
        print("False")


string_validator_isalnum("q2A")
string_validator_isalpha("q2A")
string_validator_isdigit("q2A")
string_validator_islower("q2A")
string_validator_isupper("q2A")
