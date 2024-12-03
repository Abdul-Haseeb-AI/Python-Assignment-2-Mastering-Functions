import random
import string
def gen_pwd(length):
    upr_case = string.ascii_uppercase
    lwr_case = string.ascii_uppercase
    dig_case = string.ascii_uppercase
    sym_case = string.ascii_uppercase



len = input("Enter length of password : ")
print("Password ->",gen_pwd(len))

























































# '''2. Create a function to generate a random password of given 
# length, containing uppercase, lowercase, numbers, and special 
# characters.'''


# import random
# import string

# def generate_password(length):
#     if length < 4:
#         raise ValueError("Password length must be at least 4 to include all character types.")

#     # Character pools
#     lowercase = string.ascii_lowercase
#     uppercase = string.ascii_uppercase
#     digits = string.digits
#     special_chars = string.punctuation

#     # Ensure the password contains at least one of each type
#     password = [
#         random.choice(lowercase),
#         random.choice(uppercase),
#         random.choice(digits),
#         random.choice(special_chars)
#     ]

#     # Fill the rest of the password length with random characters
#     remaining_length = length - 4
#     all_characters = lowercase + uppercase + digits + special_chars
#     password += random.choices(all_characters, k=remaining_length)

#     # Shuffle to avoid predictable patterns
#     random.shuffle(password)

#     # Join the list into a single string and return
#     return ''.join(password)

# # Example usage
# password_length = 12
# print("Generated password:", generate_password(password_length))