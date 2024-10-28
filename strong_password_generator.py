import random, string

def generatepassword(length):

    if length < 8:
        raise ValueError("length must be atleast 8")


    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation

    password = random.choice(lower)
    password += random.choice(upper)
    password += random.choice(digit)
    password += random.choice(special)

    allcharacters = lower+upper+digit+special

    k = length - 4 #for remaining characters

    while k != 0:
        password += random.choice(allcharacters)
        k -= 1


    list_password = list(password)
    print(list_password)
    random.shuffle(list_password)
    randompassword = ''.join(list_password)
    print(randompassword)

    return randompassword

# run using python 3
print(generatepassword(9))
