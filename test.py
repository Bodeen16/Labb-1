import numpy as np
import matplotlib.pyplot as plt 

y = np.loadtxt('KPI.csv', delimiter=',', skiprows=3, usecols=1)
t = np.arange(y.size) / 12

plt.plot(t+1980, y)
plt.show()

I = (t+1980 >= 1991) & (t+1980 < 2021)
t = t[I]
y = y[I]

#Uppgift a; 
N = len(t)

A = np.column_stack((t**0, t))

ATA = A.T @ A
ATY = A.T @ y

c = np.linalg.solve(ATA, ATY)
c0 = c[0]
c1 = c[1]

f = c0 + c1*t

r = f - y

ERMS = np.sqrt(np.sum(r**2)/N)

print("c0 =", c0)
print("c1 =", c1)
print("RMS-felet =", ERMS)

plt.plot(t, y)
plt.plot(t, f)
plt.grid()
plt.show()

plt.plot(t, r)
plt.grid()
plt.show()