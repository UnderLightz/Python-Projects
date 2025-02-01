import random

def toss():
    return random.choice(['Heads', 'Tails'])


def main():
    value = toss()
    while True:
        print(value)
        answer = input('Do you want to flip again? (y/n) ')
        if answer == "n":
            break
        value = toss()

main()
