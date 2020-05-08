#!/usr/bin/env python3
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Would you like to subtract, divide or multiply these numbers?: ")

def add(x,y):
    sum=x+y
    return sum

def subtract(x,y):
    difference=x-y
    return difference

def multiply(x,y):
    product=x*y
    return product

def divide(x,y):
    quotient=x/y
    return quotient

#print("add: ",add(num1,num2))

if operator == "subtract":
    print(f"{num1} - {num2} is {subtract(num1,num2)}")
elif operator == "multiply":
    print(f"{num1} * {num2} is {multiply(num1,num2)}")
elif operator == "divide":
    print(f"{num1} / {num2} is {divide(num1,num2)}")



