

class monentier:
    def __init__(self, n):
        self.n = n
    def carre(self):
        return self.n**2
    def factoriel(self):
        r = 1
        for i in range(2,self.n+1):
            r *= i
        return r