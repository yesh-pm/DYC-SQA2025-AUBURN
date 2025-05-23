import random
import re
import math
import string

#Checks if number is even
def fuzzEven():
    try:
        n = random.randint(-100, 100)
        print(f"Is {n} even?")
        if (n % 2) == 0:
            print("Yes")
    except Exception as e:
        print("Error in fuzzEven", e)

#Checks if number is odd
def fuzzOdd():
    try:
        n = random.randint(-100, 100)
        print(f"Is {n} odd?")
        if n % 2 == 1:
            print("Yes")
    except Exception as e:
        print("Error in fuzzOdd", e)

#Checks if both randomly generated numbers match
def fuzzChance():
    try:
        n1 = random.randint(0, 100)
        n2 = random.randint(0, 100)
        if n1 == n2:
            print("Match")
    except Exception as e:
        print("Error in fuzzChance", e)

#Calculates the sqrt of the number
def fuzzSqrt():
    try:
        num = random.randint(-100, 100)
        math.sqrt(num)
    except ValueError:
        pass
    except Exception as e:
        print("Error in fuzzSqrt", e)

#Matches 2 strings
def fuzzMatch():
    try:
        pattern = ''.join(random.choices(string.printable, k=3))
        rstring = ''.join(random.choices(string.printable, k=8))
        re.match(pattern, rstring)
    except re.error:
        pass
    except Exception as e:
        print("Error in fuzzMatch", e)

if __name__ == '__main__':
    for i in range(10):
        fuzzEven()
        fuzzOdd()
        fuzzChance()
        fuzzSqrt()
        fuzzMatch()
