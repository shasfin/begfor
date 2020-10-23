alter_liste=[]
alter=input("inserisci numero")
while alter!="Feierabend":
    if alter>=6 and alter<=70:
        alter_liste.append(alter)
    else:
        print "entrata libera"
    alter=input("inserisci numero oppure Feierabend")
    
print alter_liste
