import numpy as np 
import matplotlib.pyplot as plt 

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
