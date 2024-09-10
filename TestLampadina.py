from lampadina import Lampadina

lamp1 = Lampadina()

lamp1.taratura = int(input(f"Inserire la taratura della lampadina: "))
scelta = 0

while scelta != 3:

    scelta = int(input(f"Premere 1 per premere l'interruttore, premere 2 per visualizzare lo stato della lampadina o premere 3 per uscire dal programma "))

    if scelta == 1:

        lamp1.click()

    elif scelta == 2:

        print(lamp1.visualizza_stato())

