def sum(a,b):          # function to get sum of values
    sum = a + b
    return sum
val_1 = int(input("Enter First Number : "))
val_2 = int(input("Enter Second Number : "))
sum = sum(val_1,val_2) # sum from function is stored in another variable(sum)
print(f"{val_1} + {val_2} = {sum}")