def sum(list):
    Sum = 0
    for i in list:
        if i%2==0:
            Sum += i
    return Sum
list = []
for i in range(5):
    nums = int(input("Enter Numbers for List : "))
    list.append(nums)
print("List -> " ,list)
print("Sum ->" ,sum(list))