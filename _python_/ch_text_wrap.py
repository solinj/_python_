import textwrap

def wrap(string, max_width):
    var = textwrap.wrap(string, max_width)
    # print(var)
    j = ""
    for i in var:
        j = j + i + "\n"
    return j

    # return i







print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
#
