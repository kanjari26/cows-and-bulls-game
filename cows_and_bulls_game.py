import random 
  
rules = '''Cows and Bulls is a pen and paper code-breaking game usually played between 2 players. In this, a player tries to guess a secret code number chosen by the second player. The rules are as follows:

A player will create a secret code, usually a 4-digit number.  This number should have no repeated digits.
Another player makes a guess (4 digit number) to crack the secret number. Upon making a guess, 2 hints will be provided- Cows and Bulls.
Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position. 
For example, if the secret code is 1234 and the guessed number is 1246 then we have 2 BULLS (for the exact matches of digits 1 and 2) and 1 COW (for the match of digit 4 in the wrong position)
The player keeps on guessing until the secret code is cracked. 
The player who guesses in the minimum number of tries wins.'''
print(rules)

# Returns list of digits 
# of a number
def getDigits(num):
    return [int(i) for i in str(num)]
      
  
# Returns True if number has 
# no duplicate digits 
# otherwise False      
def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
  
  
# Generates a 4 digit number 
# with no repeated digits    
def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num
  
  
# Returns common digits with exact 
# matches (bulls) and the common 
# digits in wrong position (cows)
def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
      
    for i,j in zip(num_li,guess_li):
          
        # common digit present
        if j in num_li:
          
            # common digit exact match
            if j == i:
                bull_cow[0] += 1
              
            # common digit match but in wrong position
            else:
                bull_cow[1] += 1
                  
    return bull_cow
      
      
# Secret Code
num = generateNum()
tries =int(input('\nEnter number of tries: '))
  
# Play game until correct guess 
# or till no tries left
while tries > 0:
    guess = int(input("Enter your guess: "))
      
    if not noDuplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bull_cow = numOfBullsCows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1
      
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")
