# Retourner les éléments d'une liste dont les sommes sont nulles
#  ▪ Exemple:
#  ▪ f([1, 2, -3, 5, 7, -12, -5]) -> ([1,2,-3],[5,7,-12],[5,-5])

def trouver_sous_listes_somme_nulle(liste):
    resultats = []
    somme_cumulee = 0
    sommes = {0: [-1]}  # Initialiser avec 0 pour gérer les sous-listes commençant au début

    for i, num in enumerate(liste):
        somme_cumulee += num
        if somme_cumulee in sommes:
            for debut in sommes[somme_cumulee]:
                resultats.append(liste[debut + 1:i + 1])
            print(resultats)
            
        if somme_cumulee in sommes:
            sommes[somme_cumulee].append(i)
        else:
            sommes[somme_cumulee] = [i]

    return resultats

# Exemple d'utilisation
liste = [1, 2, -3, 5, 7, -12, -5]
resultat = trouver_sous_listes_somme_nulle(liste)
#print(resultat)  # Cela imprimera [[1, 2, -3], [5, 7, -12], [5, -5]]

        