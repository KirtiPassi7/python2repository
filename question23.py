#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
scale=input("Choose scale celsius or faherenheit:")
celsius=0
faherenheit=0
if scale=="celsius":
     temp=int(input("enter temperature"))
     faherenheit=(temp*1.8)+32
     print(faherenheit)
elif scale=="faherenheit":
     temp=int(input("enter temperature"))
     celsius=(temp-32)*0.5
     print(celsius) 
else:
     print("enter valid scale")         
     scale=input("Choose scale celsius or faherenheit:")