import numpy as np 

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
print("Skillnad: ", np.abs(I_trapets - I_exakt))

#Från utskriften ser vi att det beräknadet värdet skiljer sig något från det exakta värdet men att det fortfarande är tillräckligt nära för att vi ska kunna verifiera att funktionen fungerar.
#Beräknat värde: 20.7830380953846
#Exakt värde: 20.7781121978613 
#Skillnad: 0.004925897523300193
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

"""
#Uppgift d; 
ft = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
h = 1
Th=1
eh =1
while h < 9:
    fta = []
    i = 0
    while i < 9:
        fta.append(ft[i])
        i = i+h
    Thg = Th
    Th = h*(fta[0]/2 + np.sum(fta[1:-1]) + fta[-1]/2)
    ehg=eh
    eh = np.abs(Thg-Th)

    if h>= 4: #Sorterar så att vi endast får riktiga felvärden från for loopen. 
        Nog = np.log2(eh/ehg)
        print("Noggrannhetsordning: ", Nog)

    h = h*2
#Vi får utskriften: 
#1.976087380055654
#1.9289574937830132

#Vi ser att noggranhetsordning stämmer hyfsat med vad den ska vara för trapetsregeln i teorin där p = 2.
"""

"""
#Uppgift e; 
ft = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
h = 1
Th_lista = []
Sh = (h/3) * (ft[0] + 4*np.sum(ft[1:-1:2]) + 2*np.sum(ft[2:-1:2]) + ft[-1])

while h <= 2:
    fta = []
    i = 0 
    while i < 9:
        fta.append(ft[i])
        i = i+h 
  
    Th = h*(fta[0]/2 + np.sum(fta[1:-1]) + fta[-1]/2)
    Th_lista.append(Th)
    h = h *2

T1h = Th_lista[0]
T2h = Th_lista[1]

R = T1h - (T2h - T1h)/3

print("Richardsonextrapolation =", R)
print("Simposons regel,", Sh)

# Vi får du utskriften: 
#Richardsonextrapolation = 276.3333333333333
#Simposons regel, 276.3333333333333
#Ser att Richardsonextrapolation och Simpsons regel ger samma värde vilket stämmer överens med teorin Rh/2 = Sh/2
"""

#Uppgift f;
t = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
ft = np.array([12.00, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])

A = np.column_stack((t**0, t**1 - 2014))
c = np.linalg.lstsq(A, np.log(ft))[0]


atilde = c[0]
b = c[1]
a = np.exp(atilde)
print("a =", a)
print("b =", b)

#Vi får utskriften: 
#a = 11.998951209795411
#b = 0.23001165529172854



