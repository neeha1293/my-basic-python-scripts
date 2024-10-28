#Cryptographically secure random password generator -- uses secrets module, not random module
# Choose length based on your entropy requirements:
# 20+ characters for API keys, admins, crypto keys
# 16 characters for corporate/finance accounts
# 12 characters for personal accounts

import secrets, string, pyperclip

def generatepassword(length):

    if length < 12:
        raise ValueError("length must be atleast 12")


    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation

    password = secrets.choice(lower)
    password += secrets.choice(upper)
    password += secrets.choice(digit)
    password += secrets.choice(special)

    allcharacters = lower+upper+digit+special

    k = length - 4 #for remaining characters

    while k != 0:
        password += secrets.choice(allcharacters)
        k -= 1


    list_password = list(password)
    print(list_password)
    secrets.SystemRandom().shuffle(list_password)
    randompassword = ''.join(list_password)
    print(randompassword)

    return randompassword


##TODO IMPROVEMENT: copy password to password manager
