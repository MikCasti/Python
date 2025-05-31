"""
nome: str="Pippo"
età: int=40
temperatura: float=36.5
is_online: bool = True 

nome=45
print(nome)
"""
a=4
b=5

op=a+b #somma
print(op)

diff=a-b  #sottrazione
print(diff)

molt=a*b #moltiplicazione
print(molt)

divis=a/b #divisione
print(divis)

rest=a%b #resto della divisione
print(rest)

divf=a//b #divide e arrotonda
print(divf)

pot=a**2 #elevato alla potenza
print(pot)

c=3
d=1
c+=2 #c=c+2
print(c)

c-=d
print(c)

conf=c==d
print(conf)
conf=c>d
print(conf)
conf=c<d
print(conf)
conf>=d
print(conf)

n1=4
n2=2

n3=(n1>0 and n2>0) 
print(n3)

n3=(n1>n3 or n2>8)
print(n3)

n3=(n1>0 and n2>0 )or (n1>3 or n2>8)
print(n3)

n3=not n1>0 
print(n3)

n4=-7
n4= abs(n4)
print(n4)

pi=3.1438489473943
pi=round(pi,2)
print(pi)

n5=4
pi=pow(n4,2) #potenza
print(n5)

m=max(4,7,9)
print(m)

m=min(4,4,7,9)
print(m)

st="6"
s1=int(st)+1
print(s1)

st="3.14"
s1=float(st)
print(s1)

s2=10
s1=str(s2)
print(s1)

s2=1
s1=bool("false")
print(s1)

s3=3.14
s3=int(s3)
print(s3)
