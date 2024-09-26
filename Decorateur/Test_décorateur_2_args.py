# Application décorateur

# ▪ Implémenter les fonctions somme





def entier(func):
    
    def inner1(*args, **kwargs):
         
        returned_value = func(*args, **kwargs)
        # storing time before function execution
        print("after Execution")
        return returned_value
    
    return inner1
  


@entier
def sum_two_numbers(a,b):
    
    print("Inside the function")
    return a + b
    
a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))