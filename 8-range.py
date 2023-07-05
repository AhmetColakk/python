
# ? range genartes iteration with specific times with its argument
# ? In this case 5 times (0 to 5) 5 is not inclusive
# for n in range(5):
#     print(n)

# ? range(startPoint, endPoint) endPoint is not inclusive
# for n in range(5, 15):
#     print(n)

# ? range(startPoint, endPoint, step)
# ? Every iteration (step) is increased 4, defaut is 1
# for n in range(0, 20, 4):
#     print(n)

burger = ["beef", "chicken", "veg", "supreme", "double"]

for n in range(len(burger)):
    print(burger[n])
