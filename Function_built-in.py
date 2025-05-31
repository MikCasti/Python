#Funzioni built-in per Stringhe
"""
len da la lunghezza di una stringa


"""
s1="its"
lunghezza=len(s1)
print(lunghezza)

s2="Its"
confronto=s1==s2
print(confronto)

s3=s2.lower()
print(s3)
s3=s1.upper()
print(s3)

cofronto=s1.lower()==s2.lower()
print(confronto)

presente="i" in s1
print(presente)

inizia=s2.startswith("i")
print(inizia)
fine=s2.endswith("s")
print(fine)

s4="             ciao         "
print(s4)
s5=s4.strip()
print(s5)

print("fase con \n \"apici\"")

conta=s5.count("c")
print(conta)

s6=s5.replace("c","x")
print(s6)

st="abcdefghijklmnopqrstuvwxyz" #0:c 1:i 2:a 3:o
print(st[1])
print(st[2:6])
print(st[2:10:2])

print(st[::-1])




