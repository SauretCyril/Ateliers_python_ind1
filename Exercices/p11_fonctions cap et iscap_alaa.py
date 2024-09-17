

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)
#print(titlecase(' chaine.   test, Ok,le Rire permet de viellire moins vite. le petit poucet, EtaiT Petit'))
#----------------------------------------------------------------
# majuscule sur la premiere lettre même si il y a des espaces avant
def cap(chaine: str) -> str:
    """met sous format "cap", en mettant le premier caractere en majuscule et le reste en minuscule"""
    # e1_index_first_letter = len(chaine) - len(chaine.lstrip())
    # e2_chaine = chaine[e1_index_first_letter:len(chaine)]
    # e3_space = chaine[0:e1_index_first_letter]
    # e4_chaine = e3_space+e2_chaine.capitalize()
    chaine_tmp = chaine.lstrip()
    chaine_tmp = chaine_tmp.capitalize()
    chaine_tmp = chaine_tmp.rjust(len(chaine))
    return chaine_tmp
#capitalize(' chaine.   test, Ok') 
#----------------------------------------------------------------



#----------------------------------------------------------------
# Mettre en majuscule premiere lettre et lettre qui suit un . sans tenir compte des espace, mettre en minuscule 
# les lettres qui doivent pas être en majuscule
def cap_v2(chaine: str) -> str:
    """Prendre en compte les chaines de caractères contenant un point
    Exemple:
        cap(' chaine. test, Ok') --> ' Chaine. Test, ok'"""
    phrases = chaine.split('.')
    # caped_phrases = map(cap, phrases)
    caped_phrases = map(lambda item: item.lstrip().capitalize().rjust(len(item)), phrases)
    chaine_to_return = '.'.join(caped_phrases)
    return chaine_to_return



def cap_v3(chaine: str) -> str:
    """Prendre en compte les chaines de caractères contenant un point
    Exemple:
        cap(' chaine. test, Ok') --> ' Chaine. Test, ok'"""
    phrases = chaine.split('.')
    for index, ph in enumerate(phrases):
        chaine_tmp = ph.lstrip()
        chaine_tmp = chaine_tmp.capitalize()
        chaine_tmp = chaine_tmp.rjust(len(ph))
        phrases[index] = chaine_tmp
    return '.'.join(phrases)

print(cap_v2(' chaine.   test, Ok,le Rire permet de vieillir moins vite. le petit poucet, EtaiT Petit'))
