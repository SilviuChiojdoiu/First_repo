import keyword
 #VARIABILE

myVarFirstSecond = 3 # varianta camelcase
my_var_first = True # varianta snake case
my_var_first = 3
my_var_first = 'test'
print(my_var_first)


var1 = 'Silviu'
var2 = False
var3 = 33
var4 = 1.67
print('Silviu')
print(var1)
print(str(var2))
print('Varsta mea este: ' + str(var3))


variabila_float = 1.67
variabila_int = 13
print(float(variabila_int))
print(int(variabila_float))


varb1= 'test'
varb2 = 13
varb3 = True
varb4 = 1.87
print(f'prima variabila are valoare {varb1}, a doua variabila are valoarea {varb2}, apoi {varb3} si in final {varb4}')

imi_place_la_curs = True
assert imi_place_la_curs==True, 'Error, error: studenti plictisiti'
print('Test passed, yeyy, fac treaba buna la curs!')
#assert se folosesc pe partea de automation, asa vom testa

a = int(input('Introduceti primul numar: '))
b = int(input('Introduceti al doilea numar: '))
print('Suma celor doua numere introduse de la tastatura este: ', a+b)