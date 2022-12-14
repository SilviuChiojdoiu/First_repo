# ex. 1
# note_muzicale = 'do re mi fa sol la si do'
# print(note_muzicale)
# print(note_muzicale[::-1])
# print(note_muzicale[0:len(note_muzicale)])

# ex. 2
# print(note_muzicale.count('do'))

# ex. 3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)
lista3 = [*lista1, *lista2]
print(lista3)

# ex.4
lista3 = list(set(lista1 + lista2))
print(lista3)
lista3.sort()
print(sorted(lista3))

# ex.5
if lista3 == []:
    print('Lista este goala!')
else:
    print('Lista nu este goala!')

# ex.6
lista3.clear()
print(lista3)

# ex.7
if lista3 == []:
    print('Lista este goala!')
else:
    print('Lista nu este goala!')

# ex.8
dict1 = {'Ana' : 8, 'Gigel': 9, 'Dorel': 5}
print(dict1)
dict1.keys()
print(dict1.keys())

# ex.9
for key, value in dict1.items():
    print(key, ' a luat nota', value)

# ex.10
dict1['Dorel'] = 6
print(dict1['Dorel'])

# ex.11
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# ex.12
zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# ex.13
if weekend.issubset(zile_sapt) == True:
    print('Weekend este un subset al zilelor din saptamana ')
else :
    print('Weekend nu este un subset al zilelor din saptamana')

# ex.14
dif_seturi = zile_sapt.difference(weekend)
print(dif_seturi)

# ex.15
inter_seturi = zile_sapt.intersection(weekend)
print(inter_seturi)


echipa = ['juc_1', 'juc_2','juc_3', 'juc_4', 'juc_5']
schimbari_efectuate = 1
schimbari_maxime = 3
if 'juc_2' in echipa:
    print("Da,este in teren")
elif