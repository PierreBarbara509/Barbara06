#exo1
message = ("ENTRER VOTRE PHRASE: ")
message= message.lower()
print(message)


#exo2
lavie=("entrer les chaines de caracteres: ")
lavie = lavie.split()
print(lavie)


#exo3
chaine= ("Vous pouvez entrer une chaine de caractere: ")
chaine= ' '.join(w.capitalize() for w in chaine.split())
print(chaine)

#exo4
nom=("on va a la plage: ")
rouge=nom.split()
initiale=[mot[0] for mot in rouge]
vert=''.join(initiale)
print(vert)


#exo5
cout= ("Vous pouvez entrer une chaine a plusieurs caracteres: ")
age= cout.replace("a", "@")
print(age)

#exo6
poulet=("Joyeuse ")
gorge=''.join(reversed(poulet.upper()))
print(gorge)

#exo7

neuf=("avis")
corps=neuf.index("a")
print(corps)


#exo8
fete=("Haaaaaa")
Bon="a"
va=fete.count(Bon)
print(va)

#exo9
ordre=("Lavalas")
liste=[i for i in range(len(ordre))if ordre [i] =='a']
print(liste)

#exo10
sauce=("Pierre Barbara ska_mia")
orange=sauce.replace(" ","")

print(orange)




