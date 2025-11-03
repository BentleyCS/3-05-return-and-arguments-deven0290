#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.

def larger(n1, n2):
    """Return the larger of two numbers."""
    if n1 > n2:
        return n1
    else:
        return n2


def grade(score):
    """Return the letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def fizzBuzz(n):
    """
    Return the FizzBuzz result for n.
    Usually:
    - "FizzBuzz" if divisible by 3 and 5
    - "Fizz" if divisible by 3 only
    - "Buzz" if divisible by 5 only
    - the number (or its string) otherwise
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n 


def collatz(n):
    """
    Given an integer n:
    - if n is even, return n // 2
    - if n is odd, return 3 * n + 1
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def convertTemperature(user_input):
    """
    user_input: a string like '32F' or '20C'
    Returns the converted temperature as a float.
    """
    if not user_input:
        return None  # or raise an error

    unit = user_input[-1].upper()
    value_str = user_input[:-1]
    try:
        temperature_value = float(value_str)
    except ValueError:
        return None  # or raise an error

    if unit == "C":
        # return Fahrenheit
        return (temperature_value * 9/5) + 32
    elif unit == "F":
        # return Celsius
        return (temperature_value - 32) * 5/9
    else:
        return None
