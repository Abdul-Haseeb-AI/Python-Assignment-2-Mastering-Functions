def reverse_string(str):   #function which reverses Strings
    return str[::-1]       #[::-1] will reverse value and return result
str_input = input("Enter String: ")
print(f"Reverse of {str_input} is {reverse_string(str_input)}")