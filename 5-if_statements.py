# age = int(input("What's  your age: "))

# ? paranthesis are optional
# if (age < 10):
#     # ? indented code blok
#     print("You are young")
# elif age < 40:
#     print("You are adult")
# else:
#     print("You are old")


# ? example
# meaty = input("Do you eat meat? (y/n): ")

# if meaty == 'y':
#     print("cool")
# else:
#     print("Here is the veggie menu...")


# ? Operators
# ? <, >, ==, !=, =>, =<


# ? Ternary assignment
# ? [on_true] if [condition] else [on_false]

# game_type = 'home'
# shirt = 'white' if game_type == 'home' else 'green'

# print(shirt)


# ? ------------------------Truty and Falsy Value------------------
#
#
#


# * FALSY Values
#
# * Sequences and Collections:
# ? Empty lists []
# ? Empty tuples ()
# ? Empty dictionaries {}
# ? Empty sets set()
# ? Empty strings ""
# ? Empty ranges range(0)


# * Numbers
# ? Zero of any numeric type.
# ? Integer: 0
# ? Float: 0.0"
# ? Complex: 0j


# * Constants
# ? None
# ? False

#
# ? Example
a = []


if a:
    print("true")
else:
    print("false")


# * Truty Values
#
# ? By default, an object is considered true.
# ? Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
# ? Numeric values (including negatives). Only zero is falsy
# ? True


b = -10

if b:
    print("true")
else:
    print("false")
