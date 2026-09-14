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

#Uppgift c;

