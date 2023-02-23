
class Edureka():
    def __init__(self):
        self.__pri=("I am Private")
        self._pro=("I am Protected")
        self.pub=("I am Public")

    def __privateMethod(self):
        print('In private')

ob=Edureka()
print(ob.pub)
print(ob._pro)
print(ob.__pri)