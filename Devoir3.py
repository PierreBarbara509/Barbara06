import copy #1
dict={"numero1":"valeur1","numero2":"valeur2","nimero3":"valeur3"}
key=list(dict.keys())
valeur=list(dict.values())
Liste_valeur=list(dict.values())
print(key)
print(valeur)
print(Liste_valeur)
print()


#2
Barbie = input("Tape yon vale: ")

if Barbie.startswith("{") and Barbie.endswith("}"):
    print("vale a gen akolad devan ak dèyè.")
else:
    print("vale a pa gen akolad devan ak dèyè.")
    

    
3
dictionnaire = {
    "nom": "Barbara",
    "age": 22,
    "ville": "port-au-prince",
    "pays": "Haiti"
}

keys= dictionnaire.keys()

for keys in keys:
    print(keys) 
    print()   

#4
day = {
    'keys1': 'valeur1',
    'keys2': 'valeur2',
    'keys3': 'valeur3'
}

for valeur in day.values():
    print(valeur)
    print()
    


#5

dictionnaire1= {"key1": "value1", "key2": ["value2.1", "value2.2"], "key3": {"basekey1": "basevalue1"}}
dictionnaire2= copy.deepcopy(dictionnaire1)


dictionnaire2["key2"][0] = "reponse_value2.1"
dictionnaire2["key3"]["basekey1"] = "poste_basevalue1"

print("dictionnaire1:", dictionnaire1)
print("dictionnaire2:", dictionnaire2)
print()
 


#6

dictionnaire = {'kle1': 'valeur1', 'kle2': 'valeur2', 'kle3': 'valeur3'}

liste = {kle: f'_{valeur}_' for kle, valeur in dictionnaire.items()}

print(liste)
print()



#7
couple = {'key1': '123', 'key2': 'abc', 'key3': '456', 'key4': 'def'}

nombre = {key: valeur for key, valeur in couple.items() if valeur.isdigit()}
print(nombre)
print()

#8
effort = {'k1': 'valè1', 'k2': 'valè2', 'k3': 'valè3'}

derouler = [(k, v) for k, v in effort.items()]
print(derouler)
print()
#9
partage=["base1","base2","base3"]
message={}
for base in partage:
    marche=input(f"Antre definition'{base}': ")
    message[base]=marche
print(message)    
print()
#10
liquide1={"pasta":2,"fragrance":3,"texapon":4,"formol":5}
liquide2={"sel":6,"fragrance":3,"texapon":4,"pasta":2}

somme={}
for key,value in liquide1.items():
    if key in liquide2 and liquide2[key]==value:
        somme[key]=value
        
print(somme)
print()        