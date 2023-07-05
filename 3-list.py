listOne = [1, 2, 3, 4, 5, 6, 7, ]
listTwo = [1, 2, 3, 4, 5, 6, 7]


# ? reassigning
# listOne = [1, 2]
# print(listOne)


# ? get length of list
# print(len(listOne))

# ? concatenation lists
# newList = listOne + listTwo
# print(newList)


# ? get a value from specific index
# print(listOne[1])

# ? update a value of element by its index number
# listOne[1] = 90
# print(listOne[1])

# ? slice list, (startPoint, endPoint) startPoint is inclusive, endPoint is not inclusive
# ? It returns new list
# newlist = listOne[2:6]
# print(newlist)

# ? push new item to end of list
# listOne.append(30)
# print(listOne)

# ? add new item to list by defining specific location
# ? insert(indexNumber, item)
# listOne.insert(0, 14)
# print(listOne)


# ? delete last item from list
# ? By default, pop without any arguments removes the last item:
# ? pop() returns whatever element it removed
# listOne.pop()
# print(listOne)

# ? pop(index_number) removes the element by providing its index number as argument and returns the element which removed from the list.
# listOne.pop(0)
# print(listOne)

# ? remove() method takes an argument and removes the first found item from the list
# ! if item is not available in the list, gives an error
# listOne.remove(5)
# print(listOne)

# ? delete item via its index number
# ? but it returns nothing
# del(listOne[3])
# print(listOne)

# ? delete items via slicing
# ? but it returns nothing
# del listOne[2:4]
# print(listOne)


# ! clear all elements inside the list but the variable remains as an empty list
# listOne.clear()
# print(listOne)

# ? reverse a list
# ! it mutates original list
# listOne.reverse()
# print(listOne)

# ? in order to create reversed list
# ? reversed() is built-in funcs, and it returns list_reverseiterator object
# ? in order to conver to list, use list() constructor
# newList = list(reversed(listOne))
# print(newList)

# ? another way to reverse a list
# anotherList = listOne[::-1]
# anotherList.append(10)
# print(listOne)
# print(anotherList)

# ? copy a list. This is reference type
# anotherList = listOne
# copyList.append(10)

# print(listOne)
# print(anotherList)

# ? clone a list

# anotherList = listOne.copy()
# anotherList.append(10)
# print(listOne)
# print(anotherList)


# ? another way clone a list
# ? It works with [:] and [::]
# anotherList = listOne[::]
# anotherList.append(10)
# print(listOne)
# print(anotherList)
