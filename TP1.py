### TP1 

import numpy as np
import matplotlib.pyplot as plt

#Méthode d'Euler

def euler( f, a, b, N, y0):
    t = a
    h = (b-a)/N
    y = np.zeros(N)
    y[0] = y0
    i = 0
    while(i< N-1):
        y[i+1] = y[i] + h*f(t, y[i])
        t = t + h
        i = i +1
    return y #retourne un tableau des N valeurs prise par y avec un pas h

#Solution analytque :
x = np.linspace(0, -1 , 1000)
yanalytique  = np.exp(-x)

#Solution numérique
def f1(t, x, k = 1): return -k*x

T = np.linspace(0, 1 , 1000)
Xeuler = euler(f1, 0, 1, 1000, 1)
Xanalytique  = np.exp(-T)

#Tracer la solution analytique et la solution numérique
plt.figure()
plt.plot(T, Xeuler, label = "Solution numérique")
plt.plot(T, Xanalytique, label = "Solution analytique", color = 'r')
plt.xlabel("t : temps")
plt.ylabel("x : Densité de l'élément radioactif")
plt.legend()
#plt.savefig('Figure 1')
plt.show()


#Tracer l'erreur de la méthode d'Euler

plt.figure()
plt.plot(T, np.abs(Xeuler - Xanalytique), label = "|Solution analytique - Solution numérique|")
plt.xlabel("t : temps")
plt.ylabel("E : Erreur de la solution analytique")
plt.legend()
#plt.savefig('Figure 2')
plt.show()


plt.figure() # Ici on retrace l'erreur mais en echelle logarithmique
plt.plot(np.log(T),np.log(abs(Xeuler - Xanalytique)), label = "|Solution analytique - Solution numérique|")
plt.xlabel("ln(t) : temps en echelle logaritmique")
plt.ylabel("E : Erreur de la solution analytique en echelle logaritmique")
plt.legend()
#plt.savefig('Figure 3')
plt.show()

def f2(y, t, k2 = 0.1, k = 1): return k*y - k2*Xeuler[int(t/1000)]
Yeuler = euler(f2, 0, 1, 1000, 0) 

plt.figure()
plt.plot(T, Yeuler, label = "Solution numérique de Y")
plt.xlabel("t : temps")
plt.ylabel("Y : Densité de l'élément radioactif")
plt.legend()
#plt.savefig('Figure 4')
plt.show()


w0 = 20
t = 0
h = 1/1000
v = np.zeros(1000)
x = np.zeros(1000)
x[0] = 0
v[0] = 1
i = 0
while(i< 1000 -1):
    v[i+ 1 ] = v[i] - h*w0**2*x[i]
    x[i+1] = x[i] + h*v[i]
    t = t + h
    i = i +1

plt.figure()
plt.plot(T, x, label = "Solution numérique de l'oscillateur harmonique")
plt.xlabel("t : temps")
plt.ylabel("x : Position (w0 = 20")
plt.legend()
#plt.savefig('Figure 4')
plt.show()


import rk4

def deriv(t,y,omega = 3, q =5):
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = y[2]
    dy[2] = -omega**2 * y[0] - q*y[1]
    return dy

a = 0
b = np.pi
N = 1000
h = (b-a)/N
res = np.zeros((N,3))
res[0] = (np.pi*(10/180),0,0)
omega = 3 
q = 5
print(res[0])
for i in range(N-1) : 
    res[i+1] = rk4(a + i*h, h, res[i], deriv)