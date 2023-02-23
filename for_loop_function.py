
def func1():
    x=10
    def func2(x):
        return x+1
    return func2(x)

result=func1()
print(result)
