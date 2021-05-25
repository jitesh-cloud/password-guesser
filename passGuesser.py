# importing random lib for checking out random pass
from random import *

# Taking a sample password from user to guess
give_pass = input("Enter your password: ")

# storing alphabet letter to use thm to crack password
randomPass = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v',
            'w', 'x', 'y', 'z']

# initializing an empty string
actualguess = ""
count = 0

# using loop to catch the give_pass by random guesses
# it is also showing count of the passes
while (actualguess != give_pass.lower()):
    actualguess = ""
    # generating random passwords using for loop
    for letter in range(len(give_pass)):
        guess_letter = randomPass[randint(0, 25)]
        actualguess = str(guess_letter) + str(actualguess)
    # printing guessed passwords
    print(actualguess,"-",count+1)
    count+=1

# printing the matched password
print("--------------------------------------------------------")
print("Your input is", give_pass,"-->","Your password is",actualguess)
