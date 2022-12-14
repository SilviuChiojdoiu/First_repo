
# structura alternativa if
# if fara indentare
# a = 5
# b = 10
# if a < b:
# print ('b este mai mare decat a')
# if_else
# if a < b:
#     print ('b este mai mare decat a')
# else:
#     print('Nu este mai mare')

# if_elif_else
# if a < b:
#     print ('b este mai mare decat a')
# elif a == b:
#     print( 'a egal cu b')
# else:
#     print('Nu este mai mare')

# if cu operatori (logici, aritmetici, de comparare)
# if a < b or a == b :
#     print ('mesaj 1')
# else:
#     print('mesaj 2')
'''
Exercitiul 4
RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil, 
atunci acesta va beneficia de o reducere de 10%.
Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
o reducere de 10% daca acestia calatoresc iarna.
De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sb 65 de ani vom 
avea o taxa de lux 3%, daca acestia calatoresc la clasa I, indiferent de anotimp sau o taxa de manipulare de 1% altfel:
'''
# varsta = int(input('Va rugam sa introduceti varsta: '))
# anotimp = str(input('Va rugam sa introduceti anotimpul in care calatoriti: '))
# clasa = int(input('Introduceti clasa: '))
# pretBilet = int(input('introduceti pretul biletului: '))
#
# if varsta > 65:
#     discount = 0.15
# else:
#     nrCopii = int(input('Introduceti nr de copii care insotesc: '))
#     if nrCopii >= 1 :
#         discount = 0.10
# if anotimp == 'iarna':
#     discount += 0.1
# if clasa == 1:
#     taxadelux = 0.03
# else:
#     taxadelux = 0.01
#
# pretBilet = pretBilet - pretBilet * discount + pretBilet * taxadelux
# print(discount,taxadelux, pretBilet)

# A. Scenarii pentru STATEMENT COVERAGE de 100%,
# => Persoana peste 65 de ani care calatoreste iarna la clasa 1
# => Persoana sub 65

#---------------------------------------
# Scenariul : Persoana peste 65 de ani care calatoreste iarna la clasa 1
# test case = cum testam ?
# summary (test condition): Verifica faptul ca pentru un calator peste 65 de ani care calatoreste iarna
# la clasa 1 se aplica un discount de 25% si o taxa de lux de 3%
# Steps to reproduce:
# 1. Intra in aplicatie
# 2. Alege destinatia dorita pentru a identifica pretul de baza al biletului
# 3. Completeaza informatiile legate de varsta, sezon si clasa.
# 4. Verifica pretul calculat al biletului.
# Expected result: Seniorul va primi o reducere de 25% si va plati o taxa de 3% din pretul biletului.




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# STRUCTURI DE DATE
# 1. Lista - se defineste cu paranteze patrate []
# - este o colectie de date, ordonate, cu tipuri de date diferite sau de acelasi fel
# - are proprietatea de a fi mutabila ( adica de a si putea sa isi schimbe elemente)
# Actiuni asupra unei liste: adaugam elemente, stergem elemente, modificam un element de la un anumit index
# sa mutam un element la un anumit index

# 1. declararea si initializarea unei liste goale
a = []
# 2. declararea si initializarea unei liste populate
a_prezenti = ['Raul', 'Simona', 'Alex', 'Dan', 'Ramona1']
a_absenti = ['Silviu', 'Carmen', 'Iulia', 'Ramona']
# string_a = 'Ana are mere si este fericita'
# a_split = string_a.split()
# print(a_split)
# # 3. accesarea elementelor
# print(f'Primul element din lista este: {a_prezenti[0]}')
# print(f'Primul element din lista este: {a_absenti[0]}')
# # 4. accesarea ultimului element din lista
# print(f'Ultimul element: {a_prezenti[len(a_prezenti)-1]}')
# print(f'Ultimul element: {a_prezenti[-1]}')
# # functia .append
# a_prezenti.append('Adela')
# print(a_prezenti)
# # functia .insert
# a_absenti.insert(2,'Adela')
# print(a_absenti)
# # functia .index
# print(a_absenti.index('Iulia'))
# functia .remove
# print(a_prezenti.remove('Dan'))
# print(a_prezenti)
# functia .pop
print(a_absenti.pop(-4))
print(a_absenti)
# functia .count
print(a_prezenti.count('Simona'))
# f. extend = imbina listele . extinde lista cu alta lista
print(a_prezenti.extend(a_absenti))
print(a_prezenti)
# ASCII: https://infoas.ro/lectie/90/codul-ascii-tabel-complet
# putem avea si liste neomogene
lista_neomogena = ['maria', 12, True, 15.3] # - asta este o structura de date




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# SETURI - sunt structuri sau colectii de date NEORDONATE , INUTABILE (NU SE POT MODIFICA VALORILE DATE )
# - se definesc cu o pereche de acolade {}
# operatii: putem accesa, adauga sau sterge elemente

# 1. Definirea unui set gol
set_gol = set()
print(type(set_gol))
# 2. definirea unui set populat
set_populat = {'caine', 'pisica', 'hamster', 'papagal'}
# accesarea unui element din set
# varianta cu operatul IN
print('hamster'in set_populat)
# assert 'tom' in set_populat, 'ERROR: Eroare'

# Functia .add() - adauga un element
# set_populat.add('Gaina')
# print(set_populat)

# functie .pop() - sterge un element la intamplare
# set_populat.pop()
# print(set_populat)

# functia .REMOVE()
set_populat.remove('hamster')
print(set_populat)

# functia .discard() - se executa fara sa returneze eroare
set_populat.discard('broasca')
print(set_populat)

# functia .update(), .union(), .clear()
set_populat.update() # face o concatenare - se
set_populat.union() # creeaza o a 3- a lista care implica concatenarea celor 2 liste implicate
set_populat.clear() # goleste continutul listei set_populat

# tupluri si dictionare


