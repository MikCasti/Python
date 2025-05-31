try:
    #file = open("esempio.txt","r")
    file = open("c:/tmp/miofile.txt","r")
    contenuto = file.readlines()

    for linea in contenuto:


        print(linea)

    file.close()
except FileNotFoundError:
    print("File non trovato")


file = open("esempio.txt","w") #se non esiste  si crea se no sovrascrive
file.write("Ciao sono un file scritto da Python")
file.close

file = open("esempio.txt","a",encoding="utf-8") #se non esiste  si crea se no sovrascrive
file.write("\n quesra è una vuoa riga")
file.close

with open("esempio.txt","r",encoding="utf-8") as f:
        contenuto=file.read()
        print(contenuto)                                                                                                                                                                                                                                        

with open("esempio.txt","w",encoding="utf-8") as File:
     righe=[]
     righe.append("Prima riga\n")
     righe.append("Seconda riga\n")
     file.writelines(righe)
     