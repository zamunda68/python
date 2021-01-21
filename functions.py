# Function is a collection of code which performs specific tasks.
# It allows you to organize your code better. Similar to variables, functions need to be named.
# The best way to name function is to its purpose - the name should be similar to what the function
# will be doing.

# The function name is preferred to be lower-case. If multiple words are involved, use underscore ("_")

# The function is defined with "def", the name is "sayhi"
def say_hi():
    print("Hello user")

# The function needs to be called, in order for it to be used
# by simply typing it on a new line, at the start of the line.
say_hi()  # this is how a function is called

# Functions also have parameters which are specified within the brackets, after the function's name.
# In this case, the parameter is called "name".

def say_hi(name):
    print("Hello " + name)

# The function is called with a parameter
say_hi("Mike")
say_hi("Steve")