import math
all_from_math_module = dir(math)
print(all_from_math_module)

# import math # Imports the math module
# everything = dir(math) # Sets everything to a list of things from math
# print everything # Prints 'em all!

def get_values(*args):
    print max(args)
    print min(args)
    print abs(args[1])

get_values(4, -9, 45)
