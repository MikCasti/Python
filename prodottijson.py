import json 
import pyodbc
conn=pyodbc.connect(

'DRIVER= (ODBC Driver 17 for SQL Server);'
'Server=DATA-Castillo;'
'DATABASE=Test_C001;'
'Trusted_Connection=yes'

)

cursor=conn.cursor()
with open("es_prodotti.json") as file: 
    json_string= json.dumps(file)
    dati=json.load(file)

for elemento in dati:
    query="INSERT INTO dbo.prodottiJson (product_id,nome) values (?,?)"
    values=(elemento["product_id"],elemento["nome"])
    cursor.execute(query,values)
for f in elemento["features"]:
    query="insert into prodotti (product_id,features) values (?,?)"
    valori=(elemento["product_id"])
    cursor.execute(query,valori)
    
conn.commit()
cursor.close()
conn.close()

    
