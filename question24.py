#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
num1=int(input("enter anumber:"))
num2=int(input("enter anumber:"))
operator=input("enter a operator")
if operator=="+":
    print("sum is:",num1+num1)
elif operator=="-":
    print("subtraction of two number is",num1-num2) 
elif operator=="*":
    print("multiplication of two number is",num1*num2)
elif operator=="/":
    print("division of two number is",num1/num2)    

