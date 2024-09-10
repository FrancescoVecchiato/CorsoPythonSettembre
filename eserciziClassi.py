import os
import pickle

class Rettangolo :

    def __init__(self, larghezza, lunghezza) :

        self.larghezza = larghezza
        self.lunghezza = lunghezza

    def __str__(self) :

        return f"Larghezza: {self.larghezza}, Lunghezza: {self.lunghezza}"

    def Perimetro(self) :

        perimetro = (self.larghezza + self.lunghezza) * 2

        return perimetro

    def Area(self) :

        area = self.larghezza * self.lunghezza

        return area

rettangolo = Rettangolo(10, 15)

print(rettangolo)

print(f"Il perimetro è di: {rettangolo.Perimetro()}")
print(f"L'area è di: {rettangolo.Area()}")

'''

Creare una classe Canzone che rappresenta canzoni
Ogni canzone ha un titolo, un autore e l’anno di pubblicazione
La classe implementa il metodo __init__
e il metodo __str__
Creare una lista di canzoni
Creare quindi all’interno della stessa pagina un programma che chiede all’utente cosa vuole fare:
1 aggiungere una nuova canzone
2 cercare una canzone dalla lista per titolo
3 stampare tutte le canzoni di un autore
4 rimuovere una canzone dal titolo
5 uscire dal programma


'''

class Canzone :

    def __init__(self, titolo, autore, anno_pubblicazione) :

        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def __str__(self) :

        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno_pubblicazione}"


#canzoni = []
scelta = 0

if os.path.exists("canzoniSalvate.pkl"):
    with open("canzoniSalvate.pkl", 'rb') as f:

        canzoni = pickle.load(f)
else:

    canzoni = []

'''
f = open("canzoniSalvate.pkl", "rb")
unpickler = pickle.Unpickler(f)
canzoni = unpickler.load()
f.close()
'''

while scelta != 5 :

    scelta = int(input(f"Premere 1 per aggiungere una canzone, premere 2 per cercare una canzone, premere 3 per stampare tutte le canzoni di un autore,"
          f"premere 4 per rimuovere una canzone dal titolo, o premere 5 per uscire dal programma: "))

    if scelta == 1 :

        can = Canzone(str(input(f"Inserire il titolo: ")), str(input(f"Inserire l'autore: ")), str(input(f"Inserire l'anno di pubblicazione: ")))
        canzoni.append(can)

    elif scelta == 2 :

        temp = str(input(f"Inserire il titolo della canzone da cercare: "))

        for i in range(len(canzoni)) :

            if canzoni[i].titolo == temp :

                print(f"La canzone {temp} è stata trovata")

            else:

                print(f"La canzone {temp} non è stata trovata")

    elif scelta == 3 :

        temp  = str(input(f"Inserire l'autore di cui vedere le canzoni: "))

        for i in range(len(canzoni)) :

            if canzoni[i].autore == temp :

                print(f"La canzone: {canzoni[i].titolo} è stata pubblicata da {temp}")

            else:

                print(f"L'autore {temp} non è stato trovato")

    elif scelta == 4 :

        temp = str(input(f"Inserire il titolo della canzone da rimuovere: "))

        for i in range(len(canzoni)) :

            if canzoni[i].titolo == temp:

                canzoni.remove(canzoni[i])
                print(f"La canzone {temp} è stata rimossa")

            else:

                print(f"La canzone {temp} non è stata trovata")

f = open("canzoniSalvate.pkl", "wb")
pickle.dump(canzoni, f)
f.close()


'''

scrivere una classe automobile con 4 attributi: marca, colore, nome conducente e km iniziali
per default gli attributi hanno i seguenti valori: marca = peugeot, colore = nero, nome conducente = nessuno
km iniziali = 16900. La classe deve contenere 3 metodi: scelta conducente(self, nome conducente) che consente 
di assegnare o modificare il nome, distanza percorsa(self, km fine) che consente di calcolare la distanza percorsa
durante il periodo di noleggio, mostrare info(self) che stampa i dati della vettura

'''

class Automobile :

    def __init__(self) :

        self.marca = "Peugeot"
        self.colore = "Nero"
        self.nome = "Nessuno"
        self.km_iniziali = 16900

    def __str__(self) :

        return f"Marca: {self.marca}, Colore: {self.colore}, Nome: {self.nome}, KM: {self.km_iniziali}"

    def scelta_conducente(self, nome):

        self.nome = nome
        print(f"Nome conducente aggiornato, nuovo conducente: {self.nome}")

    def distanza_percorsa(self, km_fine) :

        print(f"LA distanza attualmente percorsa è di: {km_fine - self.km_iniziali}")

        self.km_iniziali += km_fine

    def mostrare_info(self) :

        print(self.__str__())

auto1 = Automobile()
auto1.scelta_conducente("Patrick")
auto1.distanza_percorsa(20000)
auto1.mostrare_info()
