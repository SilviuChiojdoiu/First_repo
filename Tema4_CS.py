# ex.1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')

# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# i = 0
# while i<= len(masini)-1:
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# ex.2
# print()
# for i in range(len(masini)):
#     masini[i] = masini[i].upper()
#     if i==0 or i== len(masini)-1:
#         masini[i] = masini[i].title()
#     else:
#         print(masini)

# ex.3
print()
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Mercedes':
#         print(f'Am gasit masina dorita de dvs: {masina}')
#         break
#     else:
#         print(f'Am gasit masina X. Mai cautam!')

# ex.4
# print()
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         print(f'S-ar putea sa va placa masina {masina}')

# ex.5
# print()
# masini_vechi = []
# i = 0
# while i < len(masini):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         masini_vechi.append(masini[i])
#         masini[i] = "Tesla"
#     i += 1
#     print(f'Masini vechi : {masini_vechi}')
#     print(f'Masini noi: {masini}')

# ex.6
# print()
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# for nume, valoare in pret_masini.items():
#     if pret_masini[nume] < 15000:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {nume}')


# ex.7
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 0
# for numar in numere:
#     if numar == 3:
#         i += 1
#     print(f'Nr 3 apare de {i} ori in lista')

# ex.8
# suma = 0
# for numar in numere:
#     suma += numar
#     print(f'Suma nr este {suma}')

# ex.9
# nr_celmare = 0
# for numar in numere:
#     if numar > nr_celmare:
#         nr_celmare = numar
#     print(nr_celmare)

# ex.10
i = 0
while i <len(numere):
    numere[i] = numere[i] * -1
    i += 1
    print(numere)



