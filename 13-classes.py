
# ? creating class
# ? use Pascal case for naming

# class Planet:
#     # ! in __init__(self) func is constructor where we register properties to class
#     # ! if we don't pass it in __init()__ func like so, python added self arg automatically
#     # ! Hovever, in this case we could not add any properties

#     # ? __init__(self, param) the second parametre(param) is our own parametre which we will use them when createing new instance
#     # ! but we need to register them as below
#     def __init__(self, param) -> None:
#         # ! self parametre refers every individual instance's atributes
#         # ! not whole class, therefore self has no access to out of __init__() func
#         self.name = "Hoth"
#         self.radius = 20000
#         self.gravity = 5.5
#         self.system = "Hoth System"

#         # ? This is how we register our own attributes to class
#         self.distance = param

#     def getInfo(self, arg):
#         # ! in order to access the class's properties, we need to pass self as a first parametre
#         # ? The second parametre(arg) is optional, when we invoke the method, it will be first argument
#         return f"Name is : {self.name}, The distance is: {self.distance} Radius is: {self.radius}, The Gravity is: {self.gravity}, The system is: {self.system}. Arg is: {arg}"

#     def orbit(self):
#         return f"{self.name} is orbiting in the {self.system}"


# hoth = Planet(273)
# # print(f"Name is: {hoth.name}")
# # print(f"Radius is: {hoth.radius}")
# # print(f"Gravity is: {hoth.gravity}")

# ? This how we pass our own arguments into a method
# print(hoth.getInfo("my arg"))


# * -------------------------- An example -------------------------------------
# class Planet:

#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     def orbit(self):
#         print(self)
#         return f'{self.name} is orbiting in the {self.system}'


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# print('Planet stats:')
# print(f'Name: {hoth.name}')
# print(f'System: {hoth.system}')
# print(hoth.orbit())

# naboo = Planet('Naboo', 300000, 8, 'Naboo System')
# print('Planet stats:')
# print(f'Name: {naboo.name}')
# print(f'System: {naboo.system}')
# print(naboo.orbit())


# *--------------------- Instance level Atributes and Methods----------------------
# class Planet:
#     # ? When we define any properties in __init__() func like below,
#     # ? they are know as instance atributes which means they are unique in all instances
#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     # ? When we define any methods like below
#     # ? they are know as instance methods which means they are unique in instance
#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# # ? we can access any instance atributes or methods like below
# print(hoth.gravity)
# print(hoth.orbit())
# ! We cannot access any attributes and methods via class constractor
# ! Below code couses an error
# print(Planet.gravity)

# *----------------------------- Class Level Atributes and Methods---------------------


# class Planet:

#     # ? class level attributes and methods can be accessiable with both class constractor and instance
#     shape = "Rounded"

#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     def fun():
#         # ! This fun() method no access either the attributes of class itself and instance atributes
#         # ! If we pass here any params, when we invoke this method, we pass an argument for it
#         #  ! since its no effect, its pointless
#         return f"Silly Method"

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# ? We access the class level atribute and method in two ways like below
# ? access the attribute via class constractor and instance
# print(Planet.shape)
# print(hoth.shape)

# ? access the method via class constractor
# print(Planet.fun())

# ! Below code couses an error
# ! because "hoth" is an instance and fun() method did not take self parametre
# print(hoth.fun())

# ! Below code couses an error
# ! because Planet is a class and it does not know self since it's not an instance
# print(Planet.orbit())

# NOTE
# * If a method takes self parametre, It's accessiable for instances but it's not accessiable with class constractor

# * If a method does not take any parametre, It's accessiable for class constractor but it's not accessiable for instances

#
#
#

# *----------------------------------- @classmethod Methods -------------------------
# class Planet:
#     shape = "Rounded"

#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

#     # ? @clasmethod method provides methods for both instance and class constractor
#     @classmethod
#     def commons(cls):
#         # ! class methods takes cls parametre which stands for class itself
#         # ! But we can not acces any attributes in __init__() func
#         return f"All planets are {cls.shape}"


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# # # ? class methods can be accessable via both class constractor and instance like below
# print(Planet.commons())

# print(hoth.commons())

# *----------------------------------- @staticmethods Methods -------------------------


# class Planet:

#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

#     # ? @staticmethod has only access passed arguments when we invoke that method
#     @staticmethod
#     def spin(speed="2000 mill spin"):
#         return f"The planet spin {speed}"


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# # ? staticmethod can be used for both class constractor and instance
# print(Planet.spin())
# print(hoth.spin())

# # ? to overwrite the default param
# print(Planet.spin("8000 high speed"))
