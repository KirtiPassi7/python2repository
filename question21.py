#Write a python program that counts the occurrences of a specific element in a list.
alphabets=0
digits=0
special_character=0
str=input("enter your name,age,date of birth")
list=list(str)
print(list)
for i in list:
    if i.isalpha():
        alphabets=alphabets+1
    if i.isdigit():
        digits=digits+1    
    else:
        special_character=special_character+1    
print("total occurence of alphabets is",alphabets)
print("total occurence of digits is",digits)     
print("total occurence special characters is",special_character)
