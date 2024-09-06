#es1

num = int(input(f"Inserisci un numero: "))

if num >= 0:

    print(f"{num} e positivo")

else:

    print(f"{num} e negativo")

#es2

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))

if num1 > num2:

    print(f"{num1} e maggiore di {num2}")

elif num2 > num1:

    print(f"{num2} e maggiore di {num1}")

else:

    print(f"{num1} e uguale a {num2}")

#es3

stringa = input(f"Inserisci una stringa: ")

if stringa == "":

    print(f"la stringa e vuota")

else:

    print(f"La stringa non e vuota")

#es4

num = int(input("Inserisci un numero: "))

if num % 2 == 0:

    print(f"{num} e pari")

else:

    print(f"{num} e dispari")

#es5

stringa = input(f"inserisci una lettera")

if stringa in ["a", "e", "i", "o", "u"]:

    print(f"{stringa} e una vocale")

else:

    print(f"{stringa} non e una vocale")
