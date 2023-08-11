import random

input_file = r'C:\Users\Teofil\Desktop\passwords\password.txt'

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


def write_password(password):
    with open(input_file, 'w') as file:
        file.write(password)
    

write_password(generate_password(20))
