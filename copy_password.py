import pyperclip

def copy(password):
    """
    Copy the provided password to the clipboard.

    This function takes a password as input and copies it to the system clipboard
    using the `pyperclip` library, making it ready to be pasted.

    Parameters:
        password (str): The password to be copied to the clipboard.
    """
    pyperclip.copy(password)