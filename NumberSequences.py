# Number Sequence Program
# This program will make various number sequences for the user to play around with and explore. 


# ==============================================================================================================================
# Modules

import matplotlib.pyplot as plt
from decimal import *
import itertools
from sympy import sieve
import webbrowser

# ==============================================================================================================================
# Classes

class Collatz:

    def __init__(self):
        pass

    @staticmethod
    def collatzConjecture(x):
        plt.title('Here is your Collatz Conjecture chart')
        seq = ([x])
        while x > 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            seq.append(x)
            plt.plot(seq)
        print("\nIt took", len(seq),"steps to make it to one from your number.") 
        print("\nHere are the steps it took: ",seq)
        plt.show()
        

class Rational: 

    def __init__(self):
        pass

    @staticmethod
    def rationalNumbers(a,b,c):
        getcontext().prec = c
        print("\nHere is your repeating rational decimal sequence from your two numbers: ", a/b)

    @staticmethod
    def irrationalNumbers(a,b):
        getcontext().prec = b
        print("\nHere is your square root irrational decimal sequence from your number: ", Decimal.sqrt(a))


class Addition:

    def __init__(self):
        pass

    @staticmethod
    def numPat2(num1, num2, num3):
        a = 0
        it = itertools.cycle((num1,num2))
        while a < num3:
            a += next(it)
            print(a, end = " ")

    @staticmethod
    def numPat3(num1, num2, num3, num4):
        a = 0
        it = itertools.cycle((num1,num2, num3))
        while a < num4:
            a += next(it)
            print(a, end = " ")


class Prime:

    def __init__(self):
        pass

    @staticmethod
    def primeRange(numRange1, numRange2):
        print("\nHere are the prime numbers in the range that you entered: ", [i for i in sieve.primerange(numRange1, numRange2)])

    @staticmethod
    def primeRange2(numRange):
        sieve.extend(numRange)
        print("\nHere are the prime numbers up to the number you entered: ", sieve._list)
        print("\nThere are", len(sieve._list), "prime numbers up to", numRange)
    

class Kaprekar:

    def __init__(self):
        pass

    @staticmethod
    def kaprekar(num1):
        num2 = list(num1)
        num4 = sorted(num2)
        num3 = sorted(num2, key=int, reverse=True)
        num3 = ''.join(num3)
        num4 = ''.join(num4)
        num5 = int(num3)
        num6 = int(num4)
        num7 = num5-num6
        print(num7)
        num1a = str(num7)
        num2a = list(num1a)
        num4a = sorted(num2a)
        num3a = sorted(num2a, key=int, reverse=True)
        num3a = ''.join(num3a)
        num4a = ''.join(num4a)
        num5a = int(num3a)
        num6a = int(num4a)
        num7a = num5a-num6a
        print(num7a)
        num1b = str(num7a)
        num2b = list(num1b)
        num4b = sorted(num2b)
        num3b = sorted(num2b, key=int, reverse=True)
        num3b = ''.join(num3b)
        num4b = ''.join(num4b)
        num5b = int(num3b)
        num6b = int(num4b)
        num7b = num5b-num6b
        print(num7b)
        num1c = str(num7b)
        num2c = list(num1c)
        num4c = sorted(num2c)
        num3c = sorted(num2c, key=int, reverse=True)
        num3c = ''.join(num3c)
        num4c = ''.join(num4c)
        num5c = int(num3c)
        num6c = int(num4c)
        num7c = num5c-num6c
        print(num7c)
        num1d = str(num7c)
        num2d = list(num1d)
        num4d = sorted(num2d)
        num3d = sorted(num2d, key=int, reverse=True)
        num3d = ''.join(num3d)
        num4d = ''.join(num4d)
        num5d = int(num3d)
        num6d = int(num4d)
        num7d = num5d-num6d
        print(num7d)
        num1e = str(num7d)
        num2e = list(num1e)
        num4e = sorted(num2e)
        num3e = sorted(num2e, key=int, reverse=True)
        num3e = ''.join(num3e)
        num4e = ''.join(num4e)
        num5e = int(num3e)
        num6e = int(num4e)
        num7e = num5e-num6e
        print(num7e)
        num1f = str(num7e)
        num2f = list(num1f)
        num4f = sorted(num2f)
        num3f = sorted(num2f, key=int, reverse=True)
        num3f = ''.join(num3f)
        num4f = ''.join(num4f)
        num5f = int(num3f)
        num6f = int(num4f)
        num7f = num5f-num6f
        print(num7f)
        
# ==============================================================================================================================
# Collatz Conjecture menu functions

def collatz_menu():
    print("\nWelcome to Bruce's Collatz Conjecture Program.")
    print("\nWhat is the Collatz Conjecture?")
    print(""" \nThe Collatz Conjecture states that if you take any positive number and perform the following operations on it:
    * If the number is even, divide it by two.
    * If the number is odd, triple it and add one.
That process will eventually reach the number 1, regardless of which positive number was chosen initially""")
    print("\n** Close the chart made to run the program again **")
    
    x = int(input("\nEnter a number to run the Collatz Conjecture Program on and see if it goes to one: ", ))
    Collatz.collatzConjecture(x)

    again()

def again():
    calc_again = input('''
Do you want to run the Collatz Conjecture program again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        collatz_menu()
    elif calc_again.upper() == 'N':
        print('Exit.')
    else:
        again()


# ==============================================================================================================================
# Rational & Irrational Number menu functions

def rational_irrational():
    print("\nWelcome to Bruce's Rational & Irrational Number Sequence Generator.")
    print("\n1. Rational Number Sequence Generator")
    print("2. Irrational Number Sequence Generator")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        print("\nRational Number Sequence Generator.")
        print("\nIt generates rational decimal number sequences by having the user input two numbers and divides them and prints out the result to whatever amount of decimal patterns you choose to show the patterns")
        a = Decimal(input("\nEnter a number or a decimal number: ",))
        b = Decimal(input("Enter a number or a decimal number: ",))
        c = int(input("Enter how many decimal places you want the number printed out to: ",))
        Rational.rationalNumbers(a,b,c)

    elif choice == '2':
        print("\nIrrational Number Sequence Generator.")
        print("\nIt generates irrational decimal number sequences from square roots")
        a = Decimal(input("\nEnter a number or a decimal number: ",))
        b = int(input("Enter how many decimal places you want the number printed out to: ",))
        Rational.irrationalNumbers(a,b)

    again2()

def again2():
    calc_again = input('''
Do you want to run the Rational & Irrational Number program again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        rational_irrational()
    elif calc_again.upper() == 'N':
        print('Exit.')
    else:
        again2()


# ==============================================================================================================================
# Simple Addition Sequence menu functions

def addition_sequence():
    print("\nWelcome to Bruce's Simple Addition Number Sequence Program.")
    print("\n1. Simple Addition Number Sequence Generator with Two Numbers")
    print("2. Simple Addition Number Sequence Generator with Three Numbers")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        print("\nSimple Addition Number Sequence Generator with Two Numbers.")
        print("\nIt generates a simple sequence of two numbers being continously added to one another")
        print("\nEnter any two numbers to add together repeatedly and choose up to what number to do so.")
        num1 = int(input("\nEnter your first number: ", ))
        num2 = int(input("Enter your second number: ", ))
        num3 = int(input("Enter what number you want to run the pattern up to: ", ))
        print("Here is your number sequence:")
        Addition.numPat2(num1, num2, num3)

    elif choice == '2':
        print("\nSimple Addition Number Sequence Generator with Three Numbers.")
        print("\nIt generates a simple sequence of three numbers being continously added to one another")
        print("\nEnter any three numbers to add together repeatedly and choose up to what number to do so.")
        num1 = int(input("\nEnter your first number: ", ))
        num2 = int(input("Enter your second number: ", ))
        num3 = int(input("Enter your third number: ", ))
        num4 = int(input("Enter what number you want to run the pattern up to: ", ))
        print("Here is your number sequence:")
        Addition.numPat3(num1, num2, num3, num4)

    again3()

def again3():
    calc_again = input('''
Do you want to run the Simple Addition sequence program again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        addition_sequence()
    elif calc_again.upper() == 'N':
        print('Exit.')
    else:
        again3()

# ==============================================================================================================================
# Prime Number Sequence menu functions

def prime_numbers():
    print("\nWelcome to Bruce's Prime Number Sequence Program.")
    print("\n1. Calculate Prime Numbers from a Range of Numbers")
    print("2. Calculate Prime Numbers up to a Certain Number")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        print("Calculate Prime Numbers from a Range of Numbers")
        print("\nEnter a range of numbers to get the prime numbers within it")
        numRange1 = int(input("\nPlease enter the first number of your number range: "), )
        numRange2 = int(input("Please enter the second number of your number range: "), )
        Prime.primeRange(numRange1, numRange2)

    elif choice == '2':
        print("Calculate Prime Numbers up to a certain number")
        numRange = int(input("\nPlease enter a number to print out the prime numbers up to it: "), )
        Prime.primeRange2(numRange)

    again4()

def again4():
    calc_again = input('''
Do you want to run the Prime Number sequence program again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        prime_numbers()
    elif calc_again.upper() == 'N':
        print('Exit.')
    else:
        again4()


# ==============================================================================================================================
# Kaprekar Constant menu functions

def kaprekar_constant():
    print("\nWelcome to Bruce's Kaprekar Constant Program.")
    print("\n1. Calculate the Kaprekar Constant")
    print("2. Watch a video about the Kaprekar Constant")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        print("Calculate the Kaprekar Constant")
        print("\nThis program generates seven iterations of the algorithm used to generate the Kaprekar Constant which is the number 6174.")
        print("\nThis program is still experimental. If a result ends up in 999 and a series of zeros, re-enter the number as 0999 to get the correct answer.")
        print("Other numbers can be used such as three digit numbers. They will converge on 495. The same error correction holds true if the number is 99 followed by zeros.")
        print("\nHigher collection of digits such as five or six digits numbers will result in repeating patterns. Results will vary.")
        num1 = str(input("\nPlease enter any four digit number whose numbers are not all the same: ",))
        Kaprekar.kaprekar(num1)

    elif choice == '2':
        print("A video from Numberphille about what is the Kaprekar Constant:")
        url = 'https://www.youtube.com/watch?v=d8TRcZklX_Q'
        webbrowser.open_new(url)

    again5()

def again5():
    calc_again = input('''
Do you want to run the Kaprekar Constant program again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        kaprekar_constant()
    elif calc_again.upper() == 'N':
        print('Exit.')
    else:
        again5()

    
# ==============================================================================================================================
# Main Global Menu

while True:
    print("\nWelcome to Bruce's Number Sequence Calculator Version 1.0")
    print("\nPlease choose from the menu the kind of number sequences you would like to explore.")
    print("\n1. Collatz Conjecture")
    print("2. Rational & Irrational Number Sequences")
    print("3. Simple Addition Number Sequences")
    print("4. Prime Number Sequences")
    print("5. Kaprekar Constant")

    choice = input("\nEnter choice(1/2/3/4/5): ")

    if choice == '1':
        collatz_menu()

    elif choice == '2':
        rational_irrational()

    elif choice == '3':
        addition_sequence()

    elif choice == '4':
        prime_numbers()

    elif choice == '5':
        kaprekar_constant()


    while True:
        answer = input('\nRun the Main Number Sequence Calculator again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break