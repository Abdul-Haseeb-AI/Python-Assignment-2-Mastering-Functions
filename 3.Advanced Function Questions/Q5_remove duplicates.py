def remove_duplicates(temp_list):
    stack = []
    for i in temp_list:
        if i not in stack :
            stack.append(i)
    return stack
list = []
for i in range(5):
    nums = int(input("Enter Numbers for List : "))
    list.append(nums)
print(remove_duplicates(list))