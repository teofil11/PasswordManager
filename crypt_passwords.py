from cryptography.fernet import Fernet
import os
import pyperclip
import csv

input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'
output_file = r'C:\Users\Teofil\Desktop\passwords\en_passwords.csv'


def encrypt_file(key,decrypt_file_path,encrypt_file_path):
    with open(decrypt_file_path, 'rb') as file:
        original_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_data)

    with open(encrypt_file_path, 'wb') as file:
        file.write(encrypted_data)
    os.remove(decrypt_file_path)



def decrypt_file(key, decrypt_file_path, encrypt_file_path):
    with open(encrypt_file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(decrypt_file_path, 'wb') as file:
        file.write(decrypted_data)

    with open(decrypt_file_path, 'r') as file:
        password = file.read()
        pyperclip.copy(password)
    os.remove(decrypt_file_path)

