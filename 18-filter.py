grades = ["A", "B", "F", "C", "F", "A"]

# ? filter list's items based on condition
# ? filter() func takes 2 arguments. filter(fuction, my_list)
# ? The first one is function which we will apply our condition on it.
# ? if provided condition is True, that item remained in the list, otherwise it will be filtered out.
# ? The second argument is a list
# ? The filter() func returns a filter object. To conver to list, use list() constructor
# def remove_fails(grade):
#     return grade != "F"


# filtered = list(filter(remove_fails, grades))
# print(filtered)

# ? Traditional way
# filtered = []

# for grade in grades:
#     if grade != "F":
#         filtered.append(grade)


# print(filtered)

# ? comprehension way

filtered = [grade for grade in grades if grade != "F"]
print(filtered)
