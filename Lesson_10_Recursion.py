existing_userNames = ['shaquille.oatmeal','google_was_my_idea', 'fedora_the_explorer','OP_rah','AllGoodNamesRGone',
                      'unfinished_sentenc','anonymouse','PawneeGoddess','chickenriceandbeans','fluffycookie',
                      'toastedbagelwithcreamcheese','idrinkchocolatemilk','kim_chi','santas_number1_elf',
                      'nachocheesefries','personallyvictimizedbyreginageorge','just-a-harmless-potato']




def ig_account():
  username = input('Choose a username. ')
  
  if username in existing_userNames:
    print('That name already exists, choose another. ')
    ig_account() #repeating lines 9-13 until username is unique/meets conditions
  else:
    print(f'Your new username is {username}. ')
    
  existing_userNames.append(username)
  print('Okay, time to set up your password. ')

  return existing_userNames

ig_account()
