""" Dictionary is a special structure, which allows us to store information in what is called
key value pairs (KVP). You can create one KVP and when you want to access specific information
inside of the dictionary, you can just refer to it by its key """

#  Similar to actual dictionary, the word is the key and the meaning is the value
# Word - meaning == Key - value
# Every dictionary has a name:

# directory_name = {key_value_pair1, key_value_part2,}
monthConversions = {
    "Jan": "January",   # "Jan" is the key, "January" is the value
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Printing out the value of the key, by referring to the key itself:
print(monthConversions["Nov"])

# Another way to retrieve the value is using the "get()" function:
print(monthConversions.get("Dec"))

# If we want to pass a default value, which is not listed in the list above:
print(monthConversions.get("Dec", "Not a valid key"))

