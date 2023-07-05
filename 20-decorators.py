
# ? cough_dec(func) is a decorator func
# ? It takes a parametre such a callback (func), then wrappes that callback.
# ? so then, we can perform any thing before invoking the callback, and after as well
def cough_dec(func):

    def func_wrapper():
        # ? This code will executed before function
        print("*cough*")

        func()  # ? func() is such a callback

        # ? This code will executed code after fuction
        print("*cough*")

        # ! We have to return func_wrapper
    return func_wrapper

# ? Any functions under the @cough_dec decorator will be applied same functionality
# ? decorators does not modify funcs themselves


@cough_dec
def question():
    print("Can you give me a discount on that")

# ! To apply a decoder to any fuc, it must be top of the func


@cough_dec
def another():
    print("another func")


# question()
# another()
