#Write a python program that calculates the factorial of a given number.
num=int(input("Enter a number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i=i+1
print("factorial of gven number is:",fact)    
