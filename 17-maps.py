from random import shuffle


def jumble(words):
    anagrams = list(words)
    shuffle(anagrams)
    return ''.join(anagrams)


words = ["beetroot", "carrots", "potatos"]
anagrams = []

# ? Traditional way
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

# ? map() func takes two arguments. The first one is a function, the second one is list
# ? The jumble() func takes one arguments.
# ? When we use map() func, every list's items(words) are passed as a argument of callback func(jumble)
# ? map() func returns a object. To convert to list, use list() constructor
# a = list(map(jumble, words))
# print(a)


# ? comprehension method
anagrams = [jumble(word) for word in words]
print(anagrams)


# ? map fuction can be used for dictionaries but it cycle trough the key
# ? to iterate value, use values() method for dictionaries

# def printInfo(info):
#     return info


# user = {
#     "name": "john",
#     "email": "john@gmail.com"
# }

# a = list(map(printInfo, user.values()))

# print(a)
