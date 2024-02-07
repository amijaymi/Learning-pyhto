########Inheritance and polymorphysim
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("i am an animal")

    def eat(self):
        print("i am eating")
        
my_animal=Animal()
class Dog(Animal):###burda napiyoruz bir class yaratirken digerini animali base olarak aliyoruz
    def __init__(self):
        Animal.__init__(self)##bu kod sayesinde animali base alip buraya aktardik ve sonuc olarak o classin butun attriubute ve metodlari bu classtada gecerli olur
        print("Dog created") 
    def who_am_i(self):##burda overwrite ettik
        print("I am a dog!")
    def bark(self):
        print("WHOOOOOFFFFFFFF")

my_dog=Dog()
print(my_dog.eat())
print(my_dog.who_am_i())


###Polymorphism
##bu farkli classlarda ayni metodu kullanabilmemiz demektir
class Dog():###burda napiyoruz bir class yaratirken digerini animali base olarak aliyoruz
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + "says woof"
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + "says meow"
niko=Dog("niko")
felix=Cat("felix")
print(niko.speak())
print(felix.speak())
for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())###tabi bura yaptigimiz sey iki farkli class icin ortak bir fonksiyon olusturmus olduk ama bunu yapabilme sebebimiz ikisnde de orttak method olmasi o speak metodu eger baska bir class elemani kullansak ve onda speak olmasaydi kod hata verirdi 
pet_speak(niko)
#########
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
my_animal1=Animal("fred")
#my_animal1.speak()### it expects u to inherit and overwright
class Dog(Animal):
    def speak(self):
        return self.name+ "says woof!"
class Cat(Animal):
    def speak(self):
        return self.name+ "says meow!"
fido=Dog("fido")
milo=Cat("milo")
print(fido.speak())
print(milo.speak())
############################
class Person(object):
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def __init__(self):
        Person.__init__(self,name)
    def isEmployee(self):
        return True
    
#########
class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name,self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        Person.__init__(self,name,idnumber)
        self.salary=salary
        self.post=post
        

        
        

        