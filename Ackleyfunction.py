import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from scipy.optimize import minimize

def Ackely(x,y):
    term1 =  -20 * np.exp(-0.2*np.sqrt(0.5*(x**2 + y**2)))
    term2 = -np.exp(0.5*(np.cos(2.*np.pi*x)+np.cos(2*np.pi*y)))
    return term1 + term2

fig = plt.figure(figsize=(12,8))
x= np.linspace(-5,5,100)
y= np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)
Z= Ackely(X,Y)

ax= fig.add_subplot(111, projection='3d')
surf= ax.plot_surface(X,Y,Z,cmap='magma', alpha=0.9)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title('Ackley Function')
ax.view_init(elev=30, azim =40)
fig.colorbar(surface, shrink=0.5, label='f(x,y)')
plt.show
