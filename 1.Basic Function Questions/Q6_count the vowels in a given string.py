def count(str):   # function to get string length
    c=0
    for i in str:
        c+=1     # each character in str results in increment in value of c due to itration
    return c
string = input("Enter string : ")
print(f"Length of {string} : {count(string)}")