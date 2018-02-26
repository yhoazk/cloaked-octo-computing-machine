f = open("bin.log", "wb")
f.write(bytearray(b'\x00\x00\x00\x00'))
f.close()
