import random 

options = ['rock', 'paper', 'scissors']
player_turn = ''
comp_turn = ''


def get_selection():
    player_turn = input('Choose rock, paper or scissors. ').lower()
    if player_turn == options:
        comp_turn = random.choice(options)
        print(f'\nYou chose {player_turn}, computer chose {comp_turn}.\n')
    elif player_turn not in options:
        print("this is invalid input, Please try again")
        get_selection()



  #How can we validate the user's response? 


def decide_winner(player_turn, comp_turn):
  if player_turn == comp_turn:
    print(f'Both players selected {player_turn}. It is a tie! ')
    
  elif player_turn == 'rock':
    if comp_turn != 'paper':
      print('Rock smashes scissors! You win!')
    else:
        print('Paper covers rock! You lose.')
      
  elif player_turn == 'paper':
    if comp_turn == 'rock':
      print('Paper covers rock! You win!')
    else:
      print('Scissors cuts paper! You lose.')
      
  elif player_turn == 'scissors':
    if comp_turn == 'paper':
      print('Scissors cuts paper! You win!')
    else:
      print('Rock smashes scissors! You lose.')



get_selection()
decide_winner(player_turn, comp_turn)