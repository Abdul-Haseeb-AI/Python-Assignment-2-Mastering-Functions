import random
import string
def gen_pwd(length):
    upr_case = string.ascii_uppercase
    lwr_case = string.ascii_uppercase
    dig_case = string.ascii_uppercase
    sym_case = string.ascii_uppercase



len = input("Enter length of password : ")
print("Password ->",gen_pwd(len))