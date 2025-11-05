class NegativeNUmberError(Exception):
    pass

try:
    num = int(input("Enter a number : "))

    if num < 0:
        raise NegativeNUmberError("Number cannot be negative")
    
    result = 45/ num
    print(f"the result is {result}")

except ValueError:
    print("Error: Please enter the proper number")

except ZeroDivisionError:
    print("Error: cannot devide by 0")

except NegativeNUmberError as e:
    print(f"Error: {e}")