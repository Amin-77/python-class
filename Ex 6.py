def fib1(n):
    """in tabe ozve n om donbale fibonachi ra midahad"""
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)
list1=[]
def fib2(n):
    """in tabe listi az n ozve avval donbale fibonachi ra midahad"""
    i=n
    while n:
        if fib1(n) not in list1:
            list1.append(fib1(n))
        n -=1
    if i>1:
        list1.append(1)
    list2=list1.copy()
    list1.clear()
    return list2
