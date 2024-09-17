# Application : nombres premiers

# ▪ Ecrire un programme qui renvoi la liste des nombres premiers inférieurs à n.

# ▪ On pourra utiliser:
# ▪ 2 boucles for
# ▪ Range
# ▪ %
# ▪ Break
# ▪ Append pour remplir la liste

# ▪ Calculer le temps d'exécution pour n=10000


import time

def nombres_premiers(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Calcul du temps d'exécution pour n=10000
n = 10
start_time = time.time()
primes = nombres_premiers(n)
end_time = time.time()

print (int(1000 ** 0.5)+1)

print(f"Liste des nombres premiers inférieurs à {n} : {primes}")
print(f"Temps d'exécution : {end_time - start_time} secondes")