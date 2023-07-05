
# ? open() func takes one argument which is relative path
# text = open("files/ipsum.txt")

# for line in text:
#     # ?  rstrip() method removes extra space between lines
#     print(line.rstrip())


# ? Another way to read a file
# text = open("files/ipsum.txt")

# for line in text:
#     print(line.rstrip())


# read_lines = text.readline()
# print(read_lines)


# ? Another way to read a file
# text = open("files/ipsum.txt")

# # ? defining starting character
# text.seek(50)

# # ? readline(100) defining end character
# # ? so it will start the 50th character and ends in 150th character
# read_lines = text.readline(100)
# print(read_lines)

# # ! It must be closed
# text.close()


# ? Another way to read a file
# ? In this example, we dont need to close() method anymore
# def squence_filter(line):
#     return ">" not in line


# with open("files/dna_squence.txt") as text:
#     lines = text.readlines()
#     filterdLines = list(filter(squence_filter, lines))
#     print(filterdLines)


