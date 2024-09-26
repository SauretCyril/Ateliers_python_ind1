#Application décorateur

# ▪ Implémenter les fonctions somme, produit
# ▪ Implémenter un décorateur qui transforme les paramètres en entiers





def entier(func):
    
    def inner1(*args, **kwargs):
         
        returned_value = func(*args, **kwargs)
        # storing time before function execution
        print("after Execution")
        return returned_value
    
    return inner1
  


@entier
def sum_two_numbers(*args):
    
    print("Inside the function")
    return  
    
a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))