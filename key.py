from cryptography.fernet import Fernet

key_file_path = r'C:\Users\Teofil\Desktop\passwords\key.txt'

def write_key():
    """
    Generate and write an encryption key to a file.

    This function generates a new encryption key using Fernet and writes it to
    a specified file in binary format.

    Parameters:
        key_file_path (str): The path to the file where the encryption key will be written.
    """
    key = Fernet.generate_key()
    with open(key_file_path, 'wb') as file:
        file.write(key)

def read_key():
    """
    Read the encryption key from a file.

    This function attempts to read the encryption key from a specified file.
    If the file exists, it reads the key as binary data. If the file does not
    exist, it returns a message indicating the file's absence.

    Parameters:
        key_file_path (str): The path to the file containing the encryption key.

    Returns:
        bytes or str: If the key file exists, the function returns the encryption key as bytes.
                      If the key file does not exist, the function returns a message as a string.
    """
    try:
        with open(key_file_path, 'rb') as file:
            key = file.read()
        return key
    except FileNotFoundError:
        return 'File not exist'
