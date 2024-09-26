def check(arg):
    def decorateur(f_in):
        def f_out(x):
            assert type(x) == arg
            return f_in(x)
        return f_out
    return decorateur

@check(int) # f = check(int)(f)
def f(x):
    return x**2

print(f(3))
print(f(8))
print(f('t'))
