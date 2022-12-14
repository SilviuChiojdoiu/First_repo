# lista goala = []
# dict (map) gol = {}

# declarama si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 8}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dict-ul
print(note_elevi)

# aflam note
print(note_elevi['Gigel'])

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea dict-ului
print(len(note_elevi))

# stergem elemente din dict
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi)

#returneaza doar cheile
print(note_elevi.keys())