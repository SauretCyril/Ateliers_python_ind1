

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)
#print(titlecase(' chaine.   test, Ok,le Rire permet de viellire moins vite. le petit poucet, EtaiT Petit'))
#----------------------------------------------------------------
# majuscule sur la premiere lettre même si il y a des espaces avant
def capitalize(chaine):
    
    e1_index_first_letter = len(chaine) - len(chaine.lstrip())
    e2_chaine = chaine[e1_index_first_letter:len(chaine)]
    e3_space = chaine[0:e1_index_first_letter]
    e4_chaine = e3_space+e2_chaine.capitalize()
    return e4_chaine
#capitalize(' chaine.   test, Ok') 
#----------------------------------------------------------------



#----------------------------------------------------------------
# Mettre en majuscule premiere lettre et lettre qui suit un . sans tenir compte des espace, mettre en minuscule 
# les lettres qui doivent pas être en majuscule
def cap(chaine,i):
    #on met tout en minuscule sauf la premiere lettre 
    if i==0:
        chaine=capitalize(chaine)
    index_point = chaine.find('.', i)
    
    if (index_point != -1) and (index_point < len(chaine)):
        start_chaine=chaine[0:index_point+1 ]
        end_chaine=chaine[index_point+1:len(chaine)]
        new_chaineM = capitalize(end_chaine)
        chaine=start_chaine+new_chaineM
        chaine=cap(chaine,index_point+1)
        
        newIndex = chaine.find('.', index_point) 
        if (newIndex != -1) and (newIndex < len(chaine)):
            return chaine 
    else:
         return chaine  
    
          
        

print (cap(' chaine.   test, Ok,le Rire permet de vieillir moins vite. le petit poucet, EtaiT Petit',0))
