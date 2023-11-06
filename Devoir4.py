import random
import string
import unicodedata


#1
def couple(Base):
    phrase = ''
    for element in Base[::-1]:
        phrase += element
    return phrase

phrase = couple("Amour")
print(phrase)
print()


#2
def aleatoire(n):
    caractere = string.ascii_letters 
    choix= ''.join(random.choice(caractere) for _ in range(n))
    return choix

n = 100 
activation= aleatoire(n)
print(activation)
print()

#3
def son(n):
    if n > 26:
        raise ValueError("N pa sipoze depase 26 pou ka gen yon kòd alfabetik san repetisyon.")
    
    alphabet = list(string.ascii_lowercase)  
    effort = ''.join(random.sample(alphabet, n))  

    return effort

n = 18 
effort = son(n)
print("Kòd aleyatwa alfabetik ou an  se:", effort)
print()



#4
def cause(n):
    if n > 36:
        raise ValueError("N pa ka depase 36 poum ka gen yon kòd alfanimerik san repetisyon.")
    
    element = string.digits + string.ascii_letters  
    pause= ''.join(random.sample(element, n))  

    return pause

n = 30 
pause = cause(n)
print("Kòd aleyatwa alfanimerik ou an se:", pause)
print()



#5

def generate_slug(input_string):
    slug = input_string.lower()
    slug = unicodedata.normalize('NFC', slug)
    slug = ''.join(chaine if chaine.isalnum() or chaine == '-' else '' for chaine in slug)
    slug = slug.replace(' ', '-')
    return slug

input_string = "je vais bien"
slug = generate_slug(input_string)
print(slug)  
print()





#6
def charge(Bon, jour):
    temps = jour.join(Bon)
    return temps

nombre= 'Barbara'
jour = ','
cours = charge(nombre, jour)
print(cours)
print()



#7

def vehicule(objectif, vitesse):
    correcteur = '-'.join(str(vitesse.index(element) + 1) for element in objectif)
    return correcteur

vitesse = 'abcdefghijklmnopqrstuvwxyz'  
maintenir = vehicule('correcteur', vitesse)
print(maintenir)

#8
def instable(pousser):
    sa = 'abcdefghijklmnopqrstuvwxyz'  
    envoyer = ''

    bon = pousser.split('-')  

    for prise in bon:
        prise= int(prise)  

        if 0 <= prise < len(sa):
            chose = sa[prise]  
            envoyer+= chose
        else:
            envoyer+= '-' 
    return pousser

pousser = "0-4-8-14-13-19-4"
envoyer = instable(pousser)
print(envoyer)  




#9
def charmant(periode1, periode2):
    notion = (periode1, periode2)
    return notion

base1= 14
base2 = 'Pierre'
Note = charmant(base1, base2)
print(Note)
print()

#10
def courtois(type):
    dev= ''.join(doux[0].upper() for doux in type.split('-'))
    return dev

mot= "Barbara-pierre-ska-mia"
dev = courtois(mot)
print(dev)











