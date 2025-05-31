temp=float(input("inserisci la tua temperatura"))
farenheit= (temp*9/5)+32
print(f"La conversione in farenheit è: {farenheit}")
if temp>30:
    print(f"Messaggio di avviso")


peso=float(input("inserisci il tuo peso"))
Kg=peso*1000

altezza=float(input("Inserisci la tua altezza"))
Metri=altezza%100

IMC=Kg/Metri**2
if IMC>=18.50 and IMC<=24.9:
    print(f"normale")
elif IMC>=24.9:
    print(f"Sovrappeso")
elif IMC< 18.50:
    print(f"Sottopeso")


#3. Scrivi un programma che permetta all'utente di convertire una certa quantità di valuta da una valuta di partenza a una valuta di destinazione. 
"""
Valuta=int(input("Inserisci il tipo di valuta"))
Quantità=float(input("Inserisci la quantità"))
valuta_destionazione=int(input("Inserisci la valuta di destinazione"))

while Quantità:
    break 
if Valuta=="€":
    valuta_destionazione= Quantità*1.18
    print(f"Il valore in $ è {valuta_destionazione}")
    valuta_destionazione= Quantità/0.8439
    print(f"Il valore in £ è: {valuta_destionazione}")
if Valuta=="$":
    valuta_destionazione= Quantità/1.0771
    print(f"Il valore in € è {valuta_destionazione}")
    valuta_destionazione= Quantità/0.8439
    print(f"Il valore in £ è: {valuta_destionazione}")
if Valuta=="£":
    valuta_destionazione= Quantità/1.29
    print(f"Il valore in € è {valuta_destionazione}")
    valuta_destionazione= Quantità*1.29
    print(f"Il valore in $ è: {valuta_destionazione}")
"""

valuta_di_partenza=int(input("Inserisci la valuta di partenza (1: EUR, 2: Usd, 3 : gbp)"))
importo=float(input("Inserisci importo : "))
valuta_di_destinazione=int(input("Inserisci la valuta di destinazione (1: EUR, 2: Usd, 3 : gbp)"))
 
EUR_to_USD= 1.18
EUR_to_GBP= 0.86
USD_to_EUR= 0.85
USD_to_GBP= 0.72
GBP_to_EUR= 1.16
GBP_to_USD = 1.39
 
if valuta_di_partenza== 1 and valuta_di_destinazione==2:
    calcolo=importo*EUR_to_USD
elif valuta_di_partenza==1 and valuta_di_destinazione==1:
    calcolo=EUR_to_GBP
elif valuta_di_partenza==2 and valuta_di_destinazione==1:
   calcolo=importo*USD_to_EUR
elif valuta_di_partenza==2 and valuta_di_destinazione==3:
    calcolo=importo*USD_to_GBP
elif valuta_di_partenza==3 and valuta_di_partenza==1:
    calcolo=importo*GBP_to_EUR
elif valuta_di_partenza==3 and valuta_di_destinazione==2:
    calcolo=importo*GBP_to_USD
else:
    calcolo=importo
 
print(f"Conversione: {calcolo:.2f} ")

#4. Scrivi un programma  che stampa la tabellina per un numero inserito dall'utente.

numero=int(input("inserisci numero"))
print(f"Tabellina:{numero}")

for i in range(1,11):
    print(f"{numero} x {i}={numero*i}")

#5. Stampare tutti i numeri da 1 a 100, sostituendo i multipli di 3 con "Fizz" e i multipli di 5 con "Buzz". Per i numeri che sono multipli sia di 3 che di 5, stampare "FizzBuzz".
for i in range (1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    if i%3==0:
        print("Fizz")
    if i%5==0:
        print("Buzz")
else:
    print(i)

	# Leggere da tastiera una stringa che contenga
	# almeno una "a". Richiederla finché non valida.
	# Stampare:
	# 1) la lunghezza della stringa;
	# 2) la stringa in maiuscolo, eccetto le "a";
	# 3) il carattere alla posizione 3, se presente,
	# altrimenti l'ultimo carattere;
	# 4) le singole lettere in colonna.

s=input("Inserisci una stringa")
while True:
    if 'a' in s:
        break
        print("Errore: devi inserire almeno una a. Riprova")

lunghezza=len(s)
print(f"Lunghezza {lunghezza}")

stringa_maiuscola="" #partiamo da una parola vuota
for lettera in s:
    print(lettera)
    if lettera == 'a': #stringa_maiuscola
        stringa_maiuscola+='a'
    else: 
        stringa_maiuscola+=lettera.upper()

print(stringa_maiuscola)

if len(s)>4:
    print(f"Terzo carattere {s[3]}")
else: 
    posultimo=len(s)-1 #perchè parte da 0
    print(f"L'ultimo carattere {s[len(s)-1]}")

for lettera in s:
    print(lettera)




