'''
calls the add function inside libtest2.so file.
libtest2.so is shared library file produced from GCC with the test2.c file.

Check the Calling C functions*.html file for the detailed instructions.

'''
import sys, string, os
from ctypes import *
from cffi import FFI
import random
from sys import *

# load the share library for the C add project
libCalc = CDLL("C:\\Projects\\GCC\\Maths\libtest2.so")
#call C function to check connection
print ( libCalc.add(1,2) )

#Compiling and Executing a C program
os.chdir('C:\\Projects\\GCC\\Maths')
os.system ("gcc.exe -o test2.exe test2.c")
os.system ("test2.exe")


#os.system("C:\\Projects\\GCC\gcc\bin\gcc.exe" )
#-o test2.exe test2.c"')


