import random
userChoice = input('chose one from : paper , rock, scissors \n')
chosens = ['paper' ,'rock','scissors']
pcChoice = random.choice(chosens)
print(' your choice is ; ' ,userChoice , ' pc choice is ; ' ,pcChoice )


if pcChoice == userChoice :
  print(' tie')
elif (userChoice == "scissors" and pcChoice == 'paper'
or( userChoice == "paper" and pcChoice == 'rock') 
or (userChoice == "rock" and pcChoice == 'scissors')) :
  print('you win')
else :
  print('you lose')