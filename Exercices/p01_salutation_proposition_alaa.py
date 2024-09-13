
# En utilisant la fonction input, écrire un programme qui propose de saisir le nom est renvoie « Bonjour nom ! »
#  ▪ Ajouter au programme précédant la prise en compte du genre et renvoyer « Bonjour genre nom »
#  ▪ Limiter le choix du genre en proposant de choisir un code (1) pour madame et (2) pour monsieur.
#  ▪ Prendre en compte l’heure, pour afficher bonjour ou bonsoir

from datetime import datetime


#print (now)
#print (now.hour)

name = input("quel est votre nom ?: ")
# genre = input("Votre Genre (1=Femme , 2=Homme ): ")

code_genre = None
while code_genre not in ('1', '2'):
    code_genre = input("Votre Genre (1=Femme , 2=Homme ): ")

if code_genre == '1':
    genre = 'Madame'
elif code_genre == '2':
    genre = "Monsieur" 


now = datetime.now()
hour = now.hour

formatted_date = now.strftime("%A, %d %B %Y")
if hour >17:
    poli ="Bonsoir"
else:
    poli ="Bonjour"

print(f"{poli} {genre} {name} il est {hour}h, nous sommes le {formatted_date}")
    
