# exercitiul 1 -> for in for ( parcurgerea unei matrici)
# my_list = [
#     [1,"test1"],
#     [2,"test2", 3, "test3"],
#     [34, "test4"],
#     [5]
# ]
# # for in for
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(f'Valoarea curente a elementului din lista de pe pozitia [{i}][{j}] este : {my_list[i][j]}')

# exercitiul 2 -> parcurgeti o lista de elementele, printati elementele pe ecran iar daca gasiti stringul
# gutui, inlocuiti-l cu 'caise'

# fructe = ['gutui', 'prune', 'mere', 'pere']
# for i in range(len(fructe)):
#     print(fructe[i])
#     if fructe[i] == 'gutui':
#         fructe[i] = 'caise'
# print(fructe)

# Ex 3
# avem o lista de culori si vrem sa vindem haine in culorile respective
# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele
# in culoarea respectiva

# cul_disponibile = ['rosu', 'roz', 'verde', 'galben', 'violet', 'magenta', 'maro', 'albastru']
# culori_nepotrivite = ['galben', 'albastru', 'maro']
#
# for culoare in range(len(cul_disponibile)):
#     if cul_disponibile[culoare] in culori_nepotrivite:
#         break
#     print(f'Va recomandam haine in culoarea {cul_disponibile[culoare]}.')

# for each
# parcurgeti lista si daca gasiti sorece il stergeti
animale = ['cal', 'pisica', 'caine', 'magar', 'soarece', 'oaie', 'vaca']
for animal in range(len(animale)-1):
    if animale[animal] == 'soarece':
        animale.pop(animal)
print(animale)

# for each
# nu putem folosi functia .pop() pt ca fct ia ca si parametru indexul
# folosim fct .remove()
for animal in animale:
    if animale == 'soarece':
        animale.remove(animal)
print(animale)

# for else
# printati toate nr pana la 5

for i in range(6):
    print(i)
else:
    print(f'Am terminat!')

# acelasi ex ca mai sus dar alta fct => while

i = 0
while i<= 5:
    print(i)
    i+=1
else:
    print('Am terminat')


# FUNCTII
# definirea unei functii : incepem cu def
# ex.1 - functie simpla
def print_noapte_buna(): # nu avem parametri de aceea sunt goale parantezele
    print('Noapte buna!') # => corpul fctiei ...
    print('Este ora 8')

# print_noapte_buna() # abia acum se printeaza ce am definit mai sus in functie . altfel nu ne afiseaza nimic
#
# print_noapte_buna()
#
# print_noapte_buna()

x = print_noapte_buna() # am apelat functia def
print(x) # nu are ce sa ne returneze

def print_noapte_buna_1():
    print('Noapte buna!')
    print('Este ora 8')
    msg = 'Sunt obosit'
    return msg

y = print_noapte_buna_1() # am apelat functia def
print(y)

# ex. 2 o functie care sa ne calculeze suma a 2 nr. fara parametru ( vom da hard codat = adica trecem noi valorile)
# def calculeaza_suma():
#     a = 3
#     b = 4
#     suma = a + b
#     print(f'Suma celor 2 nr este {suma}')
#     return suma
# calculeaza_suma()
# z = calculeaza_suma()
# print(z)

# Functii cu parametri => specificam si numele informatiei care doreste a fi parametrizata ( oferirea posibilitatii de a
# executa fct de mai multe ori cu valori diferite
# ex.
# def suma(a,b):
#     suma = a + b
#     print(f'Suma celor 2 nr. este: {suma}')
#     return suma
# suma(2,4)


# Fct cu nr indefinit de parametri
# ex. 3 -> calculeaza pretul unui bilet
def pret_bilet(*nr): # (*nr) tine locul a 'n' argumente . Putem trece cand facem apelul fct cate argumente dorim ,2,5,10,etc.
    pret = 0
    for element in nr:
        pret = pret + element
    return pret
print(pret_bilet(2, 6, 7)) #-> 15 . Aici trecem argumente
print(pret_bilet(2, 6, 7, 8, 9, 20)) #-> 52






