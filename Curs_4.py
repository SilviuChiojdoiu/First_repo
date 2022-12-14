# tupluri si dictionare
# 3 tupluri
# definirea unui TUPLU gol :
t = ()
print(type(t))
# definirea unui tuplu populat:
t = ('mere', 'pere', 'gutui', 'nectarine', 'pere')
print(t)
# functii care se pot folosi cu tuple:
# functia .index - ne arata pe ce loc e indexat cuvantul in tuplu
print(t.index('nectarine'))
# functia .count - ne arata de cate ori este cuvantul in tuplu
print(t.count('pere'))

# Dictionare (DICT)
# elementele sunt de tip cheie - valoare
# cheile  trebuie sa fie unice
# cheile servesc drept inlocuitori pt index
# sunt ordonate
# cheia este in partea stanga

# definirea unui dictionar gol
d = {}
print(type(d))

# definirea unui dictionar populat
d ={
    "marca" : "Audi",
    "model" : "TT",
    "an_fabricatie" : 2010,
    "Norma_euro" : "euro 4",
    "combustibil" : "benzina",

}
print(d)
# accesarea elementelor dintr-un dictionar
print(f'Numele masinii este {d["marca"]}.')
print(f'Modelul masinii este {d.get("model")}.')

# adaugam elemente in dict
d["numar_de_locuri"] = 5
print(d)

# actualizarea elementelor dintr-un dict
d.update({"numar_de_locuri" : 5})
print(d)

silviu = {"centuri" : True}
d.update(silviu)
print(d)

# stergerea unui element dintr-un dict
d.pop("Norma_euro")
print(d)

# accesam chei sau valori
print(f'Valorile proprietatilor masinii mele sunt {d.values()}')
print(f'Proprietatile masinii mele sunt {d.keys()}')

# accesarea perechilor cheie-valoare
print(f'Dictionarul este format din urmatoarele elemente {d.items()}')

# dictionar imbricat = adica dictionar in dictionar
apa_plata = {
    "borsec": {
        "nume": "borsec",
        "producator": "borsec",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "aqua carpatica": {
        "nume": "aqua carpatica",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "dorna":
        {
            "nume": "dorna",
            "producator": "dorna",
            "impachetare": "bax",
            "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}
print(apa_plata['aqua carpatica']['impachetare'])
print(apa_plata['dorna']['promovare']['reclama'])

# Structurile repetitive - while, for, for each
# 1. WHILE  - ex o serie de instructiuni atata timp cat o conditie este adevarata
# elementul sau variabila de control se declara de regula in afara while-lului

# ex.1 - printati toate nr de la 1 la 10
# i = 1
# while i <= 10 :
#     print(f'nr curent este {i} ')
#     i = i+1 # incrementam

# ex.2 - printati 101 dalmatieni
# dalmatieni = 1
# while dalmatieni <= 101:
#     print(f'Dalmatianul nr {dalmatieni}')
#     dalmatieni += 1

# ex.3 - printati suma nr de la 1 la 10
i = 0
suma = 0
while i <= 10:
    suma = suma + i
    i = i + 1
    print(suma)

# ex.4 parcurgeti o lista si printati fiecare element
l1 = ['Ramona', 'Dan', 'Alex', 'Iulia', 'Carmen', 'Raul', 'Ramona2', 'Simona', 'Silviu']
i = 0
while i < len(l1) :
    print(l1[i])
    i+=1
print(len(l1))
