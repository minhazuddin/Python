# For 32 bit it will return 32 and for 64 bit it will return 64
import struct, platform
print(struct.calcsize("P") * 8)


import platform
print(platform.architecture()[0])
