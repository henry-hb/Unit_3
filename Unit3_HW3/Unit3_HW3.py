"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you will get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.
"""
while(True):
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
    except ValueError:
        print("Input must be a number")
    else:
        sum = num1 + num2
        print(sum)