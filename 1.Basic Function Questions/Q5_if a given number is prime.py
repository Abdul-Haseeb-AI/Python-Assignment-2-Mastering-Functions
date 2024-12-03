def cheak_prime(num):
    if num % 2 != 0 and num % 3 != 0:
        print("Prime Number")
    else:
        print("Not a Prime Number")
int_num = int(input("Enter Number : "))
cheak_prime(int_num)