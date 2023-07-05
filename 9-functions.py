
# ? function with default args
# def greetings(msg="Good moorning", name="david"):
#     return msg + " " + name
# ! It cannot invonke before it initialized
# greetings("good night", "john")


# ? default argument can be overwrited like below
# greetMe = greetings(msg="Good evening")
# print(greetMe)


# ? python is first class function
# greetMe = greetings("Good evening")
# print(greetMe)


# ? Using callback example
def myCb(msg, name):
    print(f"callback run. {msg} {name}")


def greetings(msg, name, cb):
    cb(msg, name)


greetings("Hello", "Ahmet", myCb)
