import random

player = int(input("Chose your action: (1) scissor (2) rock (3)cloth"))
computer = random.randint(1, 3)
print("player action---{0}, computer action---{1}".format(player, computer))
if (player == 1 and computer == 3) or \
        (player == 2 and computer == 1) or \
        (player == 3 and computer == 2):
    print("Player won!!")
elif player == computer:
    print("we are the same")
else:
    print("Computer won")