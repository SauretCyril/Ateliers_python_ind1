import time


dicL = {}
chaine = 'aaaeed' * 1000000
print(f'set(chaine): {set(chaine)}')

t_start = time.time()
for l in set(chaine):
    if not dicL.get(l):
       dicL[l] = chaine.count(l)
     
t_end = time.time()
print(f'temps execution : {t_end-t_start} (s)')

print(dicL)