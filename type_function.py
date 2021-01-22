# type() function is built-it function commonly used for debugging.
# It can be used to determine the data type of the object in the brackets (e.g. "type(10)").

def typefunction():
    x = [1, 2, 3]
    y = 23
    z = 22

    print(type(y))

#  The function is called below:
typefunction()


# An example with loop to print out multiple objects data type using the type() function
def TypeFunctionLoop():
    x = [1, 2, 3]
    y = "y"
    z = 1j
    for i in [x, y, z]:
        print(type(i))


TypeFunctionLoop()


