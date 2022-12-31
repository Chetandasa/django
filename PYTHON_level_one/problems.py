# problem 1
s = 'django'

print (s[0])
print (s[5])
print (s[:4])
print (s[1:4])
print (s[4:])
# epud reverse di ::-1 taskunte reverseaitadi
print (s[::-1])


# problem 2
l = [3,7,[1,4,'Hello']]
# "hello" place la goodby kavale
l [2][2]= 'GoodBy'
print (l)

# problem 3 
# d1,d2,d3 la hello aine print chayale only
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
# d3 la nest_key mungata [1][0] anduku ante
# 'nest_key' 0 ante 'thisis deep'unde 1 'hello' aduku ani 1 vate 0 vatena mala reatun 'hello' vasadi


# problem 4
# mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
mylist = set([1,1,1,1,1,2,2,2,2,3,3,3,3])
print(mylist)

# problem 5
age = 4
name = "sammy"
# age ani name "hello my dog name is sammy and he is 4 years old" etla print kavale
x = "hello my dog name is {name} and he is {age} years old". format(name="sammy",age="4")
print(x)

# etla pn vasadi print
y = "hello my dog name is {a} and he is {b} years old". format(a=name,b=age)
print(y)
