import random

'''

Creare un programma che simula il gioco della morra cinese.
Il programma prevede che ci siano due giocatori l’utente e il computer
Quindi in maniera iterativa chiede all’utente di scegliere una giocata la confronta con la giocata del computer,
e a seconda di chi ha vinto aumenta di 1 il punteggio, e stampa le giocate e il vincitore.
Il programma prevede 5 giocate dopodichè termina e stampa il punteggio finale sia dell’utente che del computer.
La giocata del computer deve essere un numero randomico

Consiglio: anche se le giocate sono stringhe (“carta”, “forbici” etc) potete assegnare a ciascuna giocata un numero in maniera da confrontare i numeri 
e non le stringhe

'''

'''
punteggio_pl = 0
punteggio_pc = 0
cont = 5

while cont > 0:

    scelta_pl = int(input(f"Scegli fra carta (1), sasso (2) o forbice (3) "))
    scelta_pc = random.randint(1, 3)

    if scelta_pl == scelta_pc:

        print(f"Pareggio!")

    elif scelta_pl == 1 and scelta_pc == 2:

        punteggio_pl += 1
        print(f"Carta batte sasso, vince il giocatore")

    elif scelta_pl == 2 and scelta_pc == 1:

        punteggio_pc += 1
        print(f"Carta batte sasso, vince il pc")

    elif scelta_pl == 2 and scelta_pc == 3:

        punteggio_pl += 1
        print(f"sasso batte forbice, vince il giocatore")

    elif scelta_pl == 3 and scelta_pc == 2:

        punteggio_pc += 1
        print(f"sasso batte forbice, vince il pc")

    elif scelta_pl == 3 and scelta_pc == 1:

        punteggio_pl += 1
        print(f"forbice batte carta, vince il giocatore")

    else:

        punteggio_pc += 1
        print(f"forbice batte carta, vince il pc")

    cont -= 1

print(f"Il giocatore ha fatto: {punteggio_pl} punti")
print(f"Il pc ha fatto: {punteggio_pc} punti")

if punteggio_pl > punteggio_pc:

    print(f"a fine giocata vince il giocatore!")

elif punteggio_pl < punteggio_pc:

    print(f"a fine giocata vince il pc!")

else:

    print(f"a fine giocata c'è stato un pareggio!")
'''

credito = random.randint(25, 100)
punteggio_pl = 0
punteggio_pc = 0

while credito > 0:

    puntata = int(input(f"Fai la tua puntata o premi 0 per uscire: "))

    if puntata > credito:

        while puntata > credito:

            puntata = int(input(f"Non ti puoi permettere questa puntata, attualmente hai {credito} di credito, riprova: "))

    elif puntata == 0:

        print(f"Terminazione programma...")
        break

    scelta_pl = int(input(f"Scegli fra carta (1), sasso (2) o forbice (3) "))
    scelta_pc = random.randint(1, 3)

    if scelta_pl == scelta_pc:

        print(f"Pareggio!")
        credito -= puntata

    elif scelta_pl == 1 and scelta_pc == 2:

        punteggio_pl += 1
        print(f"Carta batte sasso, vince il giocatore")
        credito += puntata

    elif scelta_pl == 2 and scelta_pc == 1:

        punteggio_pc += 1
        print(f"Carta batte sasso, vince il pc")
        credito -= puntata

    elif scelta_pl == 2 and scelta_pc == 3:

        punteggio_pl += 1
        print(f"sasso batte forbice, vince il giocatore")
        credito += puntata

    elif scelta_pl == 3 and scelta_pc == 2:

        punteggio_pc += 1
        print(f"sasso batte forbice, vince il pc")
        credito -= puntata

    elif scelta_pl == 3 and scelta_pc == 1:

        punteggio_pl += 1
        print(f"forbice batte carta, vince il giocatore")
        credito += puntata

    else:

        punteggio_pc += 1
        print(f"forbice batte carta, vince il pc")
        credito -= puntata

print(f"Il giocatore ha fatto: {punteggio_pl} punti")
print(f"Il pc ha fatto: {punteggio_pc} punti")

if punteggio_pl > punteggio_pc:

    print(f"a fine giocata vince il giocatore!")

elif punteggio_pl < punteggio_pc:

    print(f"a fine giocata vince il pc!")

else:

    print(f"a fine giocata c'è stato un pareggio!")
