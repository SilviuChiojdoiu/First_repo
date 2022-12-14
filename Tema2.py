# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneza un if else:
# flow-control sau if, else - evalueaza conditii si bifurca codul in functie de rezultat
import random

# 2. Verifica si afiseaza daca x este numar natural sau nu.
# x = 11
# if int(x) == x :
#     print(f'Numarul {x} este natural.')
# else :
#     print(f'Numarul {x} nu este natural.')

# 3. Verifica si afiseaza daca x este numar pozitiv, neutru sau negativ.
# x = 11
# if x > 0 :
#     print(f'Numarul {x} este pozitiv.')
# elif x == 0:
#     print(f'Numarul {x} este neutru.')
# else :
#     print(f'Numarul {x} este negativ.')

# 4. Verifica si afiseaza daca x este intre -2 si 13.
# x = random.randint(-7,18)
# if x > -2 and x < 13 :
#     print(f'Nr {x} este in intervalul -2 si 13.')
# else:
#     print(f'Nr {x} nu este in intervalul -2 si 13.')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
# x = random.randint(5,10)
# y = random.randint(3,4)
# dif = x-y
# print("Diferenta este:",dif)
# if dif < 5 :
#     print('Diferenta este mai mica!')
# else :
#     print('Diferenta nu este mai mica!')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
# x = random.randint(-5,40)
# print(x)
# if not ( x>=5 and x<=27 ):
#     print('Nu este intre 5 si 27.')
# else:
#     print('Este cuprins intre 5 si 27.')

# 7. x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# x = 20
# y = 20
# print("x=",x)
# print("y=",y)
# if x == y :
#  print('Sunt egale!')
# elif x > y :
#  print(f'x este mai mare.')
# else :
#  print(f'y este mai mare.')

# 8. x, y, z sunt laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
# x = 5
# y = 5
# z = 5
# print("x =", x)
# print("y =", y)
# print("z =", z)
# if x == y != z or y == z != x or z == x != y:
#  print('Triunghiul este isoscel!')
# elif x == y == z :
#  print('Triunghiul este echilateral!')
# else :
#  print('Triunghiul este oarecare!')

# 9. Citeste o litera de la tastura. Verifica si afiseaza daca este vocala sau nu.
# litera = input('Scrie o litera: ')
# vocalele_sunt = {'A','E','I','O','U', 'a', 'e', 'i', 'o', 'u'}
# if litera in vocalele_sunt:
#  print("E vocala! ")
# else:
#  print("Nu e vocala! ")

# 10. Transforma si printeaza notele din sistem romanesc in > peste 9 => A, peste 8 => B, peste 7 => C,
# peste 6 => D, peste 4 => E, 4 sau sub =>F

nota = float(input("Care este nota primita? "))
if 9 < nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota > 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 >= nota >= 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu a-ti introdus o nota de la 0 la 10.')


