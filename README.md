# Password Manager

This Python program stores passwords in an encrypted csv file

The data (password and respectively the account to which the password belongs) are read from the keyboard and entered into a csv file.

Two files will store the data:
-The first file is the one decrypted after each operation (adding, changing, copying, displaying accounts) the file is encrypted with another key rewritten in the key.txt file. After each encryption, this file is deleted
-The second file is the encrypted one. It keeps all data encrypted

Requirements:
- Python 3.x