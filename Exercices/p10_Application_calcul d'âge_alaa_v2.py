 #Définir une fonction qui prend en argument une date et retourne l’âge.
 # ▪ Indices:
 #      ▪ fromdatetime import date
 #      ▪ aujourdhui = date.today()
 #      ▪ naissance  = date(1980, 2, 28)
 #      ▪ anniversaire = naissance.replace(year=aujourdhui.year)
 #      ▪ anniversaire < aujourdhui

from datetime import date, datetime

def calculer_age(date_naissance: date) -> int:
    """retourne l'age en année"""
    aujourdhui = date.today()
    anniversaire = date_naissance.replace(year=aujourdhui.year)
    age = aujourdhui.year - date_naissance.year
    if anniversaire > aujourdhui:
        age -= 1
    return age


def get_date() -> date:
    """demande à l'utilisateur de saisir une date de naissance et la retourne si date valide
    sinon redemande à saisir une nouvelle"""
    date_format = '%d/%m/%Y'
    while True:
        date_str = input("Quel est votre date de naissance ('JJ/MM/YYYY') ?")
        try:
            date_to_return = datetime.strptime(date_str, date_format).date()
            break
        except ValueError:
            print('Date de naissance erronée, veuillez ressaisir une nouvelle date.')
    return date_to_return


def main():
    """main procedure"""
    date_value = get_date()
    print(f"Votre age: {calculer_age(date_value)} ans.")


if __name__ == "__main__":
    main()
