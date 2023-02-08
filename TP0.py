import numpy as np
import matplotlib.pyplot as plt

### Graphes, mathplotlib.plt et numpy

#Tracer une puissance de x en fonction de x en utilisant des échelles logarithmiques devrait donnner une droite
x = np.linspace(0,1, 100) # (depart, arrivé, nombre de pas)
plt.figure()
plt.plot(x, np.sqrt(x))
plt.xscale("log")
plt.yscale("log")
#On observe bien une droite mais le coefficient n'est pas le bon (log de 10 ??)
plt.show()

#Dans cette partie on veut voir comment le choix de l'echelle peut posser problème
def f(x):
    return x**3 -x

plt.figure()

x = np.linspace(-10,10, 100)
plt.subplot(211) # (211) équivalent à (2,1,1)
plt.plot(x, f(x))

x = np.linspace(-1,1, 100) # On représente ensuite avec une échelle 10x plus petite et ducoup 10x plus précise
plt.subplot(212)
plt.plot(x, f(x))

plt.show() #On s'apercoit qu'il y avait deux extremum locaux aux voisinage de 0

#On fait la même exoérience pour sin(15x)

x = np.linspace(-10,10, 100)
plt.figure()
plt.subplot(211)
plt.plot(x, np.sin(15*x))

x = np.linspace(-1,1, 100)
plt.subplot(212)
plt.plot(x, np.sin(15*x))

plt.show() # Les deux graphes n'ont rien à voir

### Marches Aléatoires

# On initialise le "random number generator" avec la graine 12345 :
np.random.seed(12345)
for i in range(10):
    print(np.random.rand()) # un réel dans [0,1]
for i in range(10):
    print(np.random.random_integers(low=1, high=6))

N = 10
a = np.random.rand(size=N) # a contient N flottants aléatoires avec 0 <= a < 1,→
b = 3.0 * np.random.rand(size=N) + 6.5; # b contient N flottantsaléatoires avec 6.5 <= b < 9.5

moy = 0

for i in range(1000):
    r1, r2 = 0, 1
    if(r1 == r2): moy = moy + 1
    while(r1 != r2) : 
        r1 = np.random.randint(1,7)
        r2 = np.random.randint(1,7)
        moy = moy + 1
        #print("(",r1,",",r2,")")
print(moy/1000)


def pile_ou_face() : 
    return np.random.randint(2)*2 -1


#np.random.seed(12345)
NPAS = 100
marche = np.empty(NPAS) # un array numpy vide pour stocker la position en fonction du temps,→

marche[0] = 0 # position initiale
for i in range(1,NPAS):
    pas = pile_ou_face()
    marche[i] = marche[i-1] + pas # Calculez la somme cumulée
# Affichage des résultats
plt.plot(np.arange(NPAS),marche)
# TRES IMPORTANT ! Bien définir les axes de tout graphe
#plt.title("position finale : ",  marche[-1])
plt.xlabel("# pas")
plt.ylabel("position")

def pile_ou_face(N) : 
    return np.random.randint(2, size = NPAS)*2 -1

marche = np.cumsum(pile_ou_face(NPAS))
plt.plot(np.arange(NPAS),marche)
# TRES IMPORTANT ! Bien définir les axes de tout graphe
#plt.title("position finale : ",  marche[-1])
plt.xlabel("# pas")
plt.ylabel("position")

#np.random.seed(12345)
NPAS = 100
NMARCHES = 1000
arrivee = np.zeros(NMARCHES) # array numpy vide pour stocker les,→ NMARCHES positions d’arrivée
def marche2(pas):
    np.sum(pile_ou_face(pas))
for i in range(NMARCHES):
    arrivee[i] = marche2(NPAS)
print(arrivee)
print((np.mean(arrivee),np.std(arrivee)))