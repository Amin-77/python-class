import numpy as np

import matplotlib.pyplot as plt
"""part one"""
'''x=4
print(x)
x=np.square(x)
print(x)
x=np.power(x,3)
print(x)
theta=1

print(np.sin(theta))'''
'radian is being used'
'''meshPoints=np.linspace(-1,1,500)
print(meshPoints[53])
print('the value is: ' + str(meshPoints[53]))
pi=np.pi
plt.plot(meshPoints,np.sin(2*pi*meshPoints))
plt.show()'''
"""part two"""
'''
vec1=np.array([-1.,4.,-9.])
mat1=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
vec2=(np.pi/4)*vec1
print(vec2)
vec2=np.cos(vec2)
print(vec2)
vec3 =vec1+2*vec2
print(vec3)
vec4=np.multiply(mat1,vec3)
print(vec4)
print(mat1.transpose())
print(np.linalg.det(mat1))
print(np.trace(mat1))
print(np.where(vec1==np.min(vec1)))
print(np.amin(mat1))
A=np.array([[17,24,1,8,15],[23,5,7,14,16],[10,12,19,21,3],[11,18,25,2,9]])
print(A)
print(np.sum(A,axis=0))
if min(np.sum(A,axis=0))==max(np.sum(A,axis=0)) and min(np.sum(A,axis=1))==max(np.sum(A,axis=1)):
    if np.sum(np.diag(A))==np.sum(np.fliplr(A)):
        print('magic square')
    else:
        print('not a magic square')  
else:
    print('not a magic square')
print(np.random.rand(10, 10))
'''
'''
"""part three"""
x=np.linspace(0,10,num=50)
y1=np.exp(-x/10)*np.sin(np.pi*x)
y2=x*np.exp(-x/3)
plt.plot(x,y1,y2,label = 'f(x)')
plt.xlabel('mehvar x ha')
plt.ylabel('mehvar y ha')
plt.show()
theta=np.linspace(0,2*np.pi,num=50)
print(theta)
R=1.2
r=R+np.cos(theta)
print(r)

x1=r*np.cos(theta)
y=r*np.sin(theta)
plt.plot(x1,y)
plt.xlabel('mehvar x ha')
plt.ylabel('mehvar y ha')
plt.show()
'''
