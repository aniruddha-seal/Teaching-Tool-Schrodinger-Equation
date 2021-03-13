import Support_Func_QDP as EF#importing the file containing all the functions
import numpy as np
import matplotlib.pyplot as plt
import time as T

def Poten_H(x):
	'''
	The potential function for simple harmonic Oscilation
	Takes either a point or an array
	returns the potential energy for the point/array
	'''
	V=m*(w*x)**2/2
	return V
h,m,w=1,1,1#we take all the constants as one for simplicity
EF.Constant_feeder(h,m,1,Poten_H)
X=np.linspace(-8,8,10**4)
T_0=T.time()
E_eigen=EF.Eigen_Range_finder(X,0,5,2)
T_end=T.time()
print(f"\nTime Taken={T_end-T_0}")
fig=plt.figure()
ax=plt.axes(xlabel='X',ylabel='Psi',ylim=(0,E_eigen[-1]*1.1))
ax.set_title("Solutions of quantum harmonic oscilator")
EF.Plot_Eq(X,E_eigen,ax)
ax.plot(X,Poten_H(X))
plt.show()
