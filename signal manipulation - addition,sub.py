
#Vyom_Paney_20102108
#problem 1
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,1,0.01)
x1=np.cos(6*(np.pi)*t)
plt.figure(figsize=(8,2))
plt.plot(t,x1, label = 'cos(6*pi*t)');plt.ylabel('x1(t)=cos(6*pi*t)')
plt.legend();plt.show()

#Question2
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,3,0.01)
x2=3*(np.cos(3*(np.pi)*t+(np.pi)/3));
plt.figure(figsize=(8,2))
plt.plot(t,x2);
plt.title('cosine curve')
plt.show()

#Question3
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-2,6,0.01)
x3=3*np.exp(0.4*t);
x4=2*np.exp(-0.9*t);
plt.figure(figsize=(8,2))
plt.plot(t,x3);
plt.plot(t,x4);
plt.title('exponential curve')
plt.show()

#Question4
import matplotlib.pyplot as plt
import numpy as np
n=np.arange(-12,13)
g=5*(n<=0)+(5-3*n)*((4>=n)*(n>0))+(-23 + pow(n,2))*((8>=n)*(n>4))+41*(n>8)
plt.figure(figsize=(8,2))
plt.stem(n,g, use_line_collection=True)
plt.xlabel('n');
plt.ylabel('g[n]')
plt.show()

#Question5
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,2,0.01)
x1=np.cos(6*(np.pi)*t);
x2=3*(np.cos(3*(np.pi)*t+(np.pi)/3));
x5=x1+x2
plt.figure(figsize=(9,3))
plt.plot(t,x5);
plt.title('addition of signals')
plt.show()

#Question 6
import matplotlib.pyplot as plt
import numpy as np
def x3(t):
  return 3*np.exp(0.4*t)
t=np.arange(-1,2,0.01)
plt.plot(t,x3(t))
x3_even=-0.5*(x3(t)+x3(-t));
x3_odd=0.5*(x3(t)-x3(-t))
plt.plot(t,x3_even, label='Even signal of x3(t)');
plt.plot(t,x3_odd, label='Odd signal of x3(t)');
plt.plot(t,x3_even+x3_odd, label='reconstructed signal of x3(t)');
plt.show()

#Question7
#x(-t)
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,1,0.1)
x=t*np.exp(-t)
plt.subplot(211);plt.plot(t,x)
plt.title('exponential curve')
plt.show()

#x(t/5)
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,1,0.1)
x=t*np.exp(-t)
plt.subplot(211);plt.plot(5*t,x)
plt.title('exponential curve')
plt.show()

#x(5t)
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,3,0.1)
x=t*np.exp(-t)
plt.subplot(211);plt.plot(t/5,x)
plt.title('exponential curve')
plt.show()

#x(t-3)
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,3,0.1)
x=t*np.exp(-t)
plt.subplot(211);plt.plot(t+3,x)
plt.title('exponential curve')
plt.show()

#x(1-2t)
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,3,0.1)
x=t*np.exp(-t)
plt.subplot(211);plt.plot(0.5*(-t)+0.5,x)
plt.title('exponential curve')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,7,.01)
v = 20*np.exp(-2*t)*(t<=2) + (-10)*(t==2) + (10*(t-3))*((t>2)*(t<=3)) + 20*(t==3)
plt.figure()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('In Lab Exercise')
plt.plot(t,v)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,7,.01)
v = 20*np.exp(-2*t)*(t<=2) + (-10)*(t==2) + (10*(t-3))*((t>2)*(t<=3)) + 20*(t==3) + (-10*(
t=-1*t;
plt.figure()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('In Lab Exercise')
plt.plot(t,v)
plt.show()
