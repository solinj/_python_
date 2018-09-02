from datetime import datetime
import math
#OR FROM MATH IMPORT SQRT
#OR FROM MATH IMPORT *
print("%02d/%02d/%04d" % (datetime.now().day, datetime.now().month, datetime.now().year))

def volume(dim):
    vol = dim**3
    print("volume of your figure is %d" % (vol))


volume(2)
print("----SQUARE ROOT----")
print(25**(0.5))
print(math.sqrt(25))
