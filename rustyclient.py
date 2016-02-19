import ctypes

lib = ctypes.WinDLL(".\\target\\release\\rustypython.dll")

#lib = cdll.LoadLib(".\target\release\rustypython.dll")
lib.process()

print("done")