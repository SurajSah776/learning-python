# Creating and Writing a File
# f = open("demo1.txt", "x")  # File exist error
f = open("demo1.txt", "w")
line = 'Writing a this line to demo1.txt using "w" mode\n'
f.write(line)
f.close

f = open("demo1.txt", "a")
line = "Appending this line to a file"
f.write(line)
f.close

# Opening a file to read
f = open("demo1.txt", "rt")
lines = f.readlines()
print(lines)  # Prints a list of lines
for line in lines:
    print(line)
f.close


# Using writelines() method

lines = ["Hey there\n", "We are using writelines() method\n",
         "to write multiple lines to a file\n"]

f = open("demo2.txt", "w")
f.writelines(lines)
f = open("demo2.txt", "r")
content = f.read()
print(content)


# Alternative of using writelines() as we explicitly need to put '\n' at the end of every line

lines = ["Hey there!!!", "We are using alternative of writelines() method\n",
         "to write multiple lines in a file\n"]
f = open("demo2.txt", "a")

for line in lines:
    f.write(line+"\n")

f = open("demo2.txt", "r")
content = f.read()
print(content)
