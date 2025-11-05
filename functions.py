def greet():
    print("Hello, I'm your Python assistant!")

greet()

#===========================================

def square(x):
    return x * x

print(square(5))
print(square(10))

#===========================================

def full_name (first, last):
    return f"{first} {last}"

print(full_name("John", "Doe"))
print(full_name("Jane", "Smith"))

#===========================================

def calculate_area(length, width):
    return length * width

print(calculate_area(5, 10))
print(calculate_area(7, 3))

#===========================================

add = lambda a,b : a + b
print(add(3, 7))
print(add(10, 20))

#===========================================
square = lambda x : x * x
list1 = [1,2,3,4,5]

print(list(map(square, list1)))

#===========================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
print(factorial(7))

#===========================================

def sum_od_digits(n):
    if n == 0:
        return 0
    
    return n%10 - sum_od_digits(n//10)

print(sum_od_digits(1234))
print(sum_od_digits(5678))

#===========================================

import math

a = math.sqrt(144)
b = math.sin(math.radians(90))

print(a,b)

#===========================================

import requests
# pip install requests

a = requests.get("https://api.github.com")
print(a.json())

#===========================================

def increment():
    counter = 0
    counter += 1
    print(counter)

increment()
increment()


#===========================================

def multiply(a,b):
    return a * b

print(multiply(4,5))
print(multiply(7,3))

#===========================================
#BONUS FUNCTION



