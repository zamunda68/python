""" If statement is used to make decision when certain a condition is true and execute another
 code if other conditions are true """

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are a female")

"""" The code is executed in this:
1. If is_male
2. Then the interpreter checks if is_male is "true" or "false"
3. Finally prints out the result or not, depending on the condition that was met """


# Below is an example of multiple conditions with the "or" operator used
is_male1 = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are male, but not tall one")
else:
    print("You are neither male or tall")
