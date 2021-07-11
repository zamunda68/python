"Creating a 2D list in a list and how you can access certain lists from the list"

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# We are accessing/calling by the index number of the row and column
print(number_grid[0][0])
print(number_grid[1][1])

"""Moving on with nested for loop"""

number_grid = [
    [0, 9, 8],
    [7, 6, 5],
    [4, 3, 2],
    [1]
]

for row in number_grid:
    print(row)