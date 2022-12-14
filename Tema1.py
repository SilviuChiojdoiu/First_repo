# variabila = zona din memoria unui calculator care tine date
marca = "Peugeot"
model = 3008
dimensiune = 5.5
electric = True
# print(type(marca))
# print(type(model))
# print(type(dimensiune))
# print(type(electric))

# dimensiune = round(dimensiune)
# print(dimensiune)
# print(type(dimensiune))

# print(f'Mi-am cumparat o masina marca {marca}.')
# print(f'Aceasta marca de masina este modelul {model}.')
# print(f'Autoturismul are lungimea de {dimensiune} metri.')
# if electric:
#     print('Imi place acest model deoarece este cu propulsie electrica.')
# else:
#     print('Nu este cu propulsie electrica')


# prenume = input('Prenumele este: ')
# nume = input('Numele este: ')
# print(f'Numele complet are {len(prenume + nume)} caractere.')

# lungimea = int(input('Lungimea triunghiului este: '))
# latimea = int(input('Latimea triunghiului este: '))
# print(f'Aria dreptunghiului este {lungimea*latimea}.')

#
# text = 'Coral is either the stupidest animal or the smartest rock'
# print(f'Cuvantul "the" apare de {text.count(" the ")} ori') # Cuvantul "the" apare de 2 ori


# text = 'Coral is either the stupidest animal or the smartest rock'
# a_text = text.split()
# print(f'Cuvantul "the" apare de {a_text.count("the")} ori in text.')

#Ex_10 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
# text = 'Coral is either the stupidest animal or the smartest rock'
#  # assert text.isdigit() is True

#Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
# Nu se va verifica daca string-ul este impar (se presupune ca vom introduce un numar corect de caractere),
# ci doar se va printa pe ecran caracterul din mijloc.

# text = str(input('Scrie un string: '))
# print(f'Caracterul din mijloc este: {text[(len(text)//2)]}')

#Ex_2 Folosind assert, verifică dacă un string este palindrom.
# text = 'ana'
# assert text == text[::-1], 'Cuvantul nu este palindrom'

#Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

# text = str(input('Scrie un string: '))
# x, y = text.split(' ')
# print(f'Primul cuvant este: {x}')
# print(f'Ultimul cuvant este: {y}')

#Ex_14 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

# text = str(input('Scrie un string: '))
# prima_litera = text[0]
# string_modificat = text[0]+text[1:len(text)-1].replace(prima_litera,prima_litera.upper())+text[len(text)-1]
# print(string_modificat)

#Ex_15 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'
user = str(input('User-ul este: '))
parola = str(input('Tasteaza parola: '))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')


