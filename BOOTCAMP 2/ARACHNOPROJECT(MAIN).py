#access libraries and py files 
import spiderDraw as sd
import functions as md
import os
import time
#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries

name = input("What is your name?")
print(f''' _______________
          | Welcome       |
          |       to      |
          | ArachnoPhonics| 
          |     {name}!!! |
          |_______________| ''')
correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True 

#Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]
#Makes calling functions easier. Just index it from the list.

#Print intro statements (welcome to game, etc)



#generate a random word from word list
word = md.generate_word()  



#Game Loop
while game: 
  md.introduction()
  tries = md.check_word(correct, incorrect, word, tries)
  
  #md.print_spider(tries,spiderList)
  
  time.sleep(1)
  os.system("clear")
  progress = md.print_word(word, correct)
  print(f"Word = {progress}")
  md.print_spider(tries,spiderList)
  print(f"Incorrect guesses so far: {incorrect}")
  

  #This is where you'll call all of your functions. Just need to decide the proper order.


  #You will also need to specify your win and lose conditions in here