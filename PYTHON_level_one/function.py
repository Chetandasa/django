# one
def my_func(param1='default'):
    print("my first pythonn function")
my_func()
# two
def my_func(param1='default'):
    print("my first pythonn function! {}".format(param1))
my_func()
# three
def hello():
    print("hello")

hello()
# four edi print la 5 vasadi 2+3=5 aitadi
def addNum(num1,num2):
    return num1+num2
result = addNum(2,3)
print(result)
# fiveedi print la 23 vasadi
def addNum(num1,num2):
    return num1+num2
result = addNum("2","3")
print(result)
# six edi print la int vasadi integer
def addNum(num1,num2):
    return num1+num2
result = addNum(2,3)
print(type(result))
# seven edi print la str vasadi string
def addNum(num1,num2):
    return num1+num2
result = addNum("2","3")
print(type(result))
# eight edo print 5 vasadi
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry, I need integers!"
result = addNum(2,3)
print(result)
# nine edi print sorry.I need integers! etla vasadi anduku ante ("2","3")edi string unde ga anduku
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry, I need integers!"
result = addNum("2","3")
print(result)
# filter
# ten print la [2,4,6,8]vasadi even numbers
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 ==0

evens = filter(even_bool,mylist)
print(list(evens))
# lambda expression
# eleven print la [2,4,6,8] vasadi even numbers
mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))
# split neku tr yarka ga .lower , .upper , .split
# split one print la ['go sports! ', 'sports'] vasadi
tweet = "go sports! #sports"
result = tweet.split('#')
print(result)
# one print la false vasadi 1,2,3 la x ledu ga anduku ani false
print('x' in [1,2,3])
# two print la true vasadi anduku ante 1,2,3 kada 'x' unde ga anduku
print('x' in [1,2,3,'x'])
