
# ? dictionaries and accessing
# ? comma used for seperation, last item's comma is optional
# ? all data type can be defined in dictionaries
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black",
#     "active": True,
#     "age": 27,
#     "lang": ["tr", "en"],
#     "adress": {
#         "county": "England",
#         "city": "london",
#     },

# }
# print(ninja_belt)

# ? another way to create a dictionary
# ninja_belt = dict(name="Ahmet", age=27, is_student=True)
# print(ninja_belt)


# ? get specific key from dict
# print(ninja_belt["cristal"])

# ? get length of dict
# print(len(ninja_belt))


# ! if there is duplication, only last one is valid
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black",
#     "active": True,
#     "age": 27,
#     "age": 50,
#     "lang": ["tr", "en"],
#     "adress": {
#         "county": "England",
#         "city": "london",
#     },

# }
# print(ninja_belt)

# ? check whether key is avilable
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# print("ali" in ninja_belt)

# ? dic.keys() gets all keys and returns dict_keys data type
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# print(ninja_belt.keys())
# # ? to conver to list
# print(list(ninja_belt.keys()))

# ? dic.values() gets all values and returns dict_values data type
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# print(ninja_belt.values())
# # ? to convert list
# print(list(ninja_belt.values()))


# ? add new element to dictionary
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# ninja_belt["ahmet"] = "blue"
# print(ninja_belt)


# * ---------------------- loop operations in dicts --------------------------------

# ? loop over a dictionarise for only keys and reversed order
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# for n in ninja_belt.keys():
#     print(n, end="\n")
# for n in reversed(ninja_belt):
#     print(n)

# ? loop over a dictionarise for only values
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# for n in ninja_belt.values():
#     print(n)

# ? loop over a dictionarise for both keys and values
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# for n in ninja_belt:
#     print(n + ": " + ninja_belt[n])

# ? another way to loop over a dictionary for bot keys and values
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# # ? n is key, x is value
# for n, x in ninja_belt.items():
#     print(n + ": " + x)


# ? another way to loop over a dictionary for bot keys and values
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# for n, x in ninja_belt.keys(), ninja_belt.values():
#     print(n + ": " + x)

# * ---------------------- copy and clone operations in dicts --------------------------------

# ? clone a dictionary
# ! This is reference type which means when change any of value of clone/original, it mutates clone/original as well
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# newList = ninja_belt
# newList["ryu"] = "white"
# print(newList)
# print(ninja_belt)

# ? copy a dictionary
# ? This time, it won't change original value
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# newList = ninja_belt.copy()
# newList["ryu"] = "white"
# print(newList)
# print(ninja_belt)

# ? another way to copy a dictionary
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# newList = dict(ninja_belt)
# newList["ryu"] = "white"
# print(newList)
# print(ninja_belt)

# * ---------------------- delete operations in dicts --------------------------------

# ? remove item from dict
# ? pop(key_name) method remove an item with its key name from dict
# ! if key is not available in dict, it causes  an error
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# ninja_belt.pop("cristal")
# print(ninja_belt)

# ? popitem method remove last inserted item from dict
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# ninja_belt.popitem()
# print(ninja_belt)

# ? another way to remove with provided key name from dict
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }

# del ninja_belt["cristal"]
# print(ninja_belt)

# ! clear() method deletes all the keys with their values
# ! however the dict itself remains as empty
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# ninja_belt.clear()
# print(ninja_belt)

# ! del dict destroyes dict forever
# ! in this case, it causes  an error
# ninja_belt = {
#     "cristal": "red",
#     "ryu": "black"
# }
# del ninja_belt
# print(ninja_belt)

# * ---------------------- dict methods --------------------------------


# * ---------------------- dict example --------------------------------

# def ninja_intro(dict):
#     for key, val in dict.items():
#         print(f'I am {key} and I am a {val} belt')


# ninja_belts = {}

# while True:
#     ninja_name = input('add a ninja name: ')
#     ninja_belt = input('add a ninja colour: ')
#     ninja_belts[ninja_name] = ninja_belt

#     while True:
#         another = input('add another? (y/n): ').lower()
#         command = ""
#         if another == 'y':
#             command = "cond"
#             break
#         elif another == "n":
#             command = "break"
#             break
#         else:
#             continue

#     if command == "cond":
#         continue
#     else:
#         break

# ninja_intro(ninja_belts)
