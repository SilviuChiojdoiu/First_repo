# ex. Obligatorii
# ex.1  -------------------------------------------------------------
import math
from datetime import date

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    def descrie_cerc(self):
        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def aria(self):
        self.aria = self.PI * self.raza ** 2
        return self.aria

    def diametru(self):
        self.diam = self.raza * 2
        return self.diam

    def circumferinta(self):
        return self.diam * self.PI

Cerc1 = Cerc(3, "Albastru")
Cerc1.descrie_cerc()
print(f'Aria cercului este {Cerc1.aria()}')
print(f'Dimetru cercului este {Cerc1.diametru()}')
print(f'Circumferinta cercului este {Cerc1.circumferinta()}')


# ex.2  -------------------------------------------------------------
class Dreptunghi():

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Lungimea este {self.lungime}!')
        print(f'Latimea este {self.latime}!')
        print(f'Culoarea este {self.culoare}!')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

dreptunghi = Dreptunghi(2,3, "Albastru")
dreptunghi.descrie_dreptunghi()
print(f'Aria dreptunghiului este {dreptunghi.aria()}')
print(f'Perimetrul dreptunghiului este {dreptunghi.perimetru()}')

# ex.3 -------------------------------------------------------------

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele angajatului este {self.nume} {self.prenume} si are salariul de {self.salariu} lei.')

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}.')

    def salariu_lunar(self):
        print(f'Salariul lunar este de : {self.salariu} lei.')

    def salariu_anual(self):
        self.salariu_anual = self.salariu * 12
        print(f'Salariul anual este de : {self.salariu_anual} lei.')

    def marire_salariu(self, marire):
        self.salariu = self.salariu + (marire/100 * self.salariu)
        print(f'Salariul dupa o marire de {marire} % este de : {self.salariu} lei.')

angajat = Angajat('Chiojdoiu', 'Silviu', 3000)
angajat.descrie()
angajat.nume_complet()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu(50)


# ex.4  -------------------------------------------------------------

class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul: {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei !')

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f'Contul {self.iban} a fost debitat cu suma de {suma} lei. Mai aveti disponibil {self.sold} lei. ')

    def creditare_cont(self,suma):
        self.sold += suma
        print(f'URA! Contul {self.iban} a fost creditat cu suma de {suma} lei. Aveti disponibil {self.sold} lei.')

cont1 = Cont('R0ZBR000123456789','Chiojdoiu Silviu', 5500)
cont1.afisare_sold()
cont1.debitare_cont(95)
cont1.creditare_cont(55)

# ex. Optionale
from tabulate import tabulate

class Factura:
    serie_factura = "CS-12-2022"

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        print(f'Noua cantitate este {cantitate}')

    def schimba_pretul(self, pret):
        self.pret_bucata = pret
        print(f'Noul pret este {pret}')

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume
        print(f'Numele produsului {self.nume_produs} s-a schimbat in {nume}')

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_bucata, self.cantitate*self.pret_bucata, date.today(), self.serie_factura]],
                       headers=['Produs', 'Cantitate', 'Pret Bucata', 'Total', 'Data', 'Serie Factura']))

fact1 = Factura(5, "Snickers", 7, 700)
fact1.genereaza_factura()


# ex.6

class Masina:
    marca = 'Renault'
    model = None
    viteza_max = 0
    viteza_actuala = 0
    culori_disponibile = ['alb', 'gri',' negru', 'albastru', 'portocaliu','rosu']
    culoare = 'gri'
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoare}')
        print(f'Masina este inamtriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii este: {self.culoare}')
        else:
            print('ERROR: Culoarea aleasa nu exista.')

    def accelereaza(self, viteza):
        if viteza <= 0:
            print(f'ERROR')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
            print(f'Viteza este : {self.viteza_actuala} km/h')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Daca viteza este {self.viteza_actuala} atunci masina se va opri')

car1 = Masina('Megane', 210)
car1.descrie()
car1.inmatriculare()
car1.descrie()
car1.vopseste_masina('Alb')
car1.descrie()
car1.accelereaza(70)
car1.descrie()
car1.franeaza()
car1.descrie()









