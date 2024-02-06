What are the security vulnerabilities in this python code?
import hashlib

def hash_password(password):
    # Insecure: Using MD5 hash algorithm
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

# Usage example
password = "myPassword123"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)
