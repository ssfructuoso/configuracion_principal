from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np
import math

PI=np.pi
orden_taylor=2  #Valor de n en la suma de Taylor del seno y del coseno
x=np.linspace(0,PI/2, num=1000) #Numero de puntos (equiespaciado) a representar graficamente




################################################
##### Coseno

def cos_confPrincipal(x):
    return 2*(PI-2*x)/(3*PI - np.sqrt(PI ** 2 + 8*PI*x -8*x**2))


def cos_taylor(x, n):
    value=0
    for k in range(0,n+1):
        value += (-1)**k * x**(2*k) / math.factorial(2*k)
    return value

####

plt.figure('Cos(x)')

plt.subplot(2,2,1)
plt.plot(x, np.cos(x), label='cos(x) Numpy')
plt.title("Cos(x)")

plt.plot(x, cos_confPrincipal(x), label='cos(x) ConfPrincipal')

plt.plot(x, cos_taylor(x, orden_taylor), label='cos(x) Taylor orden '+str(orden_taylor))

plt.legend()

##Calculo errores 

plt.subplot(2,2,2)
plt.plot(x, np.abs(np.cos(x)-cos_confPrincipal(x)), label='ConfPrincipal')
plt.plot(x, np.abs(np.cos(x)-cos_taylor(x,orden_taylor)), label='Taylor orden '+str(orden_taylor))

plt.title("Error absoluto")
plt.legend()

plt.title("Error absoluto (porcetaje)")
plt.legend()


plt.subplot(2,2,4)
plt.plot(np.log10(x), np.log10(np.abs(np.cos(x)-cos_confPrincipal(x))), label='ConfPrincipal')
plt.plot(np.log10(x), np.log10(np.abs(np.cos(x)-cos_taylor(x,orden_taylor))), label='Taylor orden ')

plt.title("log(Error absoluto)")




################################################
################################################
##### Seno

def sen_confPrincipal(x):
    return -np.sqrt(3)*(1 - 2/(3-np.sqrt(3*(1-8*(x-PI/2)**2/(3*PI**2)))))


def sen_taylor(x, n):
    value=0
    for k in range(0,n+1):
        value += (-1)**k * x**(1+2*k) / math.factorial(1+2*k)
    return value

####

plt.figure('Sen(x)')

plt.subplot(2,2,1)
plt.plot(x, np.sin(x), label='sen(x) Numpy')
plt.title("Sen(x)")

plt.plot(x, sen_confPrincipal(x), label='Sen(x) ConfPrincipal')

plt.plot(x, sen_taylor(x, orden_taylor), label='sen(x) Taylor orden '+str(orden_taylor))

plt.legend()

##Calculo errores 

plt.subplot(2,2,2)
plt.plot(x, np.abs(np.sin(x)-sen_confPrincipal(x)), label='ConfPrincipal')
plt.plot(x, np.abs(np.sin(x)-sen_taylor(x,orden_taylor)), label='Taylor orden '+str(orden_taylor))

plt.title("Error absoluto")
plt.legend()

plt.subplot(2,2,4)
plt.plot(np.log10(x), np.log10(np.abs(np.sin(x)-sen_confPrincipal(x))), label='ConfPrincipal')
plt.plot(np.log10(x), np.log10(np.abs(np.sin(x)-sen_taylor(x,orden_taylor))), label='Taylor orden ')

plt.title("log(Error absoluto)")



plt.show() #Se muestran por pantalla las graficas