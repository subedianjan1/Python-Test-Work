'''
calls the add function inside libtest2.so file.
libtest2.so is shared library file produced from GCC with the test2.c file.

Check the Calling C functions*.html file for the detailed instructions.

'''

from ctypes import *
from cffi import FFI
import random
from sys import *

# load the share library for the C add project
libCalc = CDLL("C:\\Projects\\GCC\\Maths\libtest2.so")
#call C function to check connection
print ( libCalc.add(1,2) )


