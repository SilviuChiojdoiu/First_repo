# Slicing

poezie = 'Ana are mare si, este vesela pentru ca este miercuri'
print(poezie [0:len(poezie)]) # extrage toate caracterele de la inceput pana la sfarsit cu specif pozitiei de start (0) si stop (len(pozie) (lung stringului poezie)
print(poezie[:]) # extragem toate caract de la inceput pana la sfarsit cu poz de start si stop implicita
print(poezie[::]) # extragem toate caract -//- start, stop, si pas (implicite sau default)

# extragem toate caracterele de la inceput pana la sfarsit din 2 in 2 caractere
print(poezie[0:len(poezie):2])
print(poezie[::2])

# extragem toate caracterele de pozitia 5 la 13 inclusiv (adica 14)
print(poezie[5:14])

# extragem ultimele 3 caract de la final
print(poezie[len(poezie)-3:len(poezie)])
# sau mai
print(poezie[-3:])
# printam stringul in ordine inversa
print(poezie[::-1])

# Metoda split - spargem poezia in mai multe cuvinte despartite de , - se returneaza o lista de elemente iar splitul se va face la fiecare cuvant
print(poezie.split(sep= ","))
print(poezie.split(sep= " L "))
print(poezie.split(sep = " "))

# Metoda replace - inlocuim o litera cu o alta litera
print(poezie.replace('A', 'm'))
print(poezie.replace('Ana', 'Maria'))

# Metoda upper - scriem cu litere mari textul
print(poezie.upper())
print(poezie.upper(). replace('A', 'a'))

# Metoda index() si metoda find()
print(poezie.index('A')) # >0
print(poezie.index('a')) # > 2
print(poezie.find('a'))
'''dif dintre find si index este faptul ca find returneaza -1 
in care cazul in care caracterul nu este gasit iar index ne returneaza o eroare'''

# print(poezie.find('x'))
# print(poezie.index('x'))

# Metoda isnumeric() ,  metoda count (), metoda capitalize ()
numeric = "1234"
print(poezie.isnumeric())
print(numeric.isnumeric())

print(poezie.count('a'))
print(poezie.count('A'))

print(poezie.capitalize())

# Operatori
# de atribuire : =, +=, -=, *=, /=

# = egal
variabila1 = 7
variabila1 = 53

# += adaugare
# variabila1 += 7 #se adauga 7 la 53 rezultand 60
# print(variabila1)
variabila1 = variabila1+7
print(variabila1)

list1 = [1,2,3]
list2 = [4,5]
print(id(list1), id(list2))
# list1+=list2
# print(list1)
# print(id(list1))
list1=list1+list2
print(list1)
print(id(list1)) # se aloca o noua zona id din memorie

# -= scadere
var2 = 47
var2 -= 7
print(var2) # din 47 se scade valoare 7 iar rez final este suprascris in variabila var2 40
var2 = var2-7
print(var2)

# *= inmultire
var2 = 7
var2 *= 7
print(var2) #= 49
var2 = var2*2 # 49*2 =98
print(var2) # 98

# /= impartire
var2 = 14
var2 /= 7
print(var2) #= 2
var2 = var2/2 # 2/2 =1
print(var2) # 1

# Operatori aritmetici : +, -, *, /, **, %, //

nr1 = 10
nr2 = 4
print(f'Suma este {nr1+nr2}')
print(f'Diferenta este {nr1-nr2}')
print(f'Produsul este {nr1*nr2}')
print(f'Impartirea este {nr1/nr2}')
print(f'Restul impartirii este {nr1%nr2}') # modulo
print(f'Rez. floor division este {nr1//nr2}') #floor division  TAIE ZECIMALE
print(f'Ridicarea la putere este {nr1**nr2}')

# Op. de comparare : ==, <=, >=, < , >, !=(diferit)
# op. de comparatie returneaza un rez de tip boolean
nbr1 = 5
nbr2 = 6
print(nbr1==nbr2)
print(nbr1<=nbr2)
print(nbr1>=nbr2)
print(nbr1<nbr2)
print(nbr1>nbr2)
print(nbr1!=nbr2)

# operatori logici : and, or, not
# ordinea prioritatilor : not > and > or
nmbr1 = 5
nmbr2 = 6
print(nmbr1 > nmbr2 or nmbr1 == nmbr2) # false = false => false
print(nmbr1 > nmbr2 or nmbr1 < nmbr2) # false or true => true
print(nmbr1 > nmbr2 and nmbr1 < nmbr2) # false and true => false
print(not nmbr1 > nmbr2 and nmbr1 < nmbr2) # true and true => true
print(not (nmbr1 > nmbr2 and nmbr1 < nmbr2)) # not (false and true) = not false = true
print(not nmbr1 == nmbr2 and not nmbr1 >= nmbr2) #not false and not flase => true and true => true


# Structura alternativa if