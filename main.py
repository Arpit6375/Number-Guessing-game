import random
import math
 # Take Inputs
lower = int(input("Enter Lower bound :- ")) 
 
# Take Inputs
upper = int(input("Enter Upper bound :- "))  
 
# generating any random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
 
 # Initialize number of guesses
count = 0
 
# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
   
    # take guessing number as input
    guess = int(input("Guess a number :- ")) 
     
    # Condition testing
    if x == guess:  
       print("Congratulations you did it in ", count, " tries!")
       # Once guessed, loop will break 
       break
    elif x > guess:
       print("You Guessed too Small!")
    //////
 
# If Guessing is more than required guesses, then shows this output
if count >= math.log(upper - lower + 1, 2):
   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time !")
