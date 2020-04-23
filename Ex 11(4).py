class time:
    i=0
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.second = s
    def show(obj,ruz):
        obj.date = ruz
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def number_of_seconds(obj):
        return str (obj.hour*3600+obj.minute*60+obj.second)
    def sub(obj,obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second
    def kam_kardan(obj1,hh,mm,ss):
        obj1.hour -= hh
        obj1.minute -= mm
        obj1.second -= ss
    def __add__(obj,obj2):
        obj.hour += obj2.hour
        obj.minute += obj2.minute
        obj.second += obj2.second
    def regulator_plus(obj):
        while(obj.second>=60):
            obj.second-=60
            i+=1
        obj.minute +=i
        i=0
        while(obj.minute>=60):
            obj.second-=60
            i+=1
        obj.hour +=i
        i=0
        while(obj.hour>=24):
            obj.hour-=24
            
    def __eq__(obj,obj1):
        if (obj.hour==obj1.hour) and (obj.minute==obj1.minute) and (obj.second==obj1.second):
            return True
        return False
    def __gt__(obj,obj1):
        if obj.hour>obj1.hour:
            return True
        if obj.hour==obj1.hour and obj.minute>obj1.minute:
            return True
        if obj.hour==obj1.hour and obj.minute==obj1.minute and obj.second>obj1.second:
            return True
        return False
    def __lt__(obj,obj1):
        if obj.hour<obj1.hour:
            return True
        if obj.hour==obj1.hour and obj.minute<obj1.minute:
            return True
        if obj.hour==obj1.hour and obj.minute==obj1.minute and obj.second<obj1.second:
            return True
        return False
    def __ge__ (obj,obj1):
        if obj.hour>obj1.hour:
            return True
        if obj.hour==obj1.hour and obj.minute>obj1.minute:
            return True
        if obj.hour==obj1.hour and obj.minute==obj1.minute and obj.second>=obj1.second:
            return True
        return False
    def __le__ (obj,obj1):
        if obj.hour<obj1.hour:
            return True
        if obj.hour==obj1.hour and obj.minute<obj1.minute:
            return True
        if obj.hour==obj1.hour and obj.minute==obj1.minute and obj.second<=obj1.second:
            return True
        return False
    def __sub__ (obj,obj1):
        obj.hour -= obj1.hour
        obj.minute -= obj1.minute
        obj.second -= obj1.second
    def sub_regulator (obj):
        i=0
        while(obj.second<0):
            obj.second+=60
            i-=1
        obj.minute -=i
        i=0
        while(obj.minute<0):
            obj.second+=60
            i-=1
        obj.hour -=i
        i=0
        while(obj.hour<0):
            obj.hour+=24
