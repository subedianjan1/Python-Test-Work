from cffi import FFI
import random
from sys import *

print  ("Gooday")

def load(filename):
    #load source code
    source  = open('C:\\Projects\\Eclipse Workspace\\test2\\src\\test2' +'.c').read()
    includes = open('C:\\Projects\\Eclipse Workspace\\test2\\src\\add' +'.h').read()



#Embed C function decleration for future use. Can we Embed C codes here?

ffi = FFI()
ffi.cdef("""
int add(int, int);
""")



'''


class AddTest(unittest.TestCase);
    def test_addition(self);
        module = load('add')
        self.assertEqual(module.add(1,2), 1 + 2)
run(AddTest)
'''

