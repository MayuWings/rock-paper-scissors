from getpass import getpass as input

print("hehe wanna play some rock paper scissors?")
print("select your move (R, P or S)")
print()
player1 = input("player 1 > ")
print()
player2 = input("player 2 > ")
print()

if player1 == "R":
  if player2 == "R":
    print("You both picked Rock! Its a draw!")
  elif player2 == "S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2 == "P":
    print("Plaer1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1 == "P":
  if player2 == "R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2 == "S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player2 == "P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  else:
    print("Invalid Move Player 2!")
elif player1 == "S":
  if player2 == "R":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player2 == "S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player2 == "P":
    print("Player1's Scissors make confetti out of Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")