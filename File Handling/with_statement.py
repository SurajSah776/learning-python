# The 'with' statement in file handling is used to automaticall close the file. We do not need to explicitly close the file

with open("demo2.txt", "r") as f:

    lines = f.read()
    print(lines)

"""
# Binary File

f = open("binary.txt", "rb")
line = f.read()
print(line)

f.close()
"""
