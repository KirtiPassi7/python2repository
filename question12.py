#Write a python program that calculates the sum of the digits of a given number.
num=int(input("enter a number"))
digit=0
sum=0
while num!=0:
    digit=num%10
    num=num//10
    sum=sum+digit
print("The sum is",sum)

