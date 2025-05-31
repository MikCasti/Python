from Account_Bancarioex import AccountBancario 

try:
    saldo= float(input("Inserisci il tuo saldo:"))
    nomeCliente= input("Inserisci il tuo nome:")
    numeroConto= int(input("Inserisci il tuo numero del conto:"))
except ValueError:
    print("Not Valid ")

conto1=AccountBancario(nomeCliente,numeroConto,saldo)

conto1.dettagli_conto()
conto1.deposito(100)
conto1.dettagli_conto()
conto1.prelievo(100)
conto1.dettagli_conto
