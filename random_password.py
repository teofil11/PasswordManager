import random
import csv
import os

input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'

def generate_password():
    """
    Generate a random password.

    This function generates a random password of length 20 by selecting characters
    from different character sets: lowercase letters, uppercase letters, symbols, and digits.

    Returns:
        str: A randomly generated password.
    """
    password = ''
    letters = 'abcdefghijklmnopqrstuvxyz'
    upper_letters = letters.upper()
    symbols = '!@#$%^&*`~/?\\><'
    numbers = '0123456789'
    all_caracters = [letters,symbols,numbers,upper_letters]
    for i in range(20):
        type_caracter = random.choice(all_caracters)
        i = random.choice(type_caracter)
        password += i
        
    return password


def write_password(account,password):
    """
    Save account data to a CSV file.

    If the CSV file specified by input_file exists, the account data (account and password)
    is appended to the file. If the file doesn't exist, it is created, and the account data
    is written with a header row.

    Parameters:
        input_file (str): The path to the CSV file.
        account_data (list): A list containing account and password information.
    """
    account_data = [account,password]
    head = ['Account','Password']

    if os.path.exists(input_file) is False:
        with open(input_file, 'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(head)
        with open(input_file, 'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(account_data)
        
    else:
        with open(input_file, 'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(account_data)




