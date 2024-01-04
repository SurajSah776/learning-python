# Reading from a file
f = open("marks.txt", "r")

i = 0
while True:
    line = f.readline()
    if not line:
        break
    # print(line)
    stud1 = int(line.split(",")[0])
    stud2 = int(line.split(",")[1])
    stud3 = int(line.split(",")[2])

    # Printing marks
    print(f"Marks of student-{i+1} in OS : {stud1}")
    print(f"Marks of student-{i+1} in COA : {stud2}")
    print(f"Marks of student-{i+1} in AFL : {stud3}")

    i = i+1
    print(line)
