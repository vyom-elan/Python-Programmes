#20102108_Vyom_Pandey_A4
#Problem1
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft  #importing fft function from scipy
x1=([0,4,2,0])
dft=scipy.fft.fft(x1)#DFT computation of x1
plt.subplot(2, 1, 1)
plt.stem(dft.real, use_line_collection = True)#to plot real part of dft
plt.xlabel('k')
plt.ylabel('Real{x[k]}')
plt.title('Real part of DFT')
plt.show()
plt.subplot(2, 1, 2)
plt.stem(dft.imag, use_line_collection = True)#to plot imaginary part of dft
plt.xlabel('k')
plt.ylabel('Img{X{k}}')
plt.title('Imaginary Part of DFT')
plt.show()
print('DFT X[k] =',dft)

#Problem2
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft
Xk=[6,-2-4j,-2,-2+4j]
idft=scipy.fft.ifft(Xk) #to plot IDFT
plt.subplot(2, 1, 1)
plt.stem(idft.real, use_line_collection = True)#plots the real part of idft
plt.xlabel('n')
plt.ylabel('Real{x[n]}')
plt.title('Real part of IDFT')
plt.show()
plt.subplot(2, 1, 2)
plt.stem(idft.imag, use_line_collection = True)#to plot imaginary part of idft
plt.xlabel('n')
plt.ylabel('Img{x[n]}')
plt.title('Imaginary Part of IDFT')
plt.show()

#Problem3
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import numpy as np
N=32
t = np.arange(N)
x=np.sin(t)
sp = fftshift(fft(x))#finding dft
freq = fftshift(fftfreq(N))#Creating sample frequenices
plt.figure(figsize=(4,8))
plt.subplot(211)
plt.grid()
plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('sin(t)')
plt.subplot(212) #plotting DFT
plt.grid() 
plt.plot(freq, abs(sp)) # Real Part 
plt.xlabel('k') 
plt.ylabel('Magnitude Spectrum {|X[k]|}') 
plt.show()

#POST LAB
#QUESTION 1
import matplotlib.pyplot as plt 
import numpy as np 
import scipy.fft 
from scipy.fft import fft, fftfreq, fftshift 
Xk = [2,3+2j,0,-1*(-3+2j)] 
idft=scipy.fft.ifft(Xk)
plt.subplot(2, 1, 1) 
plt.stem(idft.real, use_line_collection = True) #plotting real part
plt.xlabel('n') 
plt.ylabel('Real{x[n]}') 
plt.title('Real part of IDFT') 
plt.show()
plt.subplot(2, 1, 2) 
plt.stem(idft.imag, use_line_collection = True) # plotting imaginary part
plt.xlabel('n') 
plt.ylabel('Img{x[n]}') 
plt.title('Imaginary Part of IDFT') 
plt.show() 
print('IDFT x[n] =',idft)

#POST LAB
#Question 2
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft 
n=np.linspace(-5,5,11)
#assigning values to delta function
del1=1*(n==(0))
del2=1*(n==(2))
del3=1*(n==(6))
X = del1 + (2*del2) + (3*del3)
dft=scipy.fft.fft(X)#Computing DFT
plt.figure(figsize=(7,7))
plt.subplot(211)
plt.stem(dft.real,use_line_collection=True) #plotting real
plt.xlabel('n --->')
plt.ylabel('X[n] --->')
plt.title('X[n] DFT(real)')
plt.figure(figsize=(7,7))
plt.subplot(212)
plt.stem(dft.imag,use_line_collection=True)#plotting imaginary
plt.xlabel('n --->')
plt.ylabel('X[n] --->')
plt.title('X[n] DFT(imag)')
plt.show()
print('X[n] DFT is: ',dft)

#Unsolved Problem
#Question 1
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
n=np.linspace(-5,5,11)
u=1*(n>=0)
u_3=1*(n>=3)
X = u - u_3
dft=scipy.fft.fft(X) #DFT computation
plt.figure(figsize=(5,5))
plt.subplot(211)
plt.stem(dft.real, use_line_collection=True)#plotting real
plt.xlabel('n--->')
plt.ylabel('X[n]--->')
plt.title('X[n] DFT(Real)')
plt.figure(figsize=(5,5))
plt.subplot(212)
plt.stem(dft.imag, use_line_collection=True)#plotting imaginary
plt.xlabel('n--->')
plt.ylabel('X[n]')
plt.title('X[n] DFT(Imaginary)')
plt.show()
print('X[n]= ',dft)

#Unsolved ProblemS
#Question 2
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
n=np.linspace(-10,10,21)
u1=1*(n>=0)
u2=1*(n>=2)
u3=1*(n>=3)
X = (2*u1) - (4*u2) + (2*u3)
dft = scipy.fft.fft(X)
plt.figure(figsize=(7,7))
plt.subplot(211)
plt.stem(dft.real,use_line_collection=True)#plotting real
plt.xlabel('n--->')
plt.ylabel('X[n]')
plt.title('X[n] DFT(real)')
plt.figure(figsize=(7,7))
plt.subplot(212)
plt.stem(dft.imag,use_line_collection=True)#plotting imaginary
plt.xlabel('n--->')
plt.ylabel('X[n]')
plt.title('X[n] DFT(imag)')
plt.show()
print('X[n] = ',dft)
