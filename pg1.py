# -*- coding utf-8 -*-

w =open("arquivo.txt", "w")
w.wrire("Esse é meu arquivo")
w.close()

arquivo = open("texto_teste.txt")
texto_completo = arquivo.read()

print(texto_completo)

#funçoes
def soma (x, y):
    return x+y
def multip (x, y):
    return x*y
def sub (x, y):
    return x-y
def div (x, y):
    return x/y
s = soma(2, 3)
m = multip(2, 3)
su= sub(10, 3)
d = div(9, 3)
print (s,m,su,d)

#estrutura de decisão 
if s > m :
   print("Soma é maior que multiplicação")
elif s == m :
   print("Valores iguais")
else :
   print("Multiplicação é maior")
rep = 5

#estrutura de repetição while
while rep > 0:
    rep += 1
    if rep == 10:
        break
print(rep)

#string pt1 pt2
var1 = "ola"
var2 = " "
var3 = "mundo"
ms = "O rato roeu a roupa do rei de roma"
ml = ms.split("r")
busca = ms.find("roma")
busca2 = ms.replace("roma","roupa")
var4 = var1+var2+var3
tamanho = len(var4)
print(var4)
print(var4[2])
print(var4[2:6])
print(tamanho)
print(var4.lower())
print(var4.upper())
print(ml)
print(busca)
print(busca2)