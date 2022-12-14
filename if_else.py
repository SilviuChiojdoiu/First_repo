# if
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dau mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = 0
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:        # daca restul impartirii nr la 2 egal 0 atunci nr este par
    print ('nr par')
else:                   # altfel nr este impar
    print('impar')

# este un nr pozitiv?
if (nr>0):
    print('pozitiv')
else:
    print("nr nu este pozitiv")

# if, else if, else

# cum ne saluta robotelul in functi de ora ?
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int
ora = int(input('Introdu ora'))
if ora < 0:
    print('Ora invalida')
elif ora <= 11:
    print('Neata dulceata!')
elif ora <= 18:
    print('Buna ziua scumpete')
elif ora <= 21:
    print('Seara Buna')
elif ora <= 24:
    print('Noapte Buna')
else:
    print('ora este mai mare de 24')
# CTRL + / - selectezi si deselectezi daca vrei sa mai rulezi sau nu o linie de cod

# functia switch
# exemplul unui robot telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0 :
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales romana')
elif optiunea == 2:
    print('ati ales engleza')
else:
    print('nu am identificat nici o optiune, mai incearca')