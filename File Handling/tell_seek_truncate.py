# We will see tell(), seek() and truncate() functions in File Handling

# seek() and tell() function

with open("demoFile.txt", "r") as f:
    print(f.tell())
    print(f.read())

    f.seek(15)
    print(f.tell())
    print(f.read())
    print(f.tell())

print()

# truncate() function

with open("demoFile1.txt", "w") as f:
    print(f.tell())
    print(f.write("Hello Suraj Kumar Sah, Are you interested in coding? are you?"))
    f.truncate(20)
    print(f.tell())
