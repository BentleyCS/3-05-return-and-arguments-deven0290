#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.

def larger():
   
    n1_input = input("Please enter the first number")
    n2_input = input("Please enter the second number")

    n1 = int(n1_input)
    n2 = int(n2_input)

    if n1 > n2:
        print(f"The larger number is: {n1}")
    else:
        print(f"The larger number is: {n2}")



def grade():
    score = int(input("Give me your score"))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

grade()

def fizzBuzz():
    n = input("Give me a number: ")
    n = int(n)
    if (n % 5 == 0 and n % 3 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0):
        print("fizz")
    elif (n % 5 == 0):
        print("buzz")
    else:
        print(n)

def collatz():
    """
    This function takes an integer input from the user.
    If the number is even, it divides it by two.
    If the number is odd, it multiplies it by 3 and adds 1.
    The new number is then printed.
    """
    try:
        n_str = input("Give me a number: ")
        n = int(n_str)
        
        if n % 2 == 0:
            new_number = n / 2
        else:
            new_number = 3 * n + 1
        
        print(new_number)
        
    except ValueError:
        print("Invalid input. Please enter an integer.")



def convertTemperature():
    user_input = input("Give me a temperature (e.g., 32F or 20C): ")

    if not user_input:
        print("No input provided. Please enter a temperature.")
        return

    unit = user_input[-1].upper()
    try:
        temperature_value = float(user_input[:-1])
    except ValueError:
        print("Invalid temperature value. Please enter a number followed by 'F' or 'C'.")
        return

    if unit == "C":
        fahrenheit = (temperature_value * 9/5) + 32
        print(f"{int(temperature_value)}C -> {int(fahrenheit)}F")
    elif unit == "F":
        celsius = (temperature_value - 32) * 5/9
        print(f"{int(temperature_value)}F -> {int(celsius)}C")
    else:
        print("Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")

convertTemperature()
