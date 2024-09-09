'''

calcolare con un while come abbiamo visto la media dei numeri somma / cont (Numero degli input ricevuti)

'''

def media_numeri() :

    num = 1
    cont = 0
    somma = 0

    while num != 0  :

        num = int(input("Inserisci un numero: "))
        cont += 1
        somma += num

    print(f"La media dei numeri inseriti è: {somma/(cont -1)}")

media_numeri()

'''

Stampare i numeri interi da 1 a 10 usando un loop while.

'''

num = 0

while num != 10 :

    num += 1
    print(num)

'''

Calcolare la somma dei primi n numeri interi positivi usando un loop while. L'utente deve inserire il valore di n.


'''

cont = 0
somma = 0
num = int(input("Inserisci un numero: "))

while cont != num :

    if num > 0 :

        somma += num

    cont += 1

print(f"La somma dei numeri positivi fino al numero inserito è: {somma}")

'''

Stampare i numeri pari da 2 a 10 usando un loop while

'''

num = 2

while num != 11 :

    if num % 2 == 0 :

        print(num)

    num += 1

'''

Scrivere una funzione che prende come parametri una lista e un elemento a e restituisce true se l'elemento
è presente nella lista e false se non vi è presente

'''

def verifica_presenza(l, a) :

    i = 0
    verifica = False

    while i < len(l) :

        if a == l[i] :

            verifica = True

        else:

            verifica = False

        i += 1

    return verifica

num = int(input("Inserisci un numero: "))
lista = []
uscita = 1

while uscita != 0 :

    lista.append(int(input("popola la lista : ")))

    uscita = int(input("Premere 0 per smettere di popolare la lista: "))


if verifica_presenza(lista, num) :

    print(f"Nella lista è stato trovato l'elemento {num}")

else:

    print(f"Nella lista non è stato trovato l'elemento {num}")
