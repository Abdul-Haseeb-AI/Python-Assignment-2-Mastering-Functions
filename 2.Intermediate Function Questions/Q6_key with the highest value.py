# key with the highest value.
def cheak(dict):
    max = 0
    for j,i in dict.items():
        if max < i:
            max = i
            key = j
    return key
age = {
        "Haseeb":17,
        "Huzaifa":12,
        "Ali":16,
    }
print("Age_Dictionary ->",age)
print("Max Value Key : ", cheak(age) )
