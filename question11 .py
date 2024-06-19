#Write a python program that generates the first n numbers in the Fibonacci sequence.
n=int(input("enter a  number"))
a=0
b=1
print(a)
print(b)
count=0
sum=0
while count<n:
    sum=a+b
    print(sum)
    a=b
    b=sum
    count=count+1
