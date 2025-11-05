str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)  # Concatenation with space
print(str1,str2)

text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[::2])

print(text[::-1])  # Reversed string

text = "i love python programming"

print(text.strip())
print(text.title())
print(text.count('o'))

str1 = "123abc"
print(str1.isalpha())
print(str1.isalnum())


name = "John"
age = 25

print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

sentence = "coding in python is fun"
new = sentence.replace("python", "Java")
print(new)

new = sentence.index("python")
print(new)

print(sentence.upper())

#problem 6

sentence = "Data Science is an interdisciplinary field."

sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in sentence.lower():
    print(char)
    if char in vowels:
        sum += 1
print(f"There are {sum} in the sentence")


string1 = "4555"

if string1 == string1[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
