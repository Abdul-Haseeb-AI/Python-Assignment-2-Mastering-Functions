def check(str1,str2):  #function which cheaks anagrams
    str1 = str1.lower()     #  convert string to lower case
    str2 = str2.lower()     #  convert string to lower case
    return sorted(str1) == sorted(str2)     #   sort strings and return true if they were equal
str1 = input("Enter First Word : ")
str2 = input("Enter Second Word : ")
if check(str1,str2):         # print if result is True
    print("YES , they is anagram")
else :
    print("NO , they is not anagram")