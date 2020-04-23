class coordination:
    x=0
    y=0
a=input('mokhtasat x noghte avval')
b=input('mokhtasat x noghte dovom')
c=input('mokhtasat y noghte avval')
d=input('mokhtasat y noghte dovom')
n1=coordination()
n2=coordination()
n1.x=a
n1.y=c
n2.x=b
n2.y=d
def distance(obj1,obj2):
    return ((obj1.x-obj2.x)**2+(obj1.y-obj2.y)**2)**0.5
