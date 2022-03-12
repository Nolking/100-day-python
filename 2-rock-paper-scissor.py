import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

computer_input = random.randint(0,2)
user_input = int(input("Make your choice in rock, paper, scissor game ! Type 0 for rock, 1 for paper or 2 scissor: "))
choices = [rock,paper,scissors]
print('computer chooses: ')
print(choices[computer_input])
print('you choose')
result = [['tie game','you win','you lose'],['you lose','tie game','you win'], ['you win', 'you lose','tie game']]
if (user_input > 2 or user_input <0):
    print(user_input)
    print("That's invalid input you lose!!")
else:
    print(choices[user_input])
    print(f"result is : {result[computer_input][user_input]}")