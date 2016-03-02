'''
This is a simple client script who will run the Rust binary library.

@author: Davide Aversa <thek3nger@gmail.com>

NOTE: Before using this script you neet to compile the rust library. Do that
with the command

    cargo build --release
    
This script is for Windows. Linux version will come.
'''

# Import the stadard interface library between Python and C libraries.
import ctypes

# We load the dll using WinDLL (windows format). For Linux try to comment
# this line and then uncomment the next one. 
lib = ctypes.WinDLL(".\\target\\release\\rustypython.dll")
#lib = cdll.LoadLib(".\target\release\rustypython.dll")

# We execute the Rust process() function we defined in src/lib.rs
print("Running process()")
lib.process()

# We execute the Rust process2() function we defined in src/lib.rs
print("Running process2(5)")
lib.process2(5)

# We want to pass a Paython List. We cannot do this directly we need to
# convert PLists into CLists.

# This say that the arguments of Rust "sum_list" are of the following types.
# However in this case this works even without this line...
lib.sum_list.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.c_size_t)

# Then we can start using our function.
print("Summing in Rust the list of first 1000 numbers.")
number_list = list(range(1001))
c_number_list = (ctypes.c_int32 * len(number_list))(*number_list)
result = lib.sum_list(c_number_list, len(number_list))
print("Result is {}. Expected 500500.".format(result))

# This is horrible. Let's write something to wrap up this.
def sum_list(nums):
    c_number_list = (ctypes.c_int32 * len(nums))(*nums)
    return lib.sum_list(c_number_list, len(nums))
    
# ... and just call this from now on. (This is always the right choice!)
print("Summing in Rust the list of the first 500 numbers.")
print("Result is {}. Expected 125250.".format(sum_list(list(range(501)))))

# This works for tuples too!
print("Summing in Rust (1,43,56).")
print("Result is {}.".format(sum_list((1,43,56))))

# ...and sets too!
print("Summing in Rust {1,43,56}.")
print("Result is {}.".format(sum_list({1,43,56})))
    

# OBJECTS
# First, we need to define a Python object which represents the Rust struct.
# This is done extending `ctypes.Structure` class and using `_fields_` instead
# of classic Python attributes.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]
    
    def __str__(self):
        return "Point ({},{})".format(self.x, self.y)

# Then we specify as usual the type declaration of the Rust function.
lib.middle.argtypes = (Point, Point)
lib.middle.restype = Point

# And then we can easily use it as a native python function!
p1 = Point(1.0, 5.0)
p2 = Point(1.0, 10.0)

res_point = lib.middle(p1, p2)
print(res_point)

# Congratulations!
print("done")