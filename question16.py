#Write a program in python that counts the frequency of each character in a string.
str=input("Enter your name:")
l1=list(str)
count=0
length=len(str)
for j in range(0,length):   
    for i in l1:
       if l1[j]==i:
        count=count+1
        i=i+1
print(count)        
        
    