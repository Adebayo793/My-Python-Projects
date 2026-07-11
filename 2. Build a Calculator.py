#Defining the functions
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x, y):
    #if y == 0:
        #return "Error! Cannot divide by zero."
    return x / y

#Getting User inputs
x = float(input("Enter a number:"))
y = float(input("Enter a number:"))
while y == 0:
    print("Cannot use zero for division, enter another number")
    y = float(input("Enter a number:"))

#Selecting which operation to carryout
operation = input("Choose operation (+, -, *, /): ")
if operation == "+":
    print(add(x, y))
elif operation == "-":
    print(subtract(x, y))
elif operation == "*":
    print(multiply(x, y))
elif operation == "/":
    print(divide(x, y))
