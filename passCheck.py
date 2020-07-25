import re

def isValidPassword(password):
    # parameters: String password   returns: whether the password is valid
    if len(password) < 9 or not re.search(r'\W', password) or not re.search(
        '[A-Z]', password) or not re.search('[0-9]', password):
        return False
    return True


password = 'YouA1AF#'

if not password:
    password = input("enter password\n")

print (isValidPassword(password))
