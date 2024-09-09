'''

Creare una lista di stringhe. Scrivere un programma che utilizzi un loop for per stampare ogni elemento della lista.

'''

lista = ["ciao ", "sono ", "una ", "lista"]

for x in lista :

    print(x)

'''

Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.

'''

lista = []

for x in range(1, 11) :

    lista.append(x)
    print(x)

'''

Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.

'''

somma = 0

for x in lista :

    somma += x

print(f"La somma dei numeri è: {somma}")

'''

Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.

'''
lista1 = []

for x  in range(1, 21) :

    lista1.append(x)

for ind in range(len(lista1)) :

    if lista1[ind] % 2 == 0 :

        print(lista1[ind])

'''

scrivere una funzione che prende come parametro una lista e un elemento x 
e restituisce l'indice o gli indici in cui si trova l'elemento sottoforma di una lista
se il programma non trova nulla stampa che l'elemento non si trova nella lista

'''

def cerca_elemento(l, a) :

    listaInd = []
    trovato = False

    for i in range(len(l)) :

        if l[i] == a :

            listaInd.append(l.index(a))
            trovato = True


    if not trovato:

        print(f"L'elemento {a} non è stato trovato")

    else:

        return listaInd

print(cerca_elemento(lista1, 20))
