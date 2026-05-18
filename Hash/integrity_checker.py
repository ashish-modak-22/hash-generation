import hashlib

def hash_file(fileLocation):
    create_sha256 = hashlib.sha256()            
    
    with open(fileLocation, "rb") as file:     
        while True:
            data_chunk = file.read(65536)        

            if not data_chunk:
                break
            create_sha256.update(data_chunk)

    return create_sha256.hexdigest()           


def check_integrity(fileLocation1, fileLocation2):
    hash_for_file1 = hash_file(fileLocation1)
    hash_for_file2 = hash_file(fileLocation2)

    if hash_for_file1 == hash_for_file2:
        print("These files contain the same data.")
    else:
        print("These files have different contents.")

fileLocation1 = "Cryptography.txt"
fileLocation2 = "TestFile.txt"


check_integrity(fileLocation1, fileLocation2)

