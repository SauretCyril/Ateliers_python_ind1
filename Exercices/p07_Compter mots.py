
# Créer une fonction qui compte le nombre d'occurrences de chaque lettre d'une chaine. 
# f('aaaeed') -> {'a': 3, 'e': 2 , 'd': 1}
#  ▪ Refaire l’exercice avec une fonction qui retourne une liste [('a', 3), ('e', 2 ), ('d', 1)]
#  ▪ Ordonner la liste selon le nombre d'apparition des éléments, en retournant une liste
#  ▪ Indications:
#  ▪ chaine.count('c') : retourne le nbre d'occurrence de 'c' dans chaine
#  ▪ set(L) : retourne un ensemble à partir d'une liste, un set est un groupe d'éléments sans 
# redondance
#  ▪ L.sort(

def f(l,word):
    word.count(l)
    


dic_nb_char={}
chaine='aaaeed'
for l in chaine:
    if not dic_nb_char.get(l):
       dic_nb_char[l]=chaine.count(l)

#Trier le dictionnaire
sorted_dic_nb_char = {k: v for k, v in sorted(dic_nb_char.items(), key=lambda item: item[1])}
print(sorted_dic_nb_char)