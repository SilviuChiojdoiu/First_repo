# dalmatienii
for i in range(0, 102):
    print(f'Dalmatianul cu nr {i}')

# dalmatienii din 2 in 2
for i in range(1, 102, 2):
    print(f'Dalmatianul cu nr {i}')

numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin intermediului indexului
for i in range(0, len(numere)):
    print(f'indexul curent este {i} adica numarul {numere[i]}')
    print(f'numarul curent este {numere[i]}')

# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'suma este {s}')

# de cate ori apare 3 in [3,2,3,5]
cifre = [3, 4, 2, 5, 3, 3, 3]
print(f"Cifra 3 apare de {cifre.count(3)} ori.")

