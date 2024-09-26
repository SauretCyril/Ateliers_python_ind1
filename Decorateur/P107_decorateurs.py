
users = {'tom':{'age':56,'métier':'Infor'},'julie':{'age':35,'métier':'avocate'}
      }
droit = {'Infor':False,'avocate':True}


def decorateur(f_in):
    #print('debut')
    print('----------------debut')
    def f_out(arg):
        utilisateur = f_in(arg)
        utilisateur_droit=False
        if utilisateur:
            #print (utilisateur)
            age = utilisateur.get('age')      
            metier = utilisateur.get('métier')
            utilisateur_droit = droit.get(metier)
            if utilisateur_droit:
                print(f"Bonjour {arg} votre age est {age}ans, youpi, vous avez l'autorisation")
            else:
                print(f"Bonjour {arg} votre age est {age}ans vous n'etes pas autorisé domage") 
        else:
            print (f"{arg}, Je vous connez pas !!!")   
    return f_out  
    



@decorateur # f = decorateur(f)
def f(arg):
    if arg in users:
        return users[arg]
    else:
        return None



f('cyril')
f('julie')
f('tom')


