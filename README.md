# File Integrity Checker 🔐
 
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Hashlib](https://img.shields.io/badge/Library-hashlib-green)
![Algorithm](https://img.shields.io/badge/Algorithm-SHA--256-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
 
A simple Python toolkit for generating SHA-256 hashes of files and verifying whether two files contain identical data — useful for checking file integrity, detecting tampering, or comparing duplicate files.
 
## 📁 Files
 
| File | Description |
|------|-------------|
| `hash.py` | Computes and prints the SHA-256 hash of a given file, reading it in 64 KB chunks for memory efficiency. |
| `integrity_checker.py` | Compares the SHA-256 hashes of two files to determine whether their contents are identical. |
 
## ✨ Features
 
- Computes SHA-256 hashes using Python's built-in `hashlib`
- Reads files in chunks (64 KB) to efficiently handle large files without high memory usage
- Compares two files' hashes to verify data integrity
- Simple, dependency-free implementation

## 🚀 Usage
 
### 1. Hash a single file
 
```bash
python hash.py
```
 
By default, it hashes `Cryptography.txt`. Update the `fileLocation` variable in the script to point to your target file.
 
```python
fileLocation = "Cryptography.txt"
print(hash_file(fileLocation))
```
 
**Output:**
```
a1b2c3d4e5f6...  (64-character hexadecimal SHA-256 hash)
```
 
### 2. Compare two files for integrity
 
```bash
python integrity_checker.py
```
 
Update `fileLocation1` and `fileLocation2` to the files you want to compare:
 
```python
fileLocation1 = "Cryptography.txt"
fileLocation2 = "TestFile.txt"
check_integrity(fileLocation1, fileLocation2)
```
 
**Output:**
```
These files contain the same data.
```
or
```
These files have different contents.
```
 
## 🛠️ How It Works
 
1. A SHA-256 hash object is created using `hashlib.sha256()`.
2. The target file is opened in binary read mode (`"rb"`).
3. The file is read in 64 KB chunks and each chunk updates the hash object — this avoids loading large files entirely into memory.
4. The final hash is returned as a hexadecimal string via `.hexdigest()`.
5. For integrity checking, two files' hashes are computed and compared directly.
## 📋 Requirements
 
- Python 3.x
- No external dependencies (uses only the standard `hashlib` library)
## 📄 License
 
This project is open source and available under the [MIT License](LICENSE).
