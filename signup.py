from pyscript import display
from js import document

def register(e):

    document.getElementById('output').innerHTML = ''
    password = document.getElementById('password').value
    username = document.getElementById('username').value
    password_length = len(password)
    username_length = len(username)

    if username == "" or password == "": #checks if the input is blank
        display("Input fields cannot be blank.", target="output")
        return

    if len(username) < 7: #checks if the username has enugh characters
        display(f"Username needs {7 - len(username)} more characters.", target="output")
        return

    hasaletter = any(char.isalpha() for char in password)
    hasanumber = any(char.isdigit() for char in password)
    long_enough = len(password) >= 10

    if not hasaletter: #checks if the password has letters
        display("Invalid input! Password must contain letters.", target="output")
    elif not hasanumber: #checks if the password has numbers
        display("Invalid input! Password must contain numbers.", target="output")
    elif not long_enough: #checks if the password is long enough
        display(f"Invalid input! Password must have {10 - len(password)} more characters to proceed.", target="output")
    else:
        display("Account created successfully!", target="output")
