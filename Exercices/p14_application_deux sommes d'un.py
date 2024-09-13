
# Retourner les indices des 2 nombres d'une liste dont  la somme est égale à une cible
#  ▪ Exemple :
#  ▪ f((1, 2, 4), 5) -> 0, 2

#pas compris

def f(liste, cible):
    # Dictionnaire pour stocker les valeurs et leurs indices
    valeurs = {}
    
    for i, num in enumerate(liste):
        complement = cible - num 
        print(f"complement = {complement}")
        if complement in valeurs:
            return valeurs[complement], i
        valeurs[num] = i
    
    return None 

print (f((1, 2, 4), 5)) #-> 0, 2