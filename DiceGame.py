import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1. Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")

            print(f"Current score: {current_score}")

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])      

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1,
      "wins! Score:", max_score)


 