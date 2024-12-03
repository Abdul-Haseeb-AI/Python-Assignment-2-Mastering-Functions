def Power(num,power):
    result = 1
    for i in range(1,power+1):
        result = result * num
    return result
num = int(input("Enter Number : "))
power = int(input("Enter Power : "))
print("Number : ",num,"Power : ",power,"Result : ", Power(num,power))