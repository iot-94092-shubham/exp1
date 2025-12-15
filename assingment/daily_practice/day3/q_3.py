def vowe():
    vowe = 'aeiouAEIOU'
    count = 0
    text = input("Enter a string: ")
    for char in text:
        if char in vowe:
            count += 1
    print("Number of vowels:", count) 

def cons():
    cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    text = input("Enter a string: ")
    for char in text:
        if char in cons:
            count += 1
    print("Number of consonants:", count)               

vowe() 
cons()         