###############practises
##lesser or greater
def lesser_of_two_evens(x,y):
    if x%2==0 and y%2==0:
        if x>y:
            return y
        else:
            return x
    else:
        if x>y:
            return x
        else:
            return y

#######
def animal_crackers(word):
    i=0
    j=0
    for letter in word:
        if letter==" ":
            j=i+1###beginning index of second word
        i+=1
    if word[0]==word[j]:
        return 
    print(j)
animal_crackers('abimin kagxi')
###2.yontem
def animal_crackers2(word):
    word_list=word.upper().split()##burda eger iki kelimeden biri kucuk biri buyuk basliyosa ikisini de buyuk yapa ve problemin cozer
    if word_list[0][0]==word_list[1][0]:
        return True
animal_crackers2('abimin agzi')


######macdonaldm

def macdonald(txt):
    the_other1=(txt[:3:])
    the_other2=(txt[3::])
    yeni=the_other1.capitalize()+the_other2.capitalize()
    print(yeni)
    return yeni

    
macdonald('sokacam ha bak')
###################
def master_yoda(sentence):
    if len(sentence)==0:
        return ''
    elif len(sentence)==1:
        return sentence


    else:
        return master_yoda(sentence[1::]) + sentence[0]
print(master_yoda('abim'))
############### level 2 problems:
def has_33(lst):
    i=0
    while i<len(lst):
        if lst[i]==3:
            if lst[i]==lst[i+1]:
                return True
            else:
                pass
has_33([1,2,3,4,3,3])
##########paper doll
def paper_doll(word):
    lst=[]
    for letter in word:
        lst.append(letter)
        lst.append(letter)
        lst.append(letter)
    print(str(lst))
    return
paper_doll('efe')


######summer69
def summer_69(arr):
    i=0
    for val in arr:
        i=0
        if val==6:
            p=i
        if val==9:
            o=i
        i+=1
    for val in range(arr[p],arr[o]):
        arr.remove(val)
    



            
            

