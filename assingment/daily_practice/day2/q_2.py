num=int(input("Enter a 5 digit number:"))
pal=0
num1 = num % 10
num2 = (num // 10) % 10
num3 = (num // 100) % 10
num4 = (num // 1000) % 10
num5 = num // 10000

pal = num1*10000+num2*1000+num3*100+num4*10+num5

if pal == num:
   print("the number is palindrome")
else:
 print("the number is not palindrome")


