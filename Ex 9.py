'045'
total=0
while(total<50):
    a=int(input('enter a number: '))
    total +=a
    print('The total is... '+str(total))
'046'
a=0
while a<=5 :
    a=int(input('enter a number: '))
print('the last number you entered was... ' + str(a))
'047'
a=int(input('enter a number: '))
b=int(input('enter another one: '))
a+=b
c=input('do you want to add another number?:(y for yes) ')
while c=='y':
    b=int(input('enter a number: '))
    a+=b
    c=input('do you want to add another number?:(y for yes) ')
print('the total is: ' + str(a))
'048'
b='y'
i=0
while b=='y':
    a=input('who do you want to invite?: ')
    i+=1
    print(a+' has been invited to your party')
    b=input('do you want to invite more people?:(y for yes) ')
print('you have invited ' + str(i)+' people to your party')
'049'
compnum=50
i=1
a=int(input('enter your guess '))
while a!=compnum:
    i+=1
    if a>compnum:
        print('too high, have another guess: ')
    if a<compnum:
        print('too low, have another guess: ')
    a=int(input())
print('well done you took ' + str(i) +' attempts')
'050'
a=int(input('enter a number between 10 and 20: '))
while a<10 or a>20:
    if a<10:
        print ('too low try again: ')
    if a>20:
        print ('too high try again: ')
    a=int(input('enter a number between 10 and 20: '))
print('Thank you')
'051'
num=10
while num>0:
    print( str(num)+' green bottles sitting on the wall,And if one green bottle should accidentally fall,')
    a=int(input('How many green bottles will be hanging on the wall? '))
    num-=1
    while a!=num:
        print('no try again')
        a=int(input('How many green bottles will be hanging on the wall? '))
print('there no more bottles on the wall')
