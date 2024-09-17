# Application : Itérateur Premiers

# ▪ Définir un itérateur qui retourne les nombres premiers
# ▪ Indications :
# ▪ Définir la méthode premiers qui permet de vérifier si un nombre est premier
# ▪ Définir la méthode __iter__ qui retourne l'objet lui-même
# ▪ Définir la méthode __next__ qui retourne le premier suivant



class PrimeIterator:
    def __init__(self):
        self.current = 1

    def premiers(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while not self.premiers(self.current):
            self.current += 1
        return self.current

# Exemple d'utilisation
prime_iter = PrimeIterator()
for _ in range(10):
    print(next(prime_iter))