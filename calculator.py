#  Really advanced calculator - add, substract, multiply, divide;

# Creating variables to work with.
# "int" is used to convert the data type from string to integer
num1 = int(input("Enter first number: "))
op = input("Enter an operator: ")
num2 = int(input("Enter second number: "))

# Below we are defining what the "op" variable is equal to:
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

# If none of the operators (+, -, /, *) above is entered, print an error:
else:
    print("Error 422: Invalid operator, please select another one.")
