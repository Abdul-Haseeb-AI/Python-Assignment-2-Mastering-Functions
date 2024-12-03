def largest_num(nums): 
    max = 0
    for i in nums :
        if max < i:
            max = i
    return max
list_num = []
num = 0
for i in range(5):
    num = int(input("Enter Numbers for List : "))
    list_num.append(num)
print("List -> ",list_num)
print(f"Largest number : {largest_num(list_num)}")