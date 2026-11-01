class dog:
    def brk(self):
        print("woof")
d1=dog()
d2=dog()
d1.brk()
print(type(d1))


class student:
    def __init__(self,name,age):
           self.name=name
           self.age=age
first=student("abel",40)

print(first.name)
# instance attributes
class car:
     def __init__(self,brand,price, model):
            self.brand=brand
            self.price=price
            self.model=model
a=car("toyota",344,"2cd") 
b=a.brand,a.price,a.model
a.color=("red")
print(b)

# class attribute
class Circle:
    pi = 3.14159

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.pi * self.r ** 2

print(Circle(2).area())


# class church:
#      churchname="adventist"
#      def __init__(self,name,tithe):
#             self.name=name
#             self.tithe=tithe
# member1= church("temesgen",2344)
# member2= church("kebada",56464)
# print(member1.name,member1.tithe)
# print(member2.name,member2.tithe)
# member1=churchname="protestant"
# print(member1)
# print(member2.churchname)

          # understand ing the methods
class akiba_team:
     def __init__(self,name,active,total):
          self.name=name
          self.active=active
          self.total=total
     def add(self,new):
          self.total+=new
     def minuss(self,remove):
          self.active-=remove

     def show(self):
          print("total number is ",self.total,'the reduce ones',self.active)
     def  final(self):
            print(self.total-self.active)
            
akiba1=akiba_team("temesgen",120,300)
akiba1.add(300)
akiba1.minuss(20)
akiba1.show()
akiba1.final()

# understand ing the _str__ and __repr__
class house:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def __str__(self):
       return f"{self.name} is {self.age} years old"
     def __repr__(self):
             return f"Dog('{self.name}', {self.age})"
h1=house("billad",34)
print(h1) #billad is 34 years old
print(repr(h1)) # Dog('billad', 34)

# Exercise from the slide1
class rectangle:
     def __init__(self,width,height):
          self.width=width
          self.height=height
     def area(self):
            return self.width*self.height
     def perimeter(self):
           return 2*(self.height+ self.width)
    
     def __str__(self):
            return f"Rectangle {self.width}x{self.height}"
     
r1=rectangle(10,20)
print(" the area of R1:",r1.area())
r2=rectangle(30,20)
print( "the area of R2:",r2.area())
r3=rectangle(40,60)
print("the area of R3:",r3.area())
p1=r1.perimeter()
print("the perimeter of r1 :" ,p1)
