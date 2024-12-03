def check(str):    # function which cheaks string is palindrom or not
    if str == str[::-1]:
        return True      # Returns TRUE if string is palandrom else return nothing
string = input ("Enter String : ")
if check(string) == True:      # if function returns TRUE
    print(string ," is palindrome")
else:
    print(string ," is not palindrome")