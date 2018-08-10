# Example one: ----
# classes are upper case!
# class Sample():
#   pass

# x = Sample()
# print(type(x))

# Example two: ----
# class Dog():
#     species = "mammal"
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name


# mydog = Dog(breed="Pit", name="fido")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)


# Example 3: -----
class Circle():
   pi = 3.14
   def __init__(self, radius=1): #meaning if i dont define the radius, then its default will be 1
    self.radius = radius

   def area(self):
       return self.radius * self.radius * Circle.pi
   
   def set_radius(self, new_r):  # set object attribute
       self.radius = new_r

myc = Circle(3)
myc.set_radius(100)
print(myc.area())