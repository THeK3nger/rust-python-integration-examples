import ctypes

lib = ctypes.WinDLL(".\\target\\release\\rustypython.dll")

#lib = cdll.LoadLib(".\target\release\rustypython.dll")
print("Running process()")
lib.process()

print("Running process2(5)")
lib.process2(5)

print("done")