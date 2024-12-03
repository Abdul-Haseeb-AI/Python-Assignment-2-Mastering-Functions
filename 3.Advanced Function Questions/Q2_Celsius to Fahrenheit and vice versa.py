def fahrenheit(c):   #function to convert celcuis to fehrenheit
    f = 0
    f = (c*(9/2))+32
    return f
def celsius(f):    #function to convert fehrenheit to celcuis
    c = 0
    c = (f*(9/2))+32
    return c
print("Choose any One:")
print("         f : to find Fahrenheit")
print("         c : to find Celcius")
choice = input("Enter Choice :")       #  Enter User's Choice
if choice == "f" or choice == "F":     #  if user wants to  convert celcuis into fehrenheit
    Cel = int(input("Enter Celcius : "))
    print("Fahrenheit -> ",fahrenheit(Cel))
elif choice == "c" or choice == "C":   #  #  if user wants to  convert fehrenheit into celcuis
    feh = int(input("Enter Fehenheit :"))
    print("Celcuis ->",celsius(feh))
    pass
else:
    print("Invalid Input")