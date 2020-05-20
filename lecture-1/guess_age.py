import random

def get_game(round=10):
    turn = round
    x = random.randint(1, 100)
    def guess(num):
        nonlocal turn
        if turn <= 0:
            print("You run out of round")
            return "game over"

        if x == num:
            print(f"Correct! the number is {num}")
            return "equal"

        if x > num:
            turn -= 1
            print(f"Your number is larger, you left {turn} turn to guess")
            return "larger"

        if x < num:
            print(f"Your number is smaller, you left {turn} turn to guess")
            turn -= 1
            return "smaller"
    
    return guess

if __name__ == "__main__":
    guess = get_game(1)

    guess(10)
    guess(20)