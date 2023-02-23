
grocery = ['bread',' milk', 'banana']
enumerateGrocery = enumerate(grocery)
# converting to list
print(type(enumerateGrocery))
print(list(enumerateGrocery))
# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
