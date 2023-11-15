import random


def generate_four_digit_number(y):
    number = ""
    for _ in range(4):
        digit = random.randint(1, y)
        number += str(digit)
    return number


class MasterMind:
    def __init__(self):
        self.color_range = 6
        self.generated_num = generate_four_digit_number(self.color_range)
        self.digits = 4

    def check_if_correct(self, guess):
        display = ""
        count = 0
        colors = "123456"
        correct = ""
        if guess == 'help':
            self.check_error("cheat")
            return "error"
        if len(guess) != 4:
            self.check_error("invalid")
            return "error"
        for i in range(len(guess)):
            if guess[i] not in colors:
                self.check_error("invalid color")
                return "error"
            elif guess[i] == self.generated_num[i]:
                display += "*"
                count += 1
                correct += str(i)
            elif guess[i] in self.generated_num:
                display += "o"
        return display

    def check_error(self, ans):
        if ans == "invalid":
            print("Invalid guess! Your guess must contain 4 digits.")
            print()
        if ans == "invalid color":
            print("Invalid color code! Color code must be within digit 1-6.")
            print()
        if ans == 'cheat':
            print(self.generated_num)
            print()

    def run_game(self):
        print("Playing Mastermind with 6 colors and 4 positions.")
        count = 1
        while True:
            guess = str(input("What is your guess?: "))
            print(f"Your guess is {guess}")
            ans = self.check_if_correct(guess)
            if ans == "error":
                print()
                continue
            print(ans)
            print()
            if ans == "****":
                break
            count += 1

        print(f"You solve it after {count} rounds")


game1 = MasterMind()
game1.run_game()




