import random
import csv
import os

input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'

def generate_password(lenght):
    password = ''
    letters = 'abcdefghijklmnopqrstuvxyz'
    upper_letters = letters.upper()
    symbols = '!@#$%^&*`~/?\\><'
    numbers = '0123456789'
    all_caracters = [letters,symbols,numbers,upper_letters]
    for i in range(lenght):
        type_caracter = random.choice(all_caracters)
        i = random.choice(type_caracter)
        password += i
        
    return password


def write_password(lenght,account):
    password = generate_password(lenght)
    accound_data = [account,password]
    head = ['Account','Password']

    if os.path.exists(input_file) is False:
        with open(input_file, 'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(head)


    with open(input_file, 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(accound_data)



