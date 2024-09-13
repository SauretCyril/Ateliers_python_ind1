#  Application itérateur
#  ▪ Créer un generator qui retroune une liste inversée
#  ▪ yrange(10) -> 10 … 1
#  ▪ yrange(10, 5) -> 10 … 6
#  ▪ yrange(10, 5, 2) -> 10 8 6
 
 
# equivalent à for i = 10 to 1 step -1

def yrange(start, stop=None, step=1):
    if stop is None:
        stop = 1
    if step == 0:
        raise ValueError("Le pas ne peut pas être zéro.")
    if start < stop:
        raise ValueError("Le point de départ doit être supérieur au point d'arrêt pour une liste inversée.")
    
    current = start
    while current >= stop:
        yield current
        current -= step

# Exemple d'utilisation
print(list(yrange(10)))        # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(yrange(10, 5)))     # [10, 9, 8, 7, 6]
print(list(yrange(10, 5, 2)))  # [10, 8, 6]
