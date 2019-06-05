from ctypes import *
from cffi import FFI
import random
from sys import *

# load the share library for the C add project
libCalc = CDLL("C:\\Projects\\GCC\\Maths\libtest2.so")
#call C function to check connection
print ( libCalc.add(1,2) )


