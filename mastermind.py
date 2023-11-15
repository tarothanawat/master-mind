import random

def generate_four_digit_number():
    # Generate a 4-digit number using digits 1-6
    number = ""
    for _ in range(4):
        digit = random.randint(1, 6)  # Generate a random digit between 1 and 6
        number += str(digit)  # Append the digit to the number string
    return number

# Generate and print a 4-digit number using digits 1-6

class MasterMind:
    def __init__(self):
        self.generated_num = generate_four_digit_number()

    def check_if_correct(self, guess):
        display = ""
        count = 0
        colors = "123456"
        correct = ""
        if guess == 'help':
            print(self.generated_num)
            return "cheat"
        if len(guess) != 4:
            return "invalid"
        for i in range(len(guess)):
            if guess[i] not in colors:
                return "invalid color"
            elif guess[i] == self.generated_num[i]:
                display += "*"
                count += 1
                correct += str(i)
            elif guess[i] in self.generated_num:
                display += "o"
        return display


    def run_game(self):
        print("Playing Mastermind with 6 colors and 4 positions.")
        count = 1
        while True:
            guess = str(input("What is your guess?: "))
            print(f"Your guess is {guess}")
            ans = self.check_if_correct(guess)
            if ans == "invalid":
                print("Invalid guess! Your guess must contain 4 digits.")
                print()
                continue
            if ans == "invalid color":
                print("Invalid color code! Color code must be within digit 1-6.")
                print()
                continue
            if ans == 'cheat':
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




