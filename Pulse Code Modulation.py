import matplotlib.pyplot as plt
import numpy as np

A = 1
fm = 10
fs = 80
n = 3
t = np.arange(0, 1, (1 / (100 * fm)))
x = A * np.cos(2 * np.pi * fm * t)
#---Sampling-----
ts = np.arange(0, 1, (1 / (fs)))
xs = A * np.cos(2 * np.pi * fm * ts)
#xs Sampled signal

#--Quantization---
x1 = xs + A
x1 = x1 / (2 * A)
L = (-1 + 2 ** n)# Levels
x1 = L * x1
xq = np.round(x1)
r = xq / L
r = 2 * A * r
r = r - A
#r quantized signal


#Calculations
MSE = np.sum((xs - r)** 2) / len(x)
Bitrate = n * fs
Stepsize = 2 * A / L
QNoise = ((Stepsize) ** 2) / 12

plt.figure(1)
plt.plot(t, x, label= 'Original Signal',linewidth = 2)
plt.title('Sampling')
plt.ylabel('Amplitute')
plt.xlabel('Time t(in sec)')

plt.stem(ts, xs, label='Sampled Signal', use_line_collection = True)
plt.show

plt.figure(2)
plt.stem(ts, x1,use_line_collection = True)
plt.title('Quantization')
plt.ylabel('Levels L')

plt.stem(ts, xq,label= 'Original Signal',use_line_collection = True)
plt.plot(ts, xq, color='r',linestyle ='-',label = 'Quantized Signal')
plt.plot(t, (x + A) * L / (2 * A), 'b--')
plt.grid()
plt.show()

#----Encoding---
for i in range(0,len(xq)):
    d = np.binary_repr(int(xq[i]),width = 3)
    print('Binary Code',i, d)


from math import log
#band limited freq in hertz
fm=1100

Rn=2*fm       # # Nyquist sampling rate
Ra=Rn*(4/3)     ## actual Nyquist sampling rate
# Here the maximum quantization error(E) is 0.5% of the peak amplitide mp. Hence, E=mp/L=0.5*mp/100*L
mp=1            ##we assume peak amplitude is unity
L=(mp*100)/(0.5*mp)#

for i in range(0,11):
    j=2**i
    if(j>=L):
        L1=j#
        break#
    
n=log(L1,2)## bits per sample
c=n*Ra## total no of bits transmitted
# Beause we can transmit up to 2bits/per hertz of bandwidth, we require minimum transmission bandwidth Bt=c/2
Bt=c/2#
print ("minimum transmission bandwidth = %.2f Hertz"%Bt)

#no of signal to be multiplexed
s=25
Cm=s*c ##total no of bits of 's' signal

c1=Cm/2 ## minimum transmission bandwidth
print ("minimum transmission bandwidth = %.2f Hertz"%c1)


from math import log,log10
L=12
#the bandwidth of signal in hertz 
B=350
n=log(L,2)#
Bt=n*B#
u=100##given
a=10*log10(3/(log(1+u))**2)
SNR=(a+(6*n))#
print ("SNR ratio is = %0.2f "%SNR)
# Here the SNR ratio for the two cases are found out. 
#The difference between the two SNRs is 12dB which is the ratio of 16. 
#Thus the SNR for L=256 is 16 times the SNR for L=64. The former requires just about 33% more bandwidth compared to the later.


import math
#given
f_m = 4.*10**3#maximum frequency or bans
x_max = 3.8#maximun input signal
P = 30.*10**-3#average power of signal
SbyN_dB= 20.#signal to noise ratio in db

#calculations
SbyN = math.exp((SbyN_dB/10)*math.log(10));
v = round((math.log10((SbyN*(x_max)**2)/(3*P))/math.log10(2.)/2.));#number of bits required per sample
BW = 30*v*f_m#transmission channel bandwidth which is greater than or equal to obtained value
r=BW*2

#result
print ("i.Number of bits required (bits) = ",round(v,2))
print ("ii.Bandwidth required for 30 PCM coders (kHz) = ",round(BW/1000.,0))
print ("iii.Signalling rate (bitspersecond) = ",round(r/1000.,0))




