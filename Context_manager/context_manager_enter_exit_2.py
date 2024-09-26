class Test:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

t = Test()

with Test() as p:
    print('in')
    print(1+'t')