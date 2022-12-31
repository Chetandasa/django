# one
if 1<2:
    print('yes')
# two
if 1<2:
    if 2 < 3:
        print("True")
# three
if 1<2:
    print('first block')
    if 20 < 3:
        print('second block')
# three di only first block vasadi print la anduku ante second block di 20 less then 3 ledu anduku ani radu
# four dindi hello print vasadi 1 is less then 2 ga hello vasadi
if 1 < 2:
    print('hello')
else:
    print('last')
# five dindi last print vasadi 1 is not greater then 2 ga lastvasadi
if 1 > 2:
    print('hello')
else:
    print('last')
# six dindi elif ran print aitadi 1 is not greater then 2 ga andukuani elif ran print aitadi
if 1 > 2:
    print('hello')
elif 3 == 3:
    print('elif ran')
else:
    print('last')
# seven dindi hello print aitadi 1 less then 2 ga anduku ani hello print aitadi mungata vodi
if 1 < 2:
    print('hello')
elif 3 == 3:
    print('elif ran')
else:
    print('last')
## for loops
# one
seq = [1,2,3,4,5,6]
for item in seq:
    # code here
    print(item)
# two
seq = [1,2,3,4,5,6]
for item in seq:
    # code here
    print('chetan')
# three
seq = [1,2,3,4,5,6]
for ronak in seq:
    # code here
    print('ronak')
# four
d = {"Sam":1,"Frank":2,"Dan":3}
for item in d:
    print(item)
# five
d = {"Sam":1,"Frank":2,"Dan":3}
for k in d:
    print(k)
    print(d[k])
# tupeels
# one
mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)
# two
mypairs = [(1,2),(3,4),(5,6)]

for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)
# three
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i + 1
# range
for item in range(10):
    print(item)
# list comprehenion
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)

print(out)
