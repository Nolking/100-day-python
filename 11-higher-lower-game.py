from higher_lower_data import data
from random import randint

data_size = len(data)
is_game_end = False
choice_A = data[randint(0, data_size - 1)]
choice_B = data[randint(0, data_size - 1)]
user_score = 0


def comparison_result(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"


def game():
    global choice_A, choice_B, user_score, is_game_end
    while choice_A == choice_B:
        choice_B = data[randint(0, data_size - 1)]
    print(f"Compare A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}")
    print("vs")
    print(f"Against B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice != comparison_result(choice_A, choice_B):
        print(f"Sorry, that's wrong! Final score is: {user_score}")
        is_game_end = True
    else:
        print("That's correct!!! ")
        choice_A = choice_B
        choice_B = data[randint(0, data_size - 1)]
        user_score += 1


while not is_game_end:
    game()
