
# ? to import Planet class from test.py
# from test import Planet

# planetX = Planet('GYX', 200000, 5.5, 'HYU System')
# print(planetX.commons())


# ? using package
# ? create a folder called space and __init__.py file
# ? space is something like package and all the python files are like module
#
# ? so, from space.my_python_file import class, func, var, etc


from space.planet import Planet as A
from space.calc import planet_mass, planet_vol
naboo = A('GYX', 200000, 5.5, 'HYU System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f"{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}")


# ? If you are in a package and want to import module from same package, use .(dot)
# ? from .file_name import class, func, var, etc.
