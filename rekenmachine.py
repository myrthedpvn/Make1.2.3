#!/usr/bin/env python

"""
Rekenmachine script
 """

# import

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def add(x, y):                                                     #To add two numbers
    return x + y

def subtract(x, y):                                                #To subtract two numbers
    return x - y

def multiply(x, y):                                                #To multiply two numbers
    return x * y

def divide(x, y):                                                  #To divide two numbers
    return x / y

def menu():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

def main():
    menu()
    while True:
        choice = input("Enter choice(1/2/3/4): ")                     #To let the user choose an input

        if choice in ('1', '2', '3', '4'):                            #To check if the choice is one of the four options
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':                                          #To use the 'add' function
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':                                        #To use the 'subtract' function
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':                                        #To use the 'multiply' function
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':                                        #To use the 'divide' function
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")

if __name__ == '__main__':  # code to execute if called from command-line
    main()