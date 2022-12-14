class ContBancar:
    # constructor
    def __init__(self, titularCont, iban):
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0


    def interogareSold(self):
        print(f'Titular: {self.titularCont}')
        print(f'IBAN: {self.iban}')
        print(f'SOLD: {self.sold}')
        print(f'Activ:  {self.activ}')
        print(f'Nr de incercari: {self.incercari_activare}')
        print(f'----------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat ! ')
            self.activ = True
        else:
            print('Pin gresit! ')
            self.incercari_activare = self.incercari_activare + 1
            # self.incercari_activare +=1 se mai poate scrie si asa codul de sus

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f' A-ti alimentat {suma}')
        print(f' Aveti in cont {self.sold}')

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f' A-ti cheltuit {suma}')
            print(f' Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente!')


    def salut(self):
        print(f'Salutare {self.titularCont}')

