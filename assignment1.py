import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("hubble_correct.dat",dtype=float)
dist=data[:,0]
vel=data[:,1]
print(dist)#dist=xi
print(vel)#vel=yi

N=len(dist)


Sxy= np.sum(dist*vel)
Sx= np.sum(dist)
Sy=np.sum(vel)
Sx_sq=np.sum(dist**2)

delta=(N*Sx_sq-(Sx)**2)

a=(Sx_sq*Sy-Sx*Sxy)/delta
b=(N*Sxy-Sx*Sy)/delta
print("estimate of a=",a)
print("estimate of b=",b)

print("Value of H0=",b*(10**6))
time= 3.086/(3.154*(b*(10**6)))
t2=3.086 /(b*(10**6))
print(time)
print(t2)

func=a+b*dist

dist=dist*(10**(-6))
plt.plot(dist,func,color='red',label='Best fit regression line')
plt.scatter(dist,vel,color='blue',label='data points')
plt.xlabel('Distance in Mpc')
plt.ylabel('Recession Velocity in km/s')
plt.title("Hubble Original Velocity - Distance Graph")
plt.grid()
#plt.errorbar(dist,vel,sigma,label='errorbar')
plt.legend()
plt.show()


