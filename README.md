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
