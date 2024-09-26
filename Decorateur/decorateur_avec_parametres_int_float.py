def check(*args):
    def decorateur(f_in):
        #Pourquoi x ? 
        def f_out(x):
            assert type(x) in args
            return f_in(x)
        return f_out
    return decorateur

@check(int, float)
def f(x):
    return x**2

print(f(3))
print(f('t'))