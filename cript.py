from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file:
        original_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(original_data)

    with open(output_file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # Generăm o cheie nouă
    key = generate_key()

    # Criptăm un fișier
    input_file_path = 'Week 20/text.txt'
    output_file_path = 'Week 20/txt.bin'
    # encrypt_file(key, input_file_path, output_file_path)

    # Decriptăm fișierul criptat
    decrypted_output_file_path = 'Week 20/text.txt'
    decrypt_file('RPN73m5sNscQ8Lv1sxG31gId-7sl-9s2byJqvZXvylg=', output_file_path, decrypted_output_file_path)

    print(key)
    print("Fișier criptat și decriptat cu succes!")