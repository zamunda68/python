# Tuples is a type of data structure where we can store different values.
# Tuples are similar to lists and it allows storing multiple pieces of information.
# Tuples are IMMUTABLE, which means you cannot change/modify its value

# Basic tuple
coordinates = (4, 5)
print(coordinates[1])  # [1] is the index position of 4 in the tuple itself
# End of tuple

# Demonstration of how tuple is immutable and it cannot be modified/changed
coordinates = (5, 6)
coordinates[1] = 10  # this is where try to assign a different value to number 5 in tuple
# expected result is an error "TypeError: 'tuple' object does not support item assignment"
print(coordinates)
# End of demonstration of how tuple cannot work
