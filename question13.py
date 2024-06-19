#Write a program that asks the user for their birth year and calculates their age.
year=int(input("enter your birth year :"))
current_year=int(input("enter current year :"))
count=0
while year!=current_year:
    count=count+1
    year=year+1
print("Your age is: ",count)    
