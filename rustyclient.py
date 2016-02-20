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

# Congratulations!
print("done")