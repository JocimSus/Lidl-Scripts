import hashlib

def check_hash(path: str, hash_base: str) -> None: 
  with open(path, 'rb') as f:
    BUF_SIZE = 65536  # Read in 64kb chunks
    sha256 = hashlib.sha256()
    while True:
      data = f.read(BUF_SIZE)
      if not data:
        break
      sha256.update(data)
    
    print("")
    print("========================================")
    print(f"Path: {path}")
    print(f"Hash(SHA256): {hash_base} ")
    print(f"SHA256: {sha256.hexdigest()}")
    print("========================================")
    
    print()
    if hash_base == sha256.hexdigest():
      print("Same hash")
    else:
      print("Diff hash")

# Get user inputs
path = input("Absolute Path: ")
hash_base = input("Hash Base(SHA256): ")

# Check Hash
check_hash(path, hash_base)