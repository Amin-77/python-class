'069'
a=('Germany','France','UK','Spain','Italy')
print(a)
b=input('\nplease enter one of the vountries above: ')
i=0
for name in a: 
    if b.upper()==name.upper():
        print(i)
    i+=1
'070'
j=0
c=int(input('now enter a number (from 0 to 4): '))
for value in a:
    if j==c:
        print(value)
    j+=1
'071'
sports=['football','hockey']
a=input('whats your favorite sport?: ')
sports.append(a)
sports.sort()
print(sports)
'072'
list1=['chemistry','physics','math','sports','history','geography']
print(list1)
a=input("which one of these don't you like?: ")
if a.lower() in list1:
    list1.remove(a.lower())
print(list1)
'073'
i=1
dict1={}
print('please enter 4 items: ')
while(i<=4):
    a=input('please enter item number '+str(i) + ' : ')
    dict1[i]=a
    i+=1
print(dict1)
a=input('enter which one you want to get rid of: ')
if a in dict1.values():
    for key in dict1:
        if a == dict1[key]:
            b=key
dict1.pop(b)
list2=[]
for value1 in dict1.values():
    list2.append(value1)
print(list2)
list2.sort()
dict2={}
l=0
for value in list2:
    for k in dict1:
        if dict1[k]==value:
            l+=1
            dict2[l]=value
print(dict2)
'074'
list1=['red','blue','purple','yellow','green','pink','orange','brown','black','grey']
print (list1)
a=int(input('please enter starting number:(between 0 and 4) '))
b=int(input('please enter ending number:(between 5 and 9) '))
print(list1[a:b])
'075'
list1=[123,542,234,678]
for a in list1:
    print(str(a)+'\n')
a=int(input('please enter a three digit number: '))
i=0
if a in list1:
    while(i<=3):
        if list1[i]==a:
            print('the position is:(from 0 to 3) ' + str(i))
        i+=1
else:
    print('this number is not on the list')
'076'
list1=[]
i=3
while i>1:
    a=input('please enter a name to add to your list: ')
    list1.append(a)
    i-=1
e=''
i=0
while(e!='no'):
    a=input('please enter a name to add to your list: ')
    e=input('do you want to add more people?: ').lower()
    list1.append(a)
for value in list1:
    i+=1
print('you have invited ' + str(i) + ' people to your party')
'077'
print(list1)
a=input('enter one of the names on the list: ')
i=0
for value in list1:
    if value==a:
        print('this is the position on the list: '+str(i))
    i+=1
b=input('do you still want them on the list?: ')
if b.lower()=='no':
    list1.remove(a)
print(list1)
'078'
list1=['Show1','Show2','Show3','Show4']
print(list1)
a=input('enter another TV show: ')
b=int(input('where do you want to put it?:(from 0 to 4) '))
list1.insert(b,a)
print(list1)
'079'
nums=[]
i=0
while i<=2:
    a=int(input('enter a number: '))
    i+=1
    nums.append(a)
    print(nums)
b=input('do you want the last number you entered?: ')
if b.lower()=='no':
    nums.pop()
print(nums)

      
        
