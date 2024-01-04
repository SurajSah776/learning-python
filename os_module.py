import os
# os.open("OS Module/intro.txt")
print(os.name)
print(os.getcwd())
# os.chdir("E:\\")
# print(os.getcwd())
# os.chdir("E:\Python\CWH Python")
# print(os.getcwd())

# listDir = os.listdir(".")
# print(listDir)

os.chdir("E:\Python\CWH Python\OS Module")
print(os.getcwd())


'''
for i in range(50):
    os.mkdir(f"Folder-{i+1}")  # To create Directories
    # os.rmdir(f"Folder-{i+1}")  # To delete Directories
    for j in range(25):
        os.mkdir(f"Folder-{i+1}\\File-{j+1}")
        # os.rmdir(f"Folder-{i+1}\\File-{j+1}")
        for k in range(25):
            os.mkdir(f"Folder-{i+1}\\File-{j+1}\\Folder-{k+1}")
            # os.rmdir(f"Folder-{i+1}\\File-{j+1}\\Folder-{k+1}")
'''
os.chdir("E:\Python\CWH Python")
print(os.getcwd())

# os.rename("os module", "OS Module")
