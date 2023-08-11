from cryptography.fernet import Fernet
import os
import pyperclip

input_file = r'C:\Users\Teofil\Desktop\passwords\password.txt'
output_file = r'C:\Users\Teofil\Desktop\passwords\en_password.txt'

def encrypt_file(key,decrypt_file_path,encrypt_file_path):
    with open(decrypt_file_path, 'rb') as file:
        original_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_data)

    with open(encrypt_file_path, 'wb') as file:
        file.write(encrypted_data)
    os.remove(decrypt_file_path)

# encrypt_file('RPN73m5sNscQ8Lv1sxG31gId-7sl-9s2byJqvZXvylg=',input_file,output_file)

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



# decrypt_file('RPN73m5sNscQ8Lv1sxG31gId-7sl-9s2byJqvZXvylg=',input_file,output_file)

def generate_key():
    return Fernet.generate_key()

print(generate_key())
