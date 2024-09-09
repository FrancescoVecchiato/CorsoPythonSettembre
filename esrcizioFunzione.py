'''

creiamo una funzione stampaPerimetro che stampa il perimetro di un rettangolo,
la funzione ha due parametri la base e l'altezza di un rettangolo e ritorna il valore del perimetro.
Invocare la funzione più volte con diversi parametri

'''

def CalcoloPerimetroRettangolo(b, a):

    perimetro = (b + a) * 2

    return perimetro

base = 12
altezza = 5

print(f"Il risultato è: {CalcoloPerimetroRettangolo(base, altezza)}")

base = 4
altezza = 18

print(f"Il risultato è: {CalcoloPerimetroRettangolo(base, altezza)}")

'''

creiamo una funzione stampaArea che stampa l'area di un rettangolo, 
la funzione ha due parametri base e altezza e ritorna l'area del rettangolo. 
Invocare la fuznione con diversi parametri

'''

def CalcoloArea(b, a):

    area = b * a

    return area

base = 13
altezza = 6

print(f"Il risultato è: {CalcoloArea(base, altezza)}")

base = 5
altezza = 19

print(f"Il risultato è: {CalcoloArea(base, altezza)}")

'''

creare la funzione RinnovoPatente la funzione ha due parametri uno è l'anno di nascita l'altro è la data di scadenza della patente.
 Se l'utente ha meno di 18 anni o più di 85 anni la funzione stampa rinnovo rifiutato. 
 Altrimenti stampa rinnovo eseguito e aumenta di dieci anni la data di scadenza della patente e la stampa. 
 Parte pro: aggiungere un parametro booleano visitaRinnovo che se è true consente il rinnovo altrimenti lo rimanda ad una nuova visita

'''

def RinnovoPatente(a, s, r):

    if r :

        if (2024 - a) < 18 or (2024 - a) > 85 :

            print("Rinnovo rifiutato")

        else:

            s += 10

            print(f"Rinnovo eseguito: Nuova scadenza: {s}")

    else :

        print("Rimandato al prossimo rinnovo")

anno = 2000
scadenza = 2024
visitaRinnovo = True

RinnovoPatente(anno, scadenza, visitaRinnovo)

'''

creare una funzione che calcola se l'anno corrente è bisestile.
Ogni anno che è equamente divisibile per 4 e 400 è un anno bisestile

'''

def CalcoloBisestile(a) :

    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0) :

        print(f"Il {a} è un anno bisestile")

    else :

        print(f"Il {a} non è un anno bisestile")

anno = 2000

CalcoloBisestile(anno)

anno = 1900

CalcoloBisestile(anno)
