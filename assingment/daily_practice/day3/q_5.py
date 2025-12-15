from operator import add, mul
def greet(name="User", msg="Welcome"):
    print(msg, name)
greet()
greet("abhi")
greet(name="abhi", msg="Hello")

def apply_function(a, b, func):
    return func(a, b)

print(apply_function(10, 5, add))
print(apply_function(10, 5, mul))