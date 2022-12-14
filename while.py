# problema: masina merge pana ramane fara benzina

litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print('Acceleram')
    # scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print ('Se aprinde martorul benzina')
print ('Stop! nu mai ai benzina')