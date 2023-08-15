from cryptography.fernet import Fernet

key_file_path = r'C:\Users\Teofil\Desktop\passwords\key.txt'

def generate_key():
    return Fernet.generate_key()

def write_key():
    key = generate_key()
    with open(key_file_path, 'wb') as file:
        file.write(key)

def read_key():
    try:
        with open(key_file_path, 'rb') as file:
            key = file.read()
        return key
    except FileNotFoundError:
        return 'File not exist'
