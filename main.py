def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

selection = int(input("""Choose an operation 1-4:
Addition 1: 
Subtraction 2:
Multiplication 3:
Division 4: """))

a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))

if selection == 1:
    print(f"{a} + {b} = {add(a,b)}")
elif selection == 2:
    print(subtract(a,b))
elif selection == 3:
    print(multiply(a,b))
elif selection == 4:
    print(division(a, b))


print("Did this work?")