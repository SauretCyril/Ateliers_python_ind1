chaine = '  ceci est une CHaine De caRActères'
# cap('  cecI est UNE chaine') -> '  Ceci est une chaine'
# iscap('Chaine') -> booléen

print(f'upper: {chaine.upper()}')
print(f'isupper: {chaine.isupper()}')
print(f'lower: {chaine.lower()}')
print(f'title: {chaine.title()}')
print(f'capitalize: {chaine.capitalize()}')

chaine = '   test  '
print(f'strip: |{chaine.strip()}|')
print(f'lstrip: |{chaine.lstrip()}|')
print(f'rstrip: |{chaine.rstrip()}|')

chaine = 'test'
print(f'rjust: |{chaine.rjust(6)}|')
print(f'ljust: |{chaine.ljust(8)}|')

chaine = 'début. milieu. fin'
print(f"split: {chaine.split('.')}")

liste = ['début', 'milieu', 'fin']
print(f'join: {"-".join(liste)}')
