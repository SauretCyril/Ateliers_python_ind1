
#Context Manager __enter__/__exit__

class Test:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

# t = Test()


with Test() as t:
    '''le systeme execute __enter__ en entrée'''
    print('in') #execute la fonction
    print('ou') #execute la fonction
    '''le systeme execute __exit_en sortie__'''