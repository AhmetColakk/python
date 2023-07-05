
# * ------------------ Sorting --------------------------------
# ? sorting in ascending order
# numbers = [9, 6, 4, 2, 8, 4, 6, 5, 7, 2, 4]
# print(sorted(numbers))


# ? sorting in descending order
# numbers = [9, 6, 4, 2, 8, 4, 6, 5, 7, 2, 4]
# print(sorted(numbers, reverse=True))

# ? sorting in alphabetic order
# ? sorted function does not modify original list but returns new sorted list
# ! notice: capital letters always come first
# ! list must include one data type otherwise sorted() function cause an error
# ? in this case all they are string
# names = ["bower", "john", "david", "Benjamin",
#          "Jane", "rebecca", "micheal"]
# a = sorted(names)
# print("Sorted List:", a)
# print("Original List:", names)

# * ------------------ Set --------------------------------

# ? set(list) func removes all the duplications in a list
# ? set func does not modify original list but returns new set instance by removing all duplications
# ! set() func returns dict
# ? it can include multi data type and numbers come first
# numbers = [9, 6, 4, 2, 8, 4, 6, 5, 7, 2, 4, "ali", "ali"]
# uniq = set(numbers)
# print(type(uniq))
# # ? then, covert to list
# print(list(uniq))


# ! set func damage the order list
# # ? if we use sorted() func first, and then use set() func, it will be unordered dict
# # ? because set func changes the order unexpectedly
# names = ["bower", "john", "david", "Benjamin",
#          "Jane", "rebecca", "micheal"]
# ordered = sorted(names)

# uniq = set(ordered)
# print(uniq)
