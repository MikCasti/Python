num1=float(input("Inserisci il numero"))
num2=float(input("Inserisci il numero"))
for f in range(1,2):
    operazione= input("inserisci il tipo di operazione")
    if operazione=="+":
        somma= num1 + num2
        print(f"la somma è:{somma}")
    if operazione=="-":
        sottrazione= num1 - num2
        print(f"la sottrazione è: {sottrazione}")
    if operazione=="*":
        moltiplicazione= num1 * num2
        print(f"la moltiplicazione è:{moltiplicazione}")
    if operazione=="/":
    
    if num2 != 0:
        divisione=num1 / num2      
        print(f"la divisione è: {divisione}")
        print(f"Not Valid")