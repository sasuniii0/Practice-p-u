fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']
print(len(fruits))  # Output: 3


#=====================================================

list1 = [i for i in range(1,11)]
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
squared = [x**2 for x in list1]
print(squared)  # Output: [1, 4, 9, 16

#====================================

numbers = [10, 23, 45, 67, 89, 12, 34]
numbers.sort()
numbers.append(100)
numbers.remove(23)
print(numbers)

#===========================================

names = ["Alice", "Bob", "Charlie"]\

names.insert(1, "David")
print(names)  # Output: ['Alice', 'David', 'Bob', 'Charlie']

#===========================================

coordinates = (10, 20)
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

coordinates[0] = 50
corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)  # Output: (50, 20)

#===========================================

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}



