####string reverse
def reverse(s):
    str=""
    for i in s:
        str=i+str
###recursive
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
 ####list append-pop
 mylist=[1,2,3,4,'efe']
 mylist.append(6)##en sona yerlestirir
 mylist.pop(4)
 mylist.insert(3,'ogulcan')##3.elemente 'ogulcan' koydu
 mylist.remove(2)## 2 yi sili

 def create_list(r1, r2, lst):
    # Base case: if r1 is equal to r2, return the list
    if r1 == r2+1:
        return lst
    # Otherwise, append r1 to the list and call the function again with r1 + 1
    else:
        lst.append(r1)
        return create_list(r1 + 1, r2, lst)
 
 ####
 def count_elements_recursion(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])
    ####
def list_reverser(lst):

    if len(lst)==0:
        return lst
    else:
        lst1=lst[::-1]
        return lst[-1]+list_reverser(lst)
k=[12,23,43,45]
list_reverser(k)
print(k)
#####
try:
    my_list = []
 
    while True:
        my_list.append(int(input()))
 
# if the input is not-integer, just print the list
except:
    print(my_list)
#####
people = {"Jay", "Idrish", "Archi"}
 
print("People:", end = " ")
print(people)
 
# This will add Daxit
# in the set
people.add("Daxit")
 
# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

#######
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
######

# checks if list still
# contains any element
a = [1, 2, 3, 4]
 
while a:
    print(a.pop())
Output
4
3
2
1
#####args
def myfunc(*args):#####istedigim kadar argument tanimlma imkan saglar yoksa buraya mesela x,y dedim anca 2 tane koyabilirdim ve bu arg dedigimiz sey tuple barindiriyor
    return sum(args)*0.5
#####kwargs
def myfunc1(**kwargs):###istedigim gibi dicr=tionary koyabilirim iceri
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('i did nit find any fruits')

myfunc(fruit='apple',veggie='lettuce')
###birlestir
def myfunc2(*args,**kwargs):
    print(args)
    print(kwargs)
myfunc2(10,20,30,fruit:'apple',food:'egg')
##myfunc2(10,20,30,fruit:'apple',food:'egg',50)yapsak hata verir cunku yerleri 50 boxmus oldu
