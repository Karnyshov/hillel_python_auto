import os
import shutil

PATH = 'requirements.txt'
x = "line"
x.upper()

# f = open("readme")  # existed file
# f = open("readme", 'w')  # not existed or existed file, start from empty file
os.listdir

if os.path.exists(PATH):  # False
    f = open(PATH)
    data = f.read()
    f.close()

if os.path.exists(PATH):
    with open(PATH) as f:
        data = f.read()

# f.closed # True
f = open("../../requirements.txt", 'r', encoding='utf8')  # existed file
# text1 = f.read(2)
# # text2 = f.read(5)
#
# print(1, f.read())
# print(2, f.read())
# if f.seekable():
#     f.seek(0)
# print(3, f.read(10))
# print(4, f.readline())
# print(4, f.readlines())
# text = f.read()
print(f.tell(), f.read())
# f.name   # fcntl for linux and mac
# f.close()

# f.write("new file data\n")
# f.writelines(['abc\n', "d\n", 'f\n'])
# f.flush()  # for loops
# f.close()
# oct(141)

dirs = []
files = []
links = []

dirs_and_files = os.listdir("../..")

for item in dirs_and_files:
    item = os.path.join("../../", item)
    if os.path.isdir(item):
        dirs.append(os.path.abspath(item))
    if os.path.isfile(item):
        files.append(os.path.abspath(item))
    if os.path.islink(item):
        links.append(os.path.abspath(item))



x = 0
