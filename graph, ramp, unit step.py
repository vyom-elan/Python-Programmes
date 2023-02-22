Experiment - 2


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,1,3,5]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Plot 2.2')
plt.show()

import matplotlib.pyplot as plt
x1 = [1,2,3,4,5]
y1 = [2,4,1,3,5]
plt.plot(x1, y1, label = "line 1")
x2 = [1,2,3,4,5]
y2 = [4,1,3,2,5]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two lines on same plot')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
names = ['group_a','group_b','group_c']
values = [1,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('categorical plotting')
plt.show()

import matplotlib.pyplot as plt 
import numpy as np
plt.plot([1,2,3,4,5,6])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
x = np.linspace(-10,10,100)
y = x**2
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('plot y=x^2')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100)
y = x**4
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot y=x^4')
plt.show()

import matplotlib.pyplot as plt
def f(t):
  return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
def f(t):
  return np.exp(-t) * np.sin(2*np.pi*t)
t1 = np.arange(0.0, 0.5)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure()
plt.subplot(312)
plt.plot(t1, f(t1), t2, f(t2))
plt.subplot(311)
plt.plot(t2, np.sin(2*np.pi*t2))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(0,5,100)
plt.figure()
plt.plot(n, np.exp(-n))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(-5,5,100)
ramp = n
u1 = 1*(n>=-3)
u2 = 1*(n>=4)
u = u1-u2
plt.plot(n,ramp)
plt.xlabel('x')
plt.ylabel('x[n] = ramp [n]')
plt.title('Unit ramp sequence')
plt.show()
plt.plot(n,u)
plt.xlabel('n')
plt.ylabel('x[n] = u[n]')
plt.title('Unit step sequence')
plt.show()
