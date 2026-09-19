# print("hello world")

# 02 variables 

first_name = "atif" # snake case writing
firstName = "ali" # camel case writing
FirstName = "ali khan" # Pascal case writing
firstname = "amina" # simple case writing
first1name = "adil" # number case writing

# illegal variable name
# $hello = "ana"

# 03 data types: primitive / non-primitive : call by reference / call by value

name = "hello" # string
age = 22 # number, integer , float
human = True # boolean 

lst = [1,2,3,True,"hello"] # list, array 
tup = (1,2,3) # tupple
dic = {"name":"ana","age":34} # dictionary
set1 = {1,2,3,4,5,5}

# 04 user input

# name = input("Enter your name? ")
# print(name)

# if else statements

marks = 90

# if marks > 100:
#     print("your marks is out of range")
# elif marks >= 90:
#     print("your marks is >= 90")
# else:
#     print("your marks is < 90")

# if (marks >= 90 and marks <= 100):
#     print(" your marks are <= 90 and >= 100")
# else:
#     print(" your marks is out of range")

# h = 4
# a = 17
# e = 12

# num = int(input("enter the number"))
# print(type(h) , type(num), num)

# if ( h > 5 and a >= 18) or ( a >= 18 and e >= 12) or (e >= 12 and h > 5):
#     print(" you are in")
# else:
#     print(" out")

# age = 20

# match(age):
#     case 18: print(" your age is 18")
#     case 19: print("your age is 19")
#     case _ : print("nothing ", age)


# 06 loops 

# for i in range(1,11,2):
#     print(i, "Pakistan zindabad")

# j = 0
# while (j <= 10):
#     print(j)
#     j = j + 1

# num = int(input("Enter the number: "))

# for i in range (1,11):
#     print(num," * ",i," = ", num*i )

# num = 2
# j = 1
# while(j <= 10):
#     print(num," * ",j," = ", num*j )
#     j = j + 1


# 07 list 


# lst = ["meena","ayesha","anam","eman"]
# lst[0] = "ana"
# lst[1] = "aiza"
# lst.append("aneeta")
# lst.pop(3)
# lst.insert(0,"afaq")

# lst.remove("eman")

# print(lst) 


# 08 tuples

# tup = ("hello world",)

# print(tup, type(tup))



# lst =list(tup)

# print(lst,type(lst))

# lst.append("masoom mehdi")

# print(lst)

# tup = tuple(lst)
# print(tup,type(tup))

# 09 dictionary 

# dic = {"name":"shaista","age":23}
# dic.update({"education":"BSCS"})
# dic.update({"isPHd":True})
# dic.pop("age")

# del dic 
# print(dic)

# print(dic.get("name") )
# print(dic.keys() )
# print(dic.items() )
# print(dic.values() )

# print(dic["name"])


# 10 functions 


b = 10  # global scope

# def sum(a = 10):
#     c = 12 # local scope / function scope

#     # print("hello world " +  str(a))
#     print(f" hello world {a} ")

# sm = input("Enter your number: ")
# sum(sm) 

# *a arbitrary arguments  
# **a Keyword arbitrary arguments

# def sm(*a):
#     print(a[0] + a[1] + a[2])

# sm(1,2,3)

# def sp(a,**b):
#     print(b["name"])

# sp(10,name ="anamika", )


# def sm(*a):
#     print(a[0] + a[1])
# sm(1,2)

# def sm(*a):
#     # print(a[0] + a[1] + a[2])
#         # return sum(a)
#     total = 0
#     for number in a:
#         total = total + number

#     return total

# print(sm(1,2,3))

# def sp(a, **b):
#     print("name", "= " , b["name"])
# sp(11,name="ana",age=33)

# def su(*a,**b):
#     # print( sum(a))
#     # print(b["name"])
#     print(sum(a) * 10, b["name"] )
    

# su(1,2,3,4,name="anamika",age=22)







# a = 10
# b = 15
# print(a,b) 

# a = a +b # 25
# b = a - b # 25 - 15 = 10
# a = a - b # 25 - 10 = 15


# [b,a] = [a, b]
# print(a,b) 


# 11 OOPs

# objects, class, Abstraction,Encapsulation,Polymorphism,inheritance:

# class Huawei:
#     a = 10

# ab = Huawei() 

# print(ab.a)

# class Huawei:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def show(self,a):
#         print("hello world", a, self.name, self.age)

# ab = Huawei()
# ab.show("hello data")

# sm = Huawei("azaaz", 23)
# sm.show(1) 

# sp = Huawei("waqar", 22)
# sp.show(2)

# su = Huawei("masoom", 21)
# su.show(3)

# class Animal:
#     def show(self):
#         print(" animales so sweet ")
#     def deepvally(self):
#         print("Animals are good ")

# class Cat(Animal):
#     def deep(self):
#         pass

# ab = Cat()
# ab.show()
# ab.deepvally()

# class Par:
#     def show(self):
#         print("Parents")
# class Child(Par):
#     def see(self):
#         pass
# class Grandchild(Child):
#     def do(self):
#         pass

# ab = Grandchild()
# ab.show()

# class ParentA:
#     def show(self):
#         print("hello ParentA class")
# class ParentB:
#     def see(self):
#         print("hello ParentB class")

# class Child(ParentA, ParentB):
#     def now(self):
#         pass

# ab = Child()
# ab.see()
# ab.show()



# class ParentA:
#     def Hello(self):
#         print("hello ParentA class")
# class ParentB(ParentA):
#     pass
# class Child(ParentA):
#     def see(self):
#         pass
# ab = Child()
# ab.Hello()

# class Math:
#     def Shape(self):
#         print("this is a shape class")
# class Ractangle(Math):
#     def Shape(self):
#         print("this is a Ractangle class")
# class Circle(Math):
#     def Shape(self):
#         print("this is a Circle class")

# ab = Ractangle()
# ab.Shape()

# class Employee:
#     def __init__(self,name,age, gender, salary):
#         self.name = name 
#         self._age = age 
#         self.gender = gender 
#         self.__salary = salary
#     def show(self):
#         pkg = self.__salary * 1.5 # hide
#         print(self.name, self._age, pkg)

# ab = Employee("shaista", 22, "Female", 190000)

# ab.show()


# class Employee:
#     def __init__(self,name,salary):
#         self.name= name 
#         self.__salary = salary

#     def salary(self):
#         pkg = self.__salary * 1.5 # encapsulation
#         print(f" my name is {self.name} and my salary is {pkg} ")

# ab = Employee("anita", 190000)
# ab.salary() 







