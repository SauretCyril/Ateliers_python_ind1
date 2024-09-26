# Application – Timer MetaClass

# • Définir une méta-classe, qui permettra d’afficher les temps d’exécution des méthodes de ses instances classes
# class MetaTimer(type):
# ...

# class Calcul(metaclass=MetaTimer):
# def __init__(self, n):
# self.n = n

# def somme_carre(self):
# '''somme des carrés des entiers inférieurs à n'''

# def liste_premiers(self):
# '''la liste de tous les nombres premiers inférieurs à n'''

import time

class MetaTimer(type):
    def __new__(cls, name, bases, dct):
        for attr, value in dct.items():
            if callable(value):
                dct[attr] = cls.time_method(value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def time_method(method):
        def timed(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time of {method.__name__}: {end_time - start_time:.4f} seconds")
            return result
        return timed

class Calcul(metaclass=MetaTimer):
    def __init__(self, n):
        self.n = n

    def somme_carre(self):
        '''somme des carrés des entiers inférieurs à n'''
        return sum(i**2 for i in range(self.n))

    def liste_premiers(self):
        '''la liste de tous les nombres premiers inférieurs à n'''
        primes = []
        for num in range(2, self.n):
            is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
            if is_prime:
                primes.append(num)
        return primes

# Exemple d'utilisation
calcul = Calcul(1000)
print(calcul.somme_carre())
print(calcul.liste_premiers())