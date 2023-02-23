
def funcl(*args,**kwargs):
    for i in kwargs.items():
        print(i)

funcl(a=10,b=20,c=30)