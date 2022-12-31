# 1 print la class vasadi[]etla bracket dukl
print(type([]))
# 2 print la tuple vasadi ()etla bracket dukl
print(type(()))
# 3 print la int vasadi number unadi anduku integer.
print(type(200))
# 4 print la float vasadi number sarta point unde ga anduku.
print(type(20.0))
# 5 print la main_.sample vasadi etla unte
class sample():
    pass

x = sample()
print(type(x))
# 6 print la main_.Dog vasadi
class Dog():
    pass

mydog = Dog()
print(type(mydog))
# 7 print la main_.Dog vasadi
class Dog():

    def __init__(self):
        pass

mydog = Dog()
print(type(mydog))
# 8 print la "Lab" vasadi
class Dog():

    def __init__(self,breed):
        self.breed = breed

mydog = Dog(breed = "Lab")
print(mydog.breed)
# 9 print la "lab" ani "Huskie" vasadi
class Dog():

    def __init__(self,breed):
        self.breed = breed

mydog = Dog(breed = "Lab")
otherdog = Dog(breed = "Huskie")
print(mydog.breed)
print(otherdog.breed)
# 10 print la "Lab" ani "sammy" vasadi
class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab",name = "sammy")
print(mydog.breed)
print(mydog.name)
# 11 print la "sammy" ani "mammal" vasadi
class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab",name = "sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
# new examples
# 1) print la 1 vasadi
class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

myc = Circle()
print(myc.radius)
# 2) print la 3 vasdi
class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)
print(myc.radius)
# 3) print la 28.26 vasadi
class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)
print(myc.area())
# 4) print la 31400.0 vasadi
class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)
myc.radius = 100
print(myc.area())
# 5) print la 3133723.14 vasadi
class Circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.area())
