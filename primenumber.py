num = int(input("enter a number :"))
use = 0
for i in range (2, num):
    if (num % i ==0 ):
        use = 1
        break

if (use == 0 ):
    print("the no is prime")
else:
    print("the no is not a prime")