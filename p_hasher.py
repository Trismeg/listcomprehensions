import hashlib

hasher = hashlib.sha256()
with open("hasher.py", 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(" the hash is ")
print(hasher.hexdigest())
