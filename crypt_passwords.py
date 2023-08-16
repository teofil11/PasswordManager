from cryptography.fernet import Fernet
import os
import csv

input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'
output_file = r'C:\Users\Teofil\Desktop\passwords\en_passwords.csv'


def encrypt_file(key,decrypt_file_path,encrypt_file_path):
    """
    Encrypt a file using the Fernet encryption scheme.

    This function reads the contents of a file specified by input_file_path,
    encrypts the data using the provided key, and then writes the encrypted
    data to the file specified by output_file_path. After encryption, the
    original input file is removed for security.

    Parameters:
        key (bytes): The encryption key used for encryption.
        input_file_path (str): The path to the input file to be encrypted.
        output_file_path (str): The path to the output file for encrypted data.
    """
    with open(decrypt_file_path, 'rb') as file:
        bytes_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(bytes_data)

    with open(encrypt_file_path, 'wb') as file:
        file.write(encrypted_data)
    os.remove(decrypt_file_path)



def decrypt_file(key, decrypt_file_path, encrypt_file_path):
    """
    Decrypt a file encrypted using the Fernet encryption scheme.

    This function decrypts the contents of a file specified by encrypt_file_path
    using the provided key, and then returns the decrypted rows as a list.

    Parameters:
        key (bytes): The decryption key used for decryption.
        encrypt_file_path (str): The path to the encrypted file to be decrypted.

    Returns:
        list: A list containing the decrypted rows from the CSV file.
    """
    rows = []
    with open(encrypt_file_path, 'rb') as file:
        bytes_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(bytes_data)

    with open(decrypt_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    with open(decrypt_file_path, 'r') as file:
        data = csv.reader(file)
        for row in data:
            rows.append(row)
    return rows

