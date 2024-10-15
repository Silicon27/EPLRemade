# Now we use the firsttest.so file to test the functions

import sys
import os
import ctypes

if sys.platform == "win32":
    lib = ctypes.CDLL(os.path.abspath("../WINOS/cfirsttest.so"))
else:
    lib = ctypes.CDLL(os.path.abspath("../UNIX/cfirsttest.so"))

lib.firsttest()

# add function
print(lib.add(1, 2))