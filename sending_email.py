
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest, 'w')
        f.write("Wellcome to Python scripting")
        f.close()

dest="C:\\Users\\kukon\\OneDrive\\Desktop\\sample.txt"

createFile(dest)

print("File created")


