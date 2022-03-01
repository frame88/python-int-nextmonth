anno = int(input('inserisci un anno: '))
mese = int(input('Inserisci un mese: '))

if mese > 12 or mese == 0:
    print('inpunt non valido')
elif mese == 12:
    print('Il prossimo mese è', 1, anno+1)
else:
    print('Il prossimo mese è: ', mese+1, anno)
    
