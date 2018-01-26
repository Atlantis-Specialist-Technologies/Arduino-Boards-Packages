import hashlib
import os

with open("ast-0.0.1.zip","rb") as f:
	h = hashlib.sha256()
	h.update(f.read())
	print(h.hexdigest())

print(os.stat("ast-0.0.1.zip").st_size)
