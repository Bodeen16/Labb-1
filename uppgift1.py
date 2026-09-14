import numpy as np
import matplotlib.pyplot as plt 

"""
#Uppgift a;

L = 1 

x = np.linspace(0, L, 200)

y = (8/3)*x - 3*x**2 + (1/3)*x**3 - (2/3)*np.sin(np.pi*x)

plt.plot(x,y)
plt.grid()
plt.show()

# 2 nollställen 
"""

"""
#Uppgift b; 

L = 1 

x = np.linspace(0, L, 200)

dg = (3/8)*(6*x - x**2 + (2*np.pi/3)*np.cos(np.pi*x))

plt.plot(x, dg)
plt.grid()
plt.show()

# Vi ser i plotten att ungefär 0.124<x<0.552 x>0.928 är derivatan > 1. Från uppgift a ser vi att första nollstället är vid ungefär x = 0.30 inte går och andra nollstället x = 0.84 går.
"""

"""
#Uppgift c;

g = lambda x: (3/8)*(3*x**2 - (1/3)*x**3+(2/3)*np.sin(np.pi*x))

x0 = 0.80
it = 0
maxiter = 300
diff = 1 
tol = 1e-10
x = x0

while diff > tol and it < maxiter: 
    xnew = g(x)
    diff = np.abs(xnew-x)
    it += 1
    x = xnew 
    print(it, x, diff)

    # Vi ser att det konvergar mot x = 0.84 med fixpunktsmetoden.
"""

"""
#Uppgift d;
F = lambda x: (8/3)*x - 3*x**2 + (1/3)*x**3 - (2/3)*np.sin(np.pi*x) 

dF = lambda x: (8/3) - 6*x + x**2 - (2*np.pi/3)*np.cos(np.pi*x)

X = 0.30
tol = 1e-10
it = 0
diff = 1 
maxiter = 300

while diff > tol and it < maxiter:
    newx = X - (F(X)/dF(X))
    diff = np.abs(newx - X)
    X = newx
    it += 1
    print(it, X, diff)
""" 

"""
#Uppgift e; 
g = lambda x: (3/8)*(3*x**2 - (1/3)*x**3 + (2/3)*np.sin(np.pi*x))

x0 = 0.80
it = 0
maxiter = 300
diff = 1 
it_fix = []
diff_fix = []
tol = 1e-10
x = x0

while diff > tol and it < maxiter: 
    xnew = g(x)
    diff = np.abs(xnew-x)
    diff_fix.append(diff)
    it_fix.append(it)
    it += 1
    x = xnew 
    print(it, x, diff)

F = lambda x: (8/3)*x - 3*x**2 + (1/3)*x**3 - (2/3)*np.sin(np.pi*x)

dF = lambda x: (8/3) - 6*x + x**2 - (2*np.pi/3)*np.cos(np.pi*x)

X = 0.30
tol = 1e-10
it = 0
diff = 1
it_newton = []
diff_newton = []
maxiter = 300

while diff > tol and it < maxiter: 
    newx = X - (F(X)/dF(X))
    diff = np.abs(newx - X)
    diff_newton.append(diff)
    X = newx
    it_newton.append(it)
    it += 1
    print(it, X, diff)

plt.semilogy(it_fix, diff_fix)
plt.semilogy(it_newton, diff_newton)
plt.grid()
plt.show()

# Vi ser utifrån plotten att Newtons metod konvergerar betydligt snabbare än fixpunktsmetoden. Detta stämmer bra överens med teorin då fixpunktsmetoden konvergerar enligt en+1 = Cen och newtons metod enligt en+1 Cen^2 

"""
