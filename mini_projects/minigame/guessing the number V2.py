import random

geussesTaken = 0

print("hello!! What is your name?")
myName = input()

number = random.randit(1, 20)
print(" Well, " + myName + ", I am thiking of a number between 1 and 20.")
for geussesTaken in range(6):
     print('Take a guess.') 
     guess = input()
     #guess = input(int())
     guess = int(guess)
    
     if guess < number:
          print('Your guess is too low.') # Eight spaces in front of "print"
  
     if guess > number:
         print('Your guess is too high.')
  
     if guess == number:
          break
  
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' +  
          guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
    