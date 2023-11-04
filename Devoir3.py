# import copy
# #1
# dict={"numero1":"valeur1","numero2":"valeur2","nimero3":"valeur3"}
# key=list(dict.keys())
# valeur=list(dict.values())
# Liste_valeur=list(dict.values())
# print(key)
# print(valeur)
# print(Liste_valeur)
# print()


#2
 

    
    
    
#3
# dictionnaire = {
#     "nom": "Barbara",
#     "age": 22,
#     "ville": "port-au-prince",
#     "pays": "Haiti"
# }

# keys= dictionnaire.keys()

# for keys in keys:
#     print(keys) 
#     print()   

# #4
# day = {
#     'keys1': 'valeur1',
#     'keys2': 'valeur2',
#     'keys3': 'valeur3'
# }

# for valeur in day.values():
#     print(valeur)
#     print()
    


# #5

# diksyone_orijinal = {"kle1": "valè1", "kle2": ["valè2.1", "valè2.2"], "kle3": {"subkle1": "subvalè1"}}

# kopi_diksyone = copy.deepcopy(diksyone_orijinal)


# kopi_diksyone["kle2"][0] = "nouvo_valè2.1"
# kopi_diksyone["kle3"]["subkle1"] = "nouvo_subvalè1"

# print("Diksyone orijinal:", diksyone_orijinal)
# # Diksyone orijinal: {'kle1': 'valè1', 'kle2': ['valè2.1', 'valè2.2'], 'kle3': {'subkle1': 'subvalè1'}}


# print("Kopi a:", kopi_diksyone)
# print()
#  #Kopi a: {'kle1': 'valè1', 'kle2': ['nouvo_valè2.1', 'valè2.2'], 'kle3': {'subkle1': 'nouvo_subvalè1'}}



# #6

# diksyone = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}

# nouvo_diksyone = {kle: f'_{valè}_' for kle, valè in diksyone.items()}

# print(nouvo_diksyone)
# print()



# #7
# couple = {'key1': '123', 'key2': 'abc', 'key3': '456', 'key4': 'def'}

# nombre = {key: valeur for key, valeur in couple.items() if valeur.isdigit()}
# print(nombre)
# print()

# #8
# effort = {'k1': 'valè1', 'k2': 'valè2', 'k3': 'valè3'}

# derouler = [(k, v) for k, v in effort.items()]
# print(derouler)
# print()
# #9
# partage=["base1","base2","base3"]
# message={}
# for base in partage:
#     marche=input(f"Antre definition'{base}': ")
#     message[base]=marche
# print(message)    
# print()
# #10
# liquide1={"pasta":2,"fragrance":3,"texapon":4,"formol":5}
# liquide2={"sel":6,"fragrance":3,"texapon":4,"pasta":2}

# somme={}
# for key,value in liquide1.items():
#     if key in liquide2 and liquide2[key]==value:
#         somme[key]=value
        
# print(somme)
# print()        