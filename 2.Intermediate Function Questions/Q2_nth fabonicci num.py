def fibonacciNum(l,r):
    while r>0:
        print(l)
        l,r = r,r+l
l = 0 
r = 1
print(fibonacciNum(l,r))