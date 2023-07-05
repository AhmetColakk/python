num1 = 3.123456
num2 = 2.123456
name = "Ali"

print("Number one is {0:.3} and number two is {1:.1f} name is {2}".format(
    num1, num2, name.upper()))
print(
    f"Number one is {num1:.5} and number two is {num2:.1f} name is {name.upper()}")


# def print_format_table():
#     """
#     ? prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(30, 38):
#             s1 = ''
#             for bg in range(40, 48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')


# print_format_table()
# print('\x1b[10;32;46m' + 'Success!' + '\x1b[0m')
