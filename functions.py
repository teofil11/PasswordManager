import random_password

input_file = r'C:\Users\Teofil\Desktop\passwords\passwords.csv'
output_file = r'C:\Users\Teofil\Desktop\passwords\en_passwords.csv'


def add_password(decrypted_rows,account):
    """
    Add a new account and generated password to a list of decrypted rows.

    This function generates a new password using the `generate_password` function,
    appends the account and generated password as a new row to the list of decrypted rows,
    and returns the updated list.

    Parameters:
        decrypted_rows (list): The list containing decrypted rows of account and password data.
        account (str): The account to be added.

    Returns:
        list: The updated list of decrypted rows.
    """
    password = random_password.generate_password()
    decrypted_rows.append([account, password])
    
    return decrypted_rows

def modify_password(decrypted_rows,account):
    """
    Modify the password associated with an account in the list of decrypted rows.

    This function searches for the specified account in the list of decrypted rows.
    If the account is found, it generates a new password using the `generate_password`
    function and updates the password in the row. If the account is not found, it prints
    a message indicating that the password doesn't exist.

    Parameters:
        decrypted_rows (list): The list containing decrypted rows of account and password data.
        account (str): The account for which the password needs to be modified.

    Returns:
        list: The updated list of decrypted rows.
    """
    for row in decrypted_rows:
        if row[0] == account:
            row[1] = random_password.generate_password()
            break
    else:
        print(f"Password for {account} doesn't exist")
    
    return decrypted_rows