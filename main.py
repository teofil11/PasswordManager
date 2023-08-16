import crypt_passwords
import random_password
import key
import copy_password
import csv
import os
import functions


input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'
output_file = r'C:\Users\Teofil\Desktop\passwords\en_passwords.csv'
key_path = r'C:\Users\Teofil\Desktop\passwords\key.txt'

def main():
    """
    Main function to manage password operations.

    This function serves as the central menu-driven control for managing passwords.
    It allows users to perform various password-related operations such as adding,
    changing, copying, and displaying passwords. The menu is presented in a loop
    until the user chooses to exit.
    """

    if os.path.exists(key_path) is False:
        key.write_key()
    while True:
        choice = input("""Chose option:
1.Add password
2.Change password
3.Copy password
4.Display the accounts
5.Exit
""")
        
        if choice == '1':
            try:
                account = input('For which account you want to generate a password: ')
                passwords = crypt_passwords.decrypt_file(key.read_key(),input_file,output_file)
                for row in passwords:
                    if row[0] == account:
                        print(f'You have password for {account}')
                        main()
                pas = functions.add_password(passwords,account)
                with open(input_file, 'w',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(pas)
                key.write_key()
                crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)
            except FileNotFoundError:
                password = random_password.generate_password()
                random_password.write_password(account,password)
                key.write_key()
                crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)
                        
        if choice == '2':
            if os.path.exists(output_file):
                account = input('For which account you want to change password a password: ')
                passwords = crypt_passwords.decrypt_file(key.read_key(),input_file,output_file)
                pas = functions.modify_password(passwords,account)
                with open(input_file, 'w',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(pas)
                key.write_key()
                crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)

            else:
                print('You dont have passwords')
        
        if choice == '3':
            if os.path.exists(output_file):
                account = input('For which account you want to copy a password: ')
                passwords = crypt_passwords.decrypt_file(key.read_key(),input_file,output_file)
                for row in passwords:
                    if row[0] == account:
                        password = copy_password.copy(row[1])
                        break
                else:
                    print(f'You dont have password for {account}')
            else:
                print('You dont have passwords')
            key.write_key()
            crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)
        
        if choice == '4':
            passwords = crypt_passwords.decrypt_file(key.read_key(),input_file,output_file)
            for row in passwords:
                print(row[0])   
            key.write_key()
            crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)

        elif choice == '5':
            if os.path.exists(input_file):
                key.write_key()
                crypt_passwords.encrypt_file(key.read_key(),input_file,output_file)
            print("Exiting.")
            break
                    
main()