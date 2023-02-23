# File name two.py
import one
print("top-level in one.py")
one.func()

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py being imported into another module")