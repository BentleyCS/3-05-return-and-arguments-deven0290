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

    - "FizzBuzz" if divisible by 3 and 5
    - "fizz" if divisible by 3 only
    - "buzz" if divisible by 5 only
    - n itself otherwise
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n


def collatz(n):
    """
    Given an integer n:
    - if n is 1, return 1
    - if n is even, return n / 2   (float)
    - if n is odd, return 3 * n + 1
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def convertTemperature(user_input):
    """
    user_input: a string like '32F' or '20C'
    Returns a string like '0C' or '68F', using integer truncation.
    """
    unit = user_input[-1].upper()
    value = int(user_input[:-1])

    if unit == "F":
        celsius = int((value - 32) * 5 / 9)
        return f"{celsius}C"
    elif unit == "C":
        fahrenheit = int((value * 9 / 5) + 32)
        return f"{fahrenheit}F"
    else:
        return None
