# Basic work with lists in Python
lucky_numbers = [4, 8, 15, 16, 23, 43]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# How to print two lists together by adding one of them to the other, with the extend method
lucky_numbers = [4, 8, 15, 16, 44, 25]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
lucky_numbers.sort(reverse=True)
print(friends)

# Printing the index (number starting from 0) of the string in the list
print(friends.index("Oscar"))
