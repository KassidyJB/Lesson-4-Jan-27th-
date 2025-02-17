import random


# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word(correct, incorrect, word, tries):
  guess = input("Guess a letter: >")
  if guess in correct or guess in incorrect:
    print("You've already guessed this letter")
  elif guess in word:
    print("This letter is correct!")
    correct.append(guess)
  elif guess not in word:
    print("This guess is inccorect.")
    incorrect.append(guess)
    tries +=1
  else:
    print("This guess is not acceptable")
  return tries
  #IF GUESS not str/IF GUESS == int:
    #print("This is not a letter!")
  #ELIF GUESS IN WORD:
    #PRINT this letter is in the word
    #correct.append()
  #ELIF GUESS NOT IN WORD:
    #PRINT this letter is not in the word
    #incorrect.append and grow spider
  #ESE GUESS IN CORRECT OR INCORRECT:
    #Tell user the guess was already repeated (invalid)
  





# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(word, correct):
  progress = ''
  for let in word:
    if let in correct:
      progress += let
    else:
      progress += "_"
  return progress



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()
  
    



#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordList = open("words.txt").read().split()
  word = random.choice(wordList)
  print('Word = ' + '_'*len(word))
  return word


  

#Put the introduction code/input player name into here 
def introduction():
  name = input(f"\nWhat is your name?\n")
  print(f''' _______________
          | Welcome       |
          |       to      |
          | ArachnoPhonics| 
          |     {name}!!! |
          |_______________| ''')
  print(f"\nWIN: Guess all letters of word before spider is 
        completely drawn\n")
  print(f"\nLOSE: Overstepping your tries or the spider is 
        completely drawn before the word is guessed\n")
introduction()


##WIN/LOSE

#IF dash NOT IN progress

# PRINT win message

# END game 

 

#ELIF tries greater than 5

# PRINT lose message

# END game


#if '_' not in progress:
    print('Congrats, you won!')
    #ASK the player if they want to play again
    #IF yes
      #Clear system
      #Clear correct letters list
      #Clear incorrect letters list 
      #Reset tries to 0
      #Generate new word

    #ELSE:
      #Print goodbye message
      #End game

  #elif tries > 5:
    print('The spider has devoured you!')
    pa = input(f'Would you like to place again? \n>').lower()
    if pa == 'yes':
      os.system('clear')
      #Clear correct letters list
      #Clear incorrect letters list 
      #Reset tries to 0
      #Generate new word

    #ELSE:
      #Print goodbye message
      #End game 