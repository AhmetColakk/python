age = 25
num = 0

# while num < age:
#     print(num)
#     num += 1

# while num < age:
#     if num % 2 == 0:
#         print(num)
#     num += 1
# ? break and continue keywords are also valid in while loop
while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
        num += 1
    if num > 10:
        break

    num += 1
else:
    print('outside of condition')  # doesn't work when using break
