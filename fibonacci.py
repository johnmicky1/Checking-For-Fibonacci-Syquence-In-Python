"""
This mini project entails using the Finabonacci. In this case I have created a function
that where a user inputs a number and the function checks whether the number 
belongs to the Fibonacci sequence or not
"""


# I Declare the function by typing
def CheckForFibonacci():
    # I then ask the user to define their target number to check
    numberToCheck = int(input("Enter Number: "))

# Note that in the Fibonacci Sequence, the first three terms contains only 0 and 1
# This this derived from the fact that the next value, is the sum of its two predecesors
# Therefore, the first three values of the Fibonacci Sequence are 0, 1, 1
    numZero = 0
    numOne = 1
    numTwo = 1

# Part 1: Do the first/initial check immediately the user enters a value based on 0 & 1

    if (numberToCheck == 0 or numberToCheck == 1):
        print("The Number is a part of Fibonacci Sequence")

# Part 2: For values greater than 0 and 1
    else:
        while numZero < numberToCheck:
            numZero = numOne + numTwo
            numTwo = numOne
            numOne = numZero
        if numZero == numberToCheck:
            print("The Number is part of Fibonacci Sequence")
        else:
            print("NO!, Number NOT part of Fibonacci Sequence")

# Call the function    
CheckForFibonacci()