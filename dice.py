import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def main():
    value = roll()
    while True:
        print(value)
        answer = input('Roll again? (y/n) ')
        if answer == "n":
            break
        value = roll()

main()

