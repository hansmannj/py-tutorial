import hashlib

password = input("Passwort: ")

print(hashlib.md5(password.encode("utf-8")).hexdigest())
