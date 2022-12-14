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

c = Car
c.accelerate(Car)

class Ferrari(Car):
    culoare = None

    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self): # poly
        print("I'm a F, I can't stop")

print(accelerate)
class Ferrari(Car):
    culoare =None
    def accelerate(self):
        print(f'test')
    def stop(self):
        print(f"I'm a Ferrari , i can' STOP")

f = Ferrari
f.accelerate(Car)








