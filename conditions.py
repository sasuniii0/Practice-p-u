#if-else conditions

#1
user_input = int(input("Enter a number: "))
if user_input > 0:
    print("The number is positive.")
elif user_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#3
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 

#match-case conditions

#1
day = int(input("Enter a number (1-7) for the day of the week: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")

#2
num_1  = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")

match operation:
    case "+":
        print("The sum is:", num_1 + num_2)
    case "-":
        print("The difference is:", num_1 - num_2)
    case "*":
        print("The product is:", num_1 * num_2)
    case "/":
        print("The quotient is:", num_1 / num_2)
    case _:
        print("Invalid operation. Please enter one of +, -, *, /.")


#for loops

#1
for i in range(1,11):
    print(i)
        
#2
user_input = int(input("Enter a number: "))
for i in range(1,13):
    print(i , "x", user_input, "=", i * user_input)

#3
sum = 0 
for i in range ( 1,101):
    sum += i
print("The sum of numbers from 1 to 100 is:", sum)

#4
for i in range(1,5):
    print("* " * i)


#while loops

#1
while i in range(1,11):
    print(i)
    i += 1

#2
password = "python123"

user_input = input("Enter the password: ")
while user_input!=password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")


#3
num = 123456
print(int(str(num)[::-1]))


#break and continue and pass

#1
for i in range(1,11):
    if i == 7 :
        break
    print(i)

#2
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#3
for i in range(1,11):
    if i == 3:
        pass
    else:
        print(i)