import numpy as np 
import matplotlib.pyplot as plt 
"""
#Uppgift a; 
f = lambda x: x**3 * np.exp(x)
igranser = [0, 2]
n = 100

def trapets(f, n, igranser):
    a, b = igranser
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    fx = f(x)

    Th = h*(fx[0]/2 + np.sum(fx[1:-1]) + fx[-1]/2)
    print("Th=", Th)
    return Th

I_trapets = trapets(f, n, igranser)
I_exakt = 6 + 2 *np.exp(2)

print("Beräknat värde:", I_trapets)
print("Exakt värde:", I_exakt)

#Från utskriften ser vi att det beräknadet värdet skiljer sig något från det exakta värdet men att det fortfarande är tillräckligt nära för att vi ska kunna verifiera att funktionen fungerar.
#Beräknat värde: 20.7830380953846
#Exakt värde: 20.7781121978613 
"""

"""
#uppgfift b;
f = lambda x: x**3 * np.exp(x)
igranser = [0, 2]
n = 1

def trapets(f, n, igranser):
    a, b = igranser
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    fx = f(x)

    Th = h*(fx[0]/2 + np.sum(fx[1:-1]) + fx[-1]/2)
    return Th

forra_fel = 0

while 512 >= n:
    I_trapets = trapets(f, n, igranser)
    I_exakt = 6 + 2 *np.exp(2)
    fel = abs(I_trapets - I_exakt)
    print("n:", n)
    print("fel:", fel)
    print("kvot:", forra_fel/fel)
    print(" ")
    forra_fel = fel
    n = n * 2

#vi ser att när n fördubblas så divideras ungefär felet med 4. vilket följer att approxamationsfelet är Ch^2 eller med andre ord att e[h]/e[h/2] = 4.
"""

"""
#Uppgift c;

ft = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
h = 1
Th = h*(ft[0]/2 + np.sum(ft[1:-1]) + ft[-1]/2)
print("Skattad total energi:", Th)

#Vi får då utskriften: Skattad total energi: 277.55.
"""

#Uppgift d; 
ft = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])

def trapets(ft, h):
   index = np.arange(0, len(ft), h)
   y = ft[index]
   Th = h*(y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)
   return Th

Th1 = trapets(ft, 1)
Th2 = trapets(ft, 2)
Th4 = trapets(ft, 4)
Th8 = trapets(ft, 8)

e1h = np.abs(Th1 - Th2)
e2h = np.abs(Th2 - Th4)
e4h = np.abs(Th4 - Th8)

print("Th1 = ", Th1)
print("Th2 = ", Th2)
print("Th4 = ", Th4)
print("Th8 = ", Th8)

print("e1h = ", e1h)
print("e2h = ", e2h)
print("e4h = ", e4h)
print("Felkvot 1 = ", e2h/e1h)
print("Felkvot 2 = ", e4h/e2h)

#Vi får urskriften:
#Felkvot 1 =  3.934246575342417
#Felkvot 2 =  3.8077994428969477

#Felkvoten ligger alltså även i detta fall runt 4, vilket följer approxamationsfelet Ch^2 e[2h]/e[h] = 4.
