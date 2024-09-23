# Complete your individualized AI problems here

#1. Even or Odd
#Write a program that asks the user for a number and then determines whether the number is even or odd. The program should print "Even" if the number is even and "Odd" if the number is odd.

#Requirements:
#-Prompt the user for a number.
#-Check if the number is even or odd.
#-Print the appropriate result.

num = int(input("Input a number:"))
if num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

#2. Simple Age Calculator
#Create a program that asks the user for their birth year and then calculates their age. The program should assume the current year is 2024.

#Requirements:
#-Prompt the user for their birth year.
#-Calculate the age based on the current year.
#-Print the user's age.

birthyear = int(input("Input your birthyear:"))
age = 2024 - birthyear
print(age)

#3. List of Numbers
#Write a program that generates a list of numbers from 1 to 10 and prints each number on a new line. You should use a loop to print the numbers.

#Requirements:
#-Create a list with numbers from 1 to 10.
#-Print each number on a new line using a loop.

new_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range (len(new_lst)):
    print(new_lst[x])


def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

