import math


p = 11
g = 7
x =  4
k = 7

y = pow(g,x) % 11
print ("======Pembangkitan Kunci======")
print("hasil y = ", y)
print ("hasil dari key public adalah", y, g, p)
print ("hasil dari key private adalah", x, p)


print("====Enkripsi====")
m = 9 #pesan di dalam range p-1
k = 7
a = pow(g, k) % 11
b = (pow(y, k) * m) % 11

print("====Cipher textnya adakah====")
print ("hasil dari a ", a)
print ("hasil dari b", b)
print ("hasil enkripsi adalah", a,b)

print("====Deskiripsi=====")
d =  pow(a, p-1-x) % p
print(d)

md = (b*d)%p


print(md)
