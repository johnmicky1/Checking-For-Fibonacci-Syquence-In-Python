# Checking-For-Fibonacci-Syquence-In-Python
The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number (called a Fibonacci number) is equal to the sum of the preceding two numbers.

The purpose of this Python script is to check if an entered number is part of the Fibonnacci Sequence or Not

The Fibonacci Sequence (1,1,2,3,5,8,13,21,34,55,89,144,233,377...... is derived as below



# 1+1=2                         #...... 13+21=34
# 1+2=3                         #...... 21+34=55
# 2+3=5                         #...... 34+55=89
# 3+5=8                         #...... 55+89=144
# 5+8=13                        #...... 89+144=233
# 8+13=21                       #...... 144+233=377

# Declaring the function
def CheckForFibonacci():
    # Next, asking user to define their target number to check
    numberToCheck = int(input("Enter Number: "))

# Notably, in the Fibonacci Sequence, the first three terms contains only 0 and 1
# This originates from the fact that the next value, is the sum of its two predecesors
# Thus, the first three values of the Fibonacci Sequence are 0, 1, 1
    numZero = 0
    numOne = 1
    numTwo = 1

# Part 1: Doing the first/initial check immediately the user enters a value based on 0 & 1

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

Other External Resources
To find out more on creating the Fibonacci Sequence, please visit https://www.programiz.com/python-programming/examples/fibonacci-sequence and https://factpros.com/fibonacci-sequence-facts/
