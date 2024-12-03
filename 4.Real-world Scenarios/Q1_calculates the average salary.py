def average(salaries):   # Function which give average
    sum = 0
    for values in salaries.values():    # use loop to get sum of values
        sum += values
    average = sum / len(salaries)       # get average using farmula
    return average
salaries = {}       # initialize a dictionary
length = int(input("Enter Number of Employees : "))
for i in range(length):     # use loop to get employees names & salaries
    print(i)
    Name = input("Enter Employee Name : ")
    salary = int(input("Enter Employee Salary : "))
    salaries[Name] = salary         # add values to salaries
print(average(salaries))