import random
import string
def gen_password(len):
    alpha = string.ascii_letters
    dig = string.digits
    sym = string.punctuation
    password = ""
    for i in range(len):
        list = [random.choice(alpha),random.choice(dig),random.choice(sym)]
        password += random.choice(list)
    return password
len = int(input("Enter Length :"))
print(gen_password(len))