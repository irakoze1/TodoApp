'''
fruits = ['tititof', 'jody', 'irakoze', 'shima',3,4,9];

for x in range(len(fruits)):
   if fruits[x] == 'tititof' or fruits[x] == 'jody':
        print(fruits[x])
    else:
        print('not tititof')

class Umuntu(object):
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("I am ", self.name, 'I have ', self.age, 'years old')

titi = Umuntu('Irakoze Thierry', 34)

titi.speak()

class Car(object):
    def __init__ (self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def Display(self, showAll):
        if showAll:
            print("This car is %s %s from %s, it is %s and have %s" %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("this car is %s %s from %s" %(self.make, self.model, self.year))
        
nyereka = Car('FORD', 'JEEP', 2012, 'NEW', 0)

nyereka.Display(False) 

li =[1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li))) 

def add(x):
    return x + 7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(isOdd, a))
c = list(map(add,b))
print(c) '''

a = [1,2,3,4,5,6,7,8,9,10]

#newList = list(filter(lambda x: x%2==0,a))

newList = list(map(lambda x: x+5,a))
print(newList)