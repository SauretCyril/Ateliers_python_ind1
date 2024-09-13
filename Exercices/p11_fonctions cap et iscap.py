

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)


def capitalize(chaine):
    
    e1_index_first_letter=len(chaine) - len(chaine.lstrip())
    e2_chaine=chaine[e1_index_first_letter:len(chaine)]
    e3_space=chaine[0:e1_index_first_letter]
    e4_chaine=e3_space+e2_chaine.capitalize()
    return e4_chaine

#print (titlecase(ab))

# majuscule sur la premiere lettre même si il y a des espaces avant
#cap1(' chaine.   test, Ok') 

def cap2(chaine,i):
    if i==0:
        chaine=capitalize(chaine)
    index_point = chaine.find('.', i)
    #print (index_point)
    print(f"{i}={chaine}")
     
    #print(len(chaine))
    if (index_point != -1) and (index_point < len(chaine)):
        start_chaine=chaine[0:index_point+1 ]
        end_chaine=chaine[index_point+1:len(chaine)]
        new_chaineM = cap1(end_chaine)
        chaine=start_chaine+new_chaineM
        chaine=cap2(chaine,index_point+1)
        
        newIndex = chaine.find('.', index_point) 
        if (newIndex != -1) and (newIndex < len(chaine)):
            return chaine 
    else:
         return chaine  
    
          
        

print (cap2(' chaine.   test, Ok,le Rire permet de viellire moins vite. le petit poucet, EtaiT Petit',0))

#print (cap1(' chaine.   test, Ok'))