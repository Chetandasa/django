# INHERITANCE
# 1) print la edi pn print vasaledu error vasadi answer etla ravale
# etla answer ravale "DOG CREATED" , "ANIMAL" , "EATING". pan vasaledu error unde
 class Animal():

     def __init__(self):
         print("ANIMAL CREATED")

     def whoAmI(self):
         print("ANIMAL")

     def eat(self):
         print('EATING')

 class Dog(Animal):

     def __init__(self):
         Animal.__init__(self)
         print("DOG CREATED")

 mydog = Dog()
 mydog.whoAmI()
 mydog.eat()


# SPECIAL METHODScls
# 1) print la  etla ravale pn vasaledu etla answer unde= Title: python, Author: chetan, Pages:200 etla print ravale pan vasaledu
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

b = Book("Python","chetan",200)
print(b)

mylist = [1,2,3]
print(mylist)
