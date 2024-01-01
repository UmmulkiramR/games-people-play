import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' + "= 1"
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' + "= 2"
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' + "= 3"

print(f"{rock}\n{paper}\n{scissors}")

game = [rock, paper, scissors]

def gameFunction():
    playerschoice = int(input("Player, what's your choice - 1, 2, 3 or 0 ?\n"))
    if playerschoice == 0:
        return 0;
    print(game[playerschoice-1])

    computersChoice = random.randint(1, 3)
    print(f"Computer chooses: {game[computersChoice-1]}")

    choices = [playerschoice,computersChoice]
    if playerschoice == computersChoice:
        print("it is a DRAW")
    elif choices.__contains__(1) and choices.__contains__(3):
        if playerschoice == 1:
            print("You win!")
        else:
            print("Comp wins!")
    elif choices.__contains__(3) and choices.__contains__(2):
        if playerschoice == 3:
            print("You win!")
        else:
            print("Comp wins!")
    elif choices.__contains__(2) and choices.__contains__(1):
        if playerschoice == 2:
            print("You win!")
        else:
            print("Comp wins!")


res = 1
while res != 0:
    res = gameFunction()
