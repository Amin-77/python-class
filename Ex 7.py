'012'
a=input('please enter your first number: ')
b=input('please enter your second number: ')
if a>b:
    print(a,b)
else:
    print(b,a)
'013'
a=int(input('please enter your number: '))
if a<20:
    print('thank you')
else:
    print('too much')
'014'
a=int(input('please enter your number: '))
if a<=20 and a>=10:
    print('thank you')
else:
    print('incorrect answer')
'015'
a=input('please enter your favorite colour: ')
if a.upper()=='RED':
    print('I like red too')
else:
    print('I dont like ' + a + ',I prefer red')
    
'016'
a=input('is it raining? ').lower()
if a=='yes':
    b=input('is it windy? ').lower()
    if b=='yes':
        print('its too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')
'017'
a = int(input('please enter your age: '))
if a>=18:
    print('you can vote')
elif a==17:
    print('you can drive')
elif a==16:
    print('you can buy a lottery ticket')
else:
    print('you can go trick or treating')
'018'
a = int(input('please enter your number: '))
if a<10:
    print('too low')
elif a>=10 and <=20:
    print('correct answer')
else:
    print('too high')
'019'
a = int(input('please enter your number: '))
if a==1:
    print('Thank you')
elif a==2:
    print('well done')
elif a==3:
    print('correct')
else:
    print('Error message')
