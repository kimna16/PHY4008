
import numpy as np
import matplotlib.pyplot as pl

def f1(x):
    return (x-1)**2+1

def f2(x):
    return (x-2)**2+2

x_vec=np.linspace(0,3,50)

y=np.array([[f1(a) for a in x_vec],[f2(a) for a in x_vec]])

new_y1=np.amin(y,1)
newindex_x1=np.argmin(y,1)
new_x1=[]
count=0
for x in x_vec:
    if (count in newindex_x1):
        new_x1.append(x)
    count+=1
new_x1=np.array(new_x1)


def pos_f(x, a, b, c):
    return c*((x-a)**2)+b

value=[x/7 for x in range(1,6)]
print(value)

pl.plot(x_vec, [[pos_f(x,new_x1[0],new_y1[0],c) for c in value] for x in x_vec])
pl.plot(x_vec, [[pos_f(x,new_x1[1],new_y1[1],c) for c in value] for x in x_vec])

x_vec=x_vec.reshape(1,50)
pl.plot(x_vec[0],y[0:][0])
pl.plot(x_vec[0],y[1:][0])

















