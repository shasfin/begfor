alter_liste=[67,78,45,34,13,12,4,6]

adult_liste=[]
minor_liste=[]

for elem in alter_liste:
    if elem>=18:
        adult_liste.append(elem)
    else:
        minor_liste.append(elem)
        
print alter_liste
print adult_liste
print minor_liste
