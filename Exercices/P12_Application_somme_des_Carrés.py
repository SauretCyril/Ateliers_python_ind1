#  Repérer la fonction sum dans la documentation Python
#  • Définir la fonction squares_sum, qui permet de faire la somme des carrés d'une suite quelconque d'entiers
#  • Exemples:– print(squars_sum(3, 5))    
# # 34– print(squars_sum(3, 5, 6)) # 170


def squares_sum(*numbers):
    result =0
    for num in numbers:
        result += pow(num,2)
    
    print (f"square result = {result}")
    

squares_sum(3,5)
#70 au lieu de 170
squares_sum(3,5,6)