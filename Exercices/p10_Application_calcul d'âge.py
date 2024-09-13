 #Définir une fonction qui prend en argument une date et retourne l’âge.
 # ▪ Indices:
 #      ▪ fromdatetime import date
 #      ▪ aujourdhui = date.today()
 #      ▪ naissance  = date(1980, 2, 28)
 #      ▪ anniversaire = naissance.replace(year=aujourdhui.year)
 #      ▪ anniversaire < aujourdhui

from datetime import date
def calculer_age(date_naissance):
    #yy=date_naissance.year
    aujourdhui = date.today()
    anniversaire = date_naissance.replace(year=aujourdhui.year)
    if anniversaire < aujourdhui:
        print(f"votre aniverssaire est :{anniversaire} vous avez {aujourdhui.year -date_naissance.year} ans")
    else:
        print(f"votre aniverssaire est :{anniversaire} vous aurez {aujourdhui.year-1 -date_naissance.year} ans")
        
    
    
def Ctrl_Format_Date( SToDate):
    one_date = SToDate['date']
    nbSep = one_date.count("/")
    format = one_date.split("/")
    print(f"nbSep {nbSep} / len = {len(format)} -{format} -")
    #peut on aller à la ligne sur une condition ?
    if nbSep==2 and len(format)==3 and (int(format[1])<=12 and int(format[1]!=0)) :
        yy = format[2]
        mm = format[1]
        dd = format[0]
        #print(f"le {dd}/{mm}/{yy}" )
        SToDate['format_ok']=True
        SToDate['date']=date(int(yy), int(mm), int(dd))
    return SToDate


SToDate={'format_ok':False}
isok= SToDate["format_ok"]
while not isok:
    SToDate['date']=input("Quel est votre date de naissance ('JJ/MM/YYYY') ?")
    SToDate['format_ok']=Ctrl_Format_Date(SToDate)
    isok= SToDate["format_ok"]

print(f"Vous êtes né(e) le {SToDate['date']}")
calculer_age(SToDate['date'])