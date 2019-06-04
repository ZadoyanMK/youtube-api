import hashlib

data = "👋  Hello Hello 👋  | + More Kids Songs | Super Simple Songs"

h1 = data.encode('utf-8').hex()

print(h1)
print(type(h1))
uh1 = bytearray.fromhex(h1).decode()
print(uh1)
