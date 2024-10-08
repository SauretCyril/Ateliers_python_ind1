#  Repérer la fonction sum dans la documentation Python
#  • Définir la fonction squares_sum, qui permet de faire la somme des carrés d'une suite quelconque d'entiers
#  • Exemples:– print(squars_sum(3, 5))    
# # 34– print(squars_sum(3, 5, 6)) # 170


def squares_sum(*numbers):
    """Calcul la somme des carrés d'une suite d'entiers."""
    result =0
    for num in numbers:
        result += pow(num,2)
    return result
    

def main():
    """main procedure"""
    print(f'squares_sum(3, 5) : {squares_sum(3, 5)}')
    print(f'squares_sum(3, 5, 6) : {squares_sum(3, 5, 6)}')


if __name__ == "__main__":
    main()