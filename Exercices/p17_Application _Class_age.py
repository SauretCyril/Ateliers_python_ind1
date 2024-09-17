
# Application : calcul d’âge

# ▪ Dans la classe Personne, remplacer l’attribut age par date de naissance (year, mounth, day) de type date
# ▪ Définir la méthode calcul_age comme méthode de la classe Personne
# ▪ Définir l’attribut age en utilisant la fonction property

from datetime import date,datetime

class Personne :
    class_attr = 0
    nbre_personnes = 0
    date_format = '%d/%m/%Y'
    
    def __init__(self,nom,prenom,date_str=''):
        self.nom = nom
        self.prenom = prenom
        self.date_saisie = date_str
        self._date_naissance = get_date(date_str)
        self._age = self.calculer_age(self._date_naissance)
        
        Personne.nbre_personnes += 1
    def _get_age(self) :
        return self._age
    
    """si on laisse la fonction il faut calculer la date de naissance en fonction de l'age"""
    # def _set_age(self,age) :
    #     self._age = age
    
    def _get_date_naissance(self):
        return self._date_naissance
    def _set_date_naissance(self,date_str):
          self.date_saisie=date_str
          self._date_naissance = get_date(date_str)
          self._age = self.calculer_age(self._date_naissance)
        
    
    age = property(_get_age)
    
    Date_naissance= property(_get_date_naissance)
    
    def calculer_age(self,date_naissance: date) -> int:
        if date_naissance:
            """retourne l'age en année"""
            aujourdhui = date.today()
            anniversaire = date_naissance.replace(year=aujourdhui.year)
            age = aujourdhui.year - date_naissance.year
            if anniversaire > aujourdhui:
                age -= 1
            return age
        else: 
            return 0
    
    
  
    
def get_date(date_str) -> date:
    """transformer date format str en format date
    sinon redemande à saisir une nouvelle"""
    date_format = '%d/%m/%Y'
    try:
        date_to_return = datetime.strptime(date_str, date_format).date()
        #if not est_bissextile(date_to_return.year) and  :
    except ValueError:
         date_to_return=None
    return date_to_return    
 
 
 
def est_bissextile(annee):
    # Une année est bissextile si elle est divisible par 4
    # mais pas divisible par 100, sauf si elle est aussi divisible par 400
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False


paul=Personne("Atreides","paul","24/01/1980") 
print(Personne.nbre_personnes)

chanie =Personne("Atreides","chanie")
chanie._set_date_naissance("01/12/1974")

print(f"{paul.prenom} {paul.nom} a {paul.age} years old. Il est né le {paul.Date_naissance}")
print(f"{chanie.prenom} {chanie.nom} a {chanie.age} years old. Il est né le {chanie.Date_naissance}")

