def febo(num):
    a=0
    b=1
    if num<=0:
        print("Enter positive number:")
    else:
        for i in range(num):
            print(a)
            c = a+b
            a = b
            b = c




num=int(input("enter a positive number:"))
febo(num)
            