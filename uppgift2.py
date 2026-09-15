import numpy as np
import matplotlib.pyplot as plt 

y = np.loadtxt('KPI.csv', delimiter=',', skiprows=3, usecols=1)
t = np.arange(y.size) / 12

plt.plot(t+1980, y)
plt.show()

I = (t+1980 >= 1991) & (t+1980 < 2021)
t = t[I]
y = y[I]

"""
#Uppgift a; 
N = len(t)

A = np.column_stack((t**0, t))

ATA = A.T @ A
ATY = A.T @ y

c = np.linalg.solve(ATA, ATY)
c0 = c[0]
c1 = c[1]

f = lambda t: c0 + c1*t

r = f(t) - y

ERMS = np.sqrt(np.sum(r**2)/N)

print("c0 =", c0)
print("c1 =", c1)
print("RMS-felet =", ERMS)

plt.plot(t + 1980, y)
plt.plot(t + 1980, f(t))
plt.grid()
plt.show()

plt.plot(t + 1980, r)
plt.grid()
plt.show()
"""

"""
#Uppgift b; 
N = len(t)

A = np.column_stack((t**0, t, np.sin((2*np.pi*t)/8), np.cos((2*np.pi*t)/8)))

ATA = A.T @ A
ATY = A.T @ y

d = np.linalg.solve(ATA, ATY)
d0 = d[0]
d1 = d[1]
d2 = d[2]
d3 = d[3]

f = lambda t: d0 + d1*t + d2*np.sin((2*np.pi*t)/8) + d3*np.cos((2*np.pi*t)/8)

r = f(t) - y

ERMS = np.sqrt(np.sum(r**2)/N)

print("d0 =", d0)
print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)
print("RMS-felet =", ERMS)

plt.plot(t + 1980, y)
plt.plot(t + 1980, f(t))
plt.grid()
plt.show()

plt.plot(t + 1980, r)
plt.grid()
plt.show()
"""

"""
#Uppgift c;
N = len(t)

c = np.array([194.56324931826524, 3.4878236585092433, -1.095820432393067, 3.480988627461247, 8.0], dtype=float)

tol = 1e-10
diff = 1
it = 0
maxiter = 300

while diff > tol and maxiter > it:
    d0 = c[0]
    d1 = c[1]
    d2 = c[2]
    d3 = c[3]
    L = c[4]

    f = lambda t, L: d0 + d1*t + d2*np.sin((2*np.pi*t)/L) + d3*np.cos((2*np.pi*t)/L)

    F = f(t, L) - y 

    J = np.column_stack((
        t**0,
        t,
        np.sin((2*np.pi*t)/L),
        np.cos((2*np.pi*t)/L),
        -(2*np.pi*t*d2/L**2)*np.cos((2*np.pi*t)/L) + (2*np.pi*t*d3/L**2)*np.sin((2*np.pi*t)/L)
    ))

    JTJ = J.T @ J 
    JTF = J.T @ F

    delta = np.linalg.solve(JTJ, -JTF)

    c = c + delta

    diff = np.max(np.abs(delta))
    it += 1

d0 = c[0]
d1 = c[1]
d2 = c[2]
d3 = c[3]
L = c[4] 

f = lambda t, L: d0 + d1*t + d2*np.sin((2*np.pi*t)/L) + d3*np.cos((2*np.pi*t)/L)

r = f(t, L) - y

ERMS = np.sqrt(np.sum(r**2)/N)

print("d0 =", d0)
print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)
print("L =", L)
print("RMS-felet =", ERMS)

plt.plot(t + 1980, y)
plt.plot(t + 1980, f(t, L))
plt.grid()
plt.show()

plt.plot(t + 1980, r)
plt.grid()
plt.show()
"""

#Uppgift d; 

#Vid körning av de tre programmen a-c får vi följande RMS-fel:
#Uppgift a: RMS-felet = 4.130967604665237
#Uppgift b: RMS-felet = 3.2131915718048005
#Uppgift c: RMS-felet = 3.198098527008681
#Vi kan alltså konstatera att modell c gav oss det lägsta RMS-felet. 
#Modell c verkar bäst eftersom den modellen har lägst RMS-fel, dvs. bäst överensstämmelse. 

#Från modellerna a-c avläser vi följande värden: 
#c1 = 3.533607064869332 - modell a
#d1 = 3.4878236585092433 - modell b
#d1 = 3.495259861428787 - modell c

#Vi ser därmed att KPI ungefär ökade med 3.53, 3.49 respektive 3.50 KPI-enheter per år. 