name = "Ahmet"
surName = 'Colak'

# check type
# print(type(name))

# get length of value
# print(len(name))

# ? concatenation
fullName = name + " " + surName
# print(fullName)

# ? Getting specific charecter
# print(name[2])

# ? Getting specific character from reverse
# print(name[-2])

# ? slice the string (startPoint, endPoint)
# ? startPoint is inclusive, endPoint is exlusive
# print(name[2:5])


# ? slice reverse (indexOfEndPoint, minusIndexOfStartPoint)
# print(name[2:-1])

# ? -----Methods-------

# ? upper case and lower case,
# ! It does not alter original value
# print(name.upper())
# print(name.lower())
# print(name)

# ? capitalize
# print(fullName.capitalize())

# ? count a specific character, returns how many of a given character in string
# print(name.count("e"))

# ? finds a specifict character and returns its index number
# ? if the the character is not available in the text, it returns -1
# print(name.find("p"))

# ? split a specific charecter and returns a list
# fruits = "banana, watermelon, peach, plum, cherry"
# print(fruits.split(", "))

# ? check a specific character, returns boolean
# a = "h" in name
# print(a)


# ? check a specific character is not in the string, returns boolean
# a = "h" not in name
# print(a)
