# enclosing function locals
# one
name = 'this is a global name!'

def greet():

    def hello():
        print("hello "+name)

    hello()

greet()

# two
name = 'this is a global name!'

def greet():
    name = "sammy"

    def hello():
        print("hello "+name)

    hello()

greet()

# three
name = 'this is a global name!'

def greet():
    name = "sammy"

    def hello():
        print("hello "+name)

    hello()

greet()
print(name)

# one
x = 50

def func(x):
    print('x is:',x)
    x = 1000
    print('local x changed to:',x)

func(x)
print(x)

# two
x = 50

def func():
    global x
    x = 1000

print("before function call, x is: ",x)
func()

# three
x = 50

def func():
    global x
    x = 1000

print("before function call, x is: ",x)
func()
print("after function call, x is: ",x)

# four
x = 50

def func():
    x = 1000

print("before function call, x is: ",x)
func()
print("after function call, x is: ",x)

# five
x = 50

def func():
    x = 1000
    return x

print("before function call, x is: ",x)
x = func()
print("after function call, x is: ",x)
