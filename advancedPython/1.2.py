from time import time 
def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print(t1 - t2)
    return wrapper

@timer
def sum_1m(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

a = sum_1m(10000)
print(a)