#########Object Orir\ented Programing#########
## class oyle bir keyword ki bu sayede kendi istedigimiz obje grubunu tanimlayip yartabiliriz
##list,tuple,string bu objelere ornektir
class Dog():
    ###class object attribute
    ##same for any instance of class
    species='mammals'
    def __init__(self,mybreed,name,spots):##Bu metodla su an attribute olusturuyoruz classsin attribute i
        ##attributrs
        #we take in the argument
        ##assign it using self.breed
        self.breed=mybreed###bunun sayeysnde 8.lineda breedi kullanicinin tanimlama imkanini sagladik
        self.name=name
        ##expext boolens
        self.spots=spots
    ###operation/actions----->Methods (method is a function inside a class)
    def bark(self,number):
        print("WOOOFFf!!! my name is {} and my old is {}".format(self.name,number))##burda self name olmali duz name hata veriir cunku selfe atif yapioz


##ustte mybreed sadece parameter yani
my_dog=Dog('huskie','sammy',True)

type(my_dog)
print(my_dog.species)##burda bunun degiskeniz sekilde self metodi olmadan attribute yaptigimiz icin butun doglarin ortak ozelligi oldiu
print(my_dog.breed)
print(my_dog.spots)
##barka number ekleme oncesi ##print(my_dog.bark())###burda parantez bunu alirken ustte almama sebebi ustteki attribute bu metod
print(my_dog.bark(10))

class Circle():
    ##class object attribute
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=self.pi*radius*radius

    ###method
    def get_circumfrance(self):
        return self.radius*self.pi*2####self.pi yerine Circle.pi da yazabiliriz ayni seye denk geliyo
    
my_circle=Circle()
print(my_circle.pi)
my_circle=Circle(30)##ustte default radius 1 olmasina ragmen bu kodla overwright etmis olduk vw radisus 30 olarak guncelllendi
print(my_circle.radius)
print(my_circle.area)

    
########Inheritance and polymorphysim
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("i am an animal")

    def eat(self):
        print("i am eating")
        
my_animal=Animal()
abi=12