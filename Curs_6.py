# importam clasele pe care le-am declarat in fisierul curs_6_imported
from Curs_6_imported import Test_case1, Test_case2, Test_case3

# math = se cauta dupa modulul (o librarie PYTHON) built-in math apeland functia import()
import math
from math import * # adica : din modulul built-in math importa tot
from math import pi


# >>> POD, CLASE, OBIECTE <<<<

# FUNCTII
# 1. functii cu nr indefinit de parametri *args
# facem o functie care calculeaza pretul unui bilet
# exemplu
def calculeaza_pretul(*pret): # asa se declara un nr indefinit de parametri
    total_pret = 0
    for element in pret:
        total_pret += element
    return total_pret
print(calculeaza_pretul(2, 6, 7))   # suma pt 3 produse
print(calculeaza_pretul(1, 3))      # suma pt 2 produse
print(calculeaza_pretul(2, 6, 7, 1, 3, 2)) # suma pt 6 parametri

# 2. functii cu kwargs -> ** nume_argument
# sunt folosite pentru a parcurge dictionare si a face operatii pe ele
# exemplu:
apa = {
    'borsec': { # key
        'nume': 'borsec', #values
        'producator': 'borsec',
        'imbuteliere': 'sticla'
    },
    'dorna': { # key
        'nume': 'dorna', #values
        'producator': 'dorna',
        'imbuteliere': 'peturi'
    }
}
# def accesare_elemente_dictionar(**kwargs):
#     for key,values in kwargs.items():
#         print(f'Detalii despre apa: {key}')
#         for key_int, values_int in values.items():
#             print(f'Apa {key} are {key_int} : {kwargs[key][key_int]}')
# print(accesare_elemente_dictionar(**apa))
# (**kwargs1, **kwargs2) - aceste tipuri de functii au un nr indefinit de elemente. se foloseste in special la dictionare.

# def accesare_elemente_dictionar1(**param1):
#     for i,j in param1.items():
#         print(f'Detalii despre apa: {i}')
#         for key, values in j.items():
#             print(f'Apa {i} are {key} : {param1[i][key]}')
# print(accesare_elemente_dictionar1(**apa))

# POD - Programare Orientare pe Obiecte (object oriented programing)
# cream un template pt atributele si pt comportamentul unui anumit obiect
# Clasa -> tiparul in sine al POD .
# Obiectul - reprezentarea efectiva a clasei
# cream un obiect prin instantiere.
# Atributele -> Proprietati -> sunt ca niste variabile care au anumite valori
# Metodele -> FUnctii in interiorul clasei - ce actiuni putem face

# Exemplu:
'''Clasa masina
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca
A. O masina de exemplu poate sa aiba urmatoarele PROPRIETATI (<=> ATRIBUTE):
 - culoare
 - viteza
 - an_fabricatie
 - marca
 - model
 - capacitate_rezervor
 - tip_combustibil
 - tractiune
 - serie_sasiu
 - cutie_viteze
 - numar_inmatriculare
B. O masina poate sa faca urmatoarele ACTIUNI ( <=> METODE)
 - pornire de pe loc
 - oprire
 - accelerare
 - franare
 - consum_instant 
 - re
'''
# definirea unei clase se face cu keywordul class
# apoi avem nevoie de un nume pentru clasa. Clasa va incepe cu litera mare si va fi scris in format snake_case sau camelCase
# Dupa nume avem intotdeauna ":"
# class Masina:
    # aici se va scrie corpul clasei

# Constructor = agent responsabil cu crearea obiectului
# Vom vorbim de 2 tipuri de constructori (cei mai uzuali): implicit si explicit. :

# 1. Constructorul explicit = cel care se defineste de noi in cod
# 2. Constructorul implicit = se apeleasza automat de Python atunci cand constructorul explicit lipseste , nu e definit.
#                           = este o bucata de cod care se apeleaza de catre Python
# Definirea unui constructor: __init__()
# Intre paranteze se vor specifica atributele care vrem sa existe in mod obligatoriu la crearea obiectului
# Exista situatia in care sa nu avem nimic intre paranteze. Daca nu avem nimic scris intre paranteze atunci toate atributele vor fi optionale

# Elementul Self -> ne ajuta sa accesam elemente definite in interiorul clasei fie ele atribute sau metode.
# toate trb accesate cu elemetul self.nume_atribut, sau self.nume_metoda

# Exemplu.1
class Scoala:
    # atribute
    nume_director = None # este un keywonrd care da o valoare nula
    nr_clase = 0
    nr_elevi_clasa = 0

    # Metode
    def calc_nr_total_elevi(self, nr_clase, nr_elevi_clasa):
        nr_total_elevi = nr_clase * nr_elevi_clasa
        return nr_total_elevi

# Instantiem un obiect al clasei Scoala care va primi in mod implicit atributele si metodele clasei Scoala
scoala_Bob = Scoala() # adica scaoala_bob va avea nume_director, nr_clase, nr_elevi_clasa
                      # aici se face schimbul de informatii
print(scoala_Bob.nume_director)
scoala_Bob.nume_director = "Ion Bob"
print(scoala_Bob.nume_director)
nr_clase = int(input("Introduceti nr de clase pt scoala Bob: "))
nr_elevi_clasa = int(input("Introduceti nr de elevi in fiecare clasa pt scoala Bob: "))
print(f'Nr total de elevi din Scoala.BOB este: {scoala_Bob.calc_nr_total_elevi(nr_clase, nr_elevi_clasa)}')

# am instantiat un nou obiect al clasei Scoala
scoala_Popovici = Scoala()
scoala_Popovici.nume_director = "Andrei Popovici"
print(f'Nr total de elevi din Scoala.POPOVICI este: {scoala_Popovici.calc_nr_total_elevi(25, 12)}') #Dam valorile parametrilor in mod explicit

continut = math.pi
print(f'pi are valoarea {continut}')

continut2 = math.factorial(3) # 3 factorial adica 1*2*3 = 6 , 5 factorial = 1*2*3*4*5 = 120 , etc
print(f'Factorial de 3 este {continut2}')

my_test_case1 = Test_case1() # obiect = importam clasa , instantiez = instanta a clasei test_case1
my_test_case2 = Test_case2()
my_test_case3 = Test_case3('test_Case_nr_003', 'The test case validates the desing and functionality of the OK button.')

my_test_case1.printeaza_test_case1()
my_test_case2.printeaza_test_case2()
my_test_case3.printeaza_test_case()
print(my_test_case3.return_name())
print(my_test_case3.return_summary())






