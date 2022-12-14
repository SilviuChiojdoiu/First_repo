#>>>>>>>>> MOSTENIREA <<<<<<<<<<<<<
# ex. 1
class Chef():
    cutite = None
    linguri = None
    def __init__(self, nr_cutite):
        self.cutite = nr_cutite
    def make_salad(self):
        print(f'Salad')
    def make_fries(self):
        print(f'fries')

class Chef2():
    sort = 2

class JapaneseChef(Chef): # mosteneste din clasa Chef
    def __init__(self, cantitate_alge, cutite):
        self.alge = cantitate_alge
        self.cutite = cutite
    def make_sushi(self):
        print(f'Sushi')

class ItalianChef(Chef, Chef2): # mosteneste din clasele Chef, Chef2
    tava = 1
    def make_pizza(self):
        print(f'Pizza')

new_chef = Chef(4)
new_chef.make_fries()

japan_chef = JapaneseChef(20, 5)
japan_chef.linguri = 6 # am schimbat valoarea linguri din none in 6
print(japan_chef.linguri)
japan_chef.make_sushi()
japan_chef.make_salad()

mario_chef = ItalianChef(5)
print(mario_chef.tava)
print(mario_chef.sort)
print(mario_chef.linguri)
mario_chef.linguri = 15
print(mario_chef.linguri)


class TokioChef(JapaneseChef): # mostenire pe niveluri in lant incepand de la JapaneseChef pana la Chef
    alge = 300

san_chef = TokioChef(30, 7)
san_chef.make_salad()


class Animale():
    sunet = None
    culoare = None
    specie = None
    varsta = None
    sunet_somn_mancare = None
    def dormi(self):
        print(f'Acum dorm {self.sunet_somn_mancare}')
    def imbatranire(self):
        self.varsta = 1
        print(f'Acum am varsta de {self.varsta}')

class Pisica(Animale):
    toarce = "Da"
    vaneaza_soareci = None
    def toarce_sa_ceri_mancare(self):
        if self.toarce == "Da": # asta se traduce "Daca pisica toarce"
            self.sunet_somn_mancare = "Miau"
        print(self.sunet_somn_mancare)

pisica = Animale()
pisica_mostenitoare = Pisica()
pisica.sunet = "Miau, Miau"
print(pisica.sunet)
print(pisica_mostenitoare.sunet)
pisica.dormi()
pisica_mostenitoare.dormi()
pisica.imbatranire()
pisica_mostenitoare.imbatranire()

# >>>>>>> POLIMORFISM <<<<<<<<<<
# ex. polimorfism cu nr indefinit de argumente

print(len("abc"))
print(len([1,2,3,4]))

def suma_numere(*args):
    suma = 0
    for elemente in args:
        suma = suma + elemente
    return suma

print(suma_numere(5,6))
print(suma_numere(5,6,7))
print(suma_numere(5,6,7,8))


# prin fct initializate cu valoare default.
def add(x,y = 0, z = 0):
    return x+y+z
print(add(5))
print(add(5,6))
print(add(5,6,7))

# prin implementarea aceleeasi metode in 2 clase diferite

class America:
    limba = "engleza"
    imn = "imnul americii"
    drapel = "drapel american"
    def printeaza_limba(self):
        print(f'Limba care se vb in SUA este {self.limba}')

class Romania:
    limba = "romana"
    imn = "desteapta-te romane"
    drapel = "tricolor"
    def printeaza_limba(self):
        print(f'Limba care se vb in RO este {self.limba}')

america = America()
romania = Romania()
america.printeaza_limba()
romania.printeaza_limba()

# ex. Polimorfism din clasa copil in clasa parinte

class Pasare:
    def describe(self):
        print(f'Sunt o pasare')
    def zboara(self):
        print(f'Sunt o pasare, deci zbor')

class Papagal(Pasare):
    def vorbeste(self):
        print(f'Sunt o pasare si vb, deci sunt papagal')

class Pinguin(Pasare):
    def zboara(self):
        print(f'Nu pot zbura, dar sunt imbracat frumos')

# pasare = Pasare()
# pasare.describe()
# pasare.zboara()
# print('>>>>>>>>>>>>>>>>')
# papagal = Papagal()
# papagal.describe()
# papagal.zboara()
# papagal.vorbeste()
# print('>>>>>>>>>>>>>>>>')
# pinguin = Pinguin()
# pinguin.describe()
# pinguin.zboara()

#   Abstractizare - o metoda care nu are corp (ca sa nu fie vizibila) . adica avem doar linia cu def .
# ca metodele sunt marcate prin intermediul unui DECORATOR (raspuns la un interviu)
# proces prin care ascundem o functionalitate specifica fata de utilizator
# un anumit comportament in clasele mostenitoare
# orice clasa cae mostenesca o cls abstracta va fi obligata sa implementeze un comportament din clasa abstracta
# avem 2 forme de abstractizare :  -> interfata ( toate metode clasei sunt abstracte),
#                                  -> abstracta (cand doar unele metode din clasa sunt abstracte)
# DECORATORUL ESTE UN SET DE INSTRUCTIUNI GRUPATE SUB UN NUME CARE SCHIMBA COMPORTAMENTUL FUNCTIEI
# @static meter - poate fi accesata prin intermediul clasei ei


#   ENCAPSULARE - tipuri de accesare:
# public    - adica avem acces la atributele si metodele clasei
# privat    - acces doar la anumite atribute si metode
# protected - acces doar unde se afla clasa


from abc import ABC,abstractmethod
from functools import wraps

class Car(ABC):
    def accelerate(self):
        pass
    def stop(self):
        print(f'STOP')

def upper_case(func):
    @wraps(func)
    def func_wrapper(text):
        return func().upper()
    return func_wrapper

@upper_case
def accelerate(text):
    print(text)

# accelerate()

class Ferrari(Car):
    culoare = None

    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self): # poly
        print("I'm a F, I can't stop")

print(accelerate)
# class Ferrari(Car):
#     culoare =None
#     def accelerate(self):
#         print(f'test')
#     def stop(self):
#         print(f"I'm a Ferrari , i can' STOP")
#
# f = Ferrari
# f.accelerate()





