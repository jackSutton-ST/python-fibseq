import time
def Fibonacci(i):
    a = 0; b = 1
    print(a)
    print(b)
    for i in range(0,i,1):
        c = a + b; a = b; b = c
        print(c)
        time.sleep(.3)
nT = int(input("How many times do you want the function to repeat: "))
Fibonacci(nT)               
