#1
m=50
element=[]
for i in range( m + 1 ):
    if i %2 ==0:
        element.append(i)
print(element)  
print()


#2
terre=[5,6,7,8,9]
oeuvre=[str(n) for n in terre ]
print(oeuvre)
print()


#3
Chaine=('bar ','naika',' love')
Canne=[Liste.capitalize()for Liste in Chaine]
for Liste in Canne:
    print(Liste)
    print()
      
#4      
cours=[7,8,9,2,3,4,5,6,10]
pause=[]
for i in cours:
    if i % 3==0:
        pause.append(i)
print(pause)
print()

#5
bousole=[1,2,5,6,7,8,9,10,11,12,13,14]
send=[]
for i in range(0,len(bousole),3):
    send.append(bousole[i:i+3])
print(send)
print()

#6
ecole = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
ta=[]
for p in ecole:
    if p not in ta:
        ta.append(p)
print(ta) 
print()       


#7
numero1=[4,5,6,7,8,9]
numero2=[2,4,6,8,5,9]
peuple=[n for n in  numero1 if n in numero2]
print(peuple)
print()

#8
element1=[1,2,3,4,5,6]
element2=[2,4,7,8,9,10]
formulaire=[element for element in element1+element2 if (element not in element1) or (element not in element2)]
print(formulaire)
print()


#9
dictionnaire={"kle1":"val1","kle2":"val2","kle3":"val3"}
Liste=[kle for kle in dictionnaire.keys()]
valeur=[valeur for valeur in dictionnaire .values()]
print(Liste)
print(valeur)
print()

#10
inter1=[2,3,4,5]
inter2=[4,6,7,8]
inter3=[1,2,3,9]

reunion1=set(inter1)
reunion2=set(inter2)
reunion3=set(inter3)

communication=reunion1.union(reunion2,reunion3)
commencement_liste=list(communication)

print(communication)
print()