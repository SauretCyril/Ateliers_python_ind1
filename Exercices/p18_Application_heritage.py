# Définir la classe Paragraphe qui hérite de la classe str
# ▪ Définir les méthodes
# ▪ cap(self) : qui prend en argument self et retourne la même chaine avec une majuscule au début.
# ▪ iscap(self) : vérifie si une chaîne de caractères est sous format cap.
# ▪ __add__(self, autre) : concatène deux paragraphes en mettant uniquement le deuxième sous format cap.
# ▪ Exemple : Paragraphe(' test') + Paragraphe(' fin chaine') -> ' test Fin chaine'

def Paragraphe(str):
    def cap(self) -> str:
        """met sous format "cap", en mettant le premier caractere en majuscule et le reste en minuscule"""
        chaine_tmp = self.lstrip()
        chaine_tmp = chaine_tmp.capitalize()
        chaine_tmp = chaine_tmp.rjust(len(self))
        return self.capitalize()
    
    def iscap(self) -> bool: 
        chaine_tmp = self.cap(self)
        return chaine_tmp == self
        
    def __add__(self, autre):
        if isinstance(autre, Paragraphe):
            return Paragraphe(self + ' ' + autre.cap())
        return NotImplemented

p1 = Paragraphe(' test')
p2 = Paragraphe(' fin chaine')
resultat = p1 + p2
print(resultat) 