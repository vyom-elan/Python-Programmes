

#Vyom_Pandey_20102108_A4
#problem 1
import matplotlib.pyplot as plt
import numpy as np
x1=([1.0, 2.0, 3.0])
x2=([0.0, 1.0, 0.5,1.0])
convolution = np.convolve(x1,x2) #performs convolution
plt.stem(convolution, use_line_collection = True) #to plot discrete signal
plt.xlabel('n')
plt.ylabel('x1[n]*x2[n]')
plt.title('DT Convolution')
plt.show()

#problem 2
import matplotlib.pyplot as plt
import numpy as np
x1=([-1.0, 2.0, -3.0])
x2=([0.0, -1.0, 0.5, 1.0])
convolution =np.convolve(x1,x2 )
l1 = np.size(x1)
l2 = np.size(x2)
n=np.arange(0,l1+l2-1,1)
plt.stem(n,convolution, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x1[n]*x2[n]')
plt.title('DT Convolution')
plt.show()

#problem 3
import matplotlib.pyplot as plt
import numpy as np
x1=([-1.0, 2.0, -3.0])
x2=([0.0, -1.0, 0.5, 1.0])
n1=([-1,0,1])
n2=([-2,-1,0,1])
convolution =np.convolve(x1,x2 ) #to perfrom convolution
l1 = np.size(x1) #to retrieve the size of array x1
l2 = np.size(x2) #to retrieve the size of array x2
lconvolve=l1+l2-1
print('length of convolved signal',lconvolve)
n=np.arange(n1[0]+n2[0],n1[-1]+n2[-1]+1,1)
print('n=',n)
plt.stem(n,convolution, use_line_collection = True) #to plot discrete time signal
plt.xlabel('n')
plt.ylabel('x1[n]*x2[n]')
plt.title('DT Convolution')
plt.show()

#unsolved problem 4
import matplotlib.pyplot as plt
import numpy as np
x1=([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
x2=([1.0, 0.0, 0.0,0.0])
convolution = np.convolve(x1,x2) #to perform convolution
plt.stem(convolution, use_line_collection = True) #to plot discrete time signal
plt.xlabel('n')
plt.ylabel('x1[n]*x2[n]')
plt.title('DT Convolution')
plt.show()

#postlab exercise
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(-5, 5, 11) #to return evenly spaced numbers over the given interval
u = 1*(n>=0)
k = 1*(n>=3)
m = 1*(n>=2)
a = u-k
b = u-m
convolution = np.convolve(a,b) #to perform convolution
plt.stem(convolution, use_line_collection = True) #to plot discrete time signal
plt.show()
