import hashlib

def hash_file(fileLocation):
    create_sha256 = hashlib.sha256()            # Creating an empty SHA-256 hash obejct
    
    with open(fileLocation, "rb") as file:      # Opening the file in 'read binary' mode
        while True:
            data_chunk = file.read(65536)        # The file is being read in chunks of 65536 bytes i.e. 64 KB

            if not data_chunk:
                break
            create_sha256.update(data_chunk)

    return create_sha256.hexdigest()            # Returning the hexadecimal representation of the hash

fileLocation = "Cryptography.txt"
print(hash_file(fileLocation))

