import random


class Game:
    def __init__(self):
        self.difficulty_level: int = self.set_game_difficulty()

        self.computer_input: int = self.get_computer_input(self.difficulty_level)

    def get_computer_input(self, game_level: int) -> int:
        computer_input: int = random.randrange(1, game_level)

        return computer_input

    def set_game_difficulty(self) -> int:
        game_difficulties = (10, 30, 50, 100, 1000, 10000)
        game_difficulties_length = 5
        while True:
            try:
                difficulty = int(input("Choose a game difficulty: ")) - 1

                if difficulty in range(game_difficulties_length):
                    return game_difficulties[difficulty]
                else:
                    print(
                        f"Error: Please choose a difficulty between 1 ~ {game_difficulties_length}"
                    )
            except ValueError:
                print("Error: Please type a number ")

    def game_logic(self):
        max_value = self.difficulty_level
        least_value = 1
        while True:
            user_input = (
                input(
                    f"A number has been generated between {least_value} and {max_value}. Guess what it is!, 'Q' to quit: "
                )
                .strip()
                .upper()
            )
            if (user_input != "Q") and (not user_input.isdigit()):
                print(f"{user_input} is invalid, please give a value or 'Q' to quit.")
                continue

            if user_input == "Q":
                return

            user_input = int(user_input)

            if user_input not in range(least_value, self.difficulty_level + 1):
                print(
                    f"{user_input} is not in the range of {least_value} ~ {max_value}."
                )
                continue

            if user_input == self.computer_input:
                print(
                    f"Congratulations!! you got it {user_input} was the right answer."
                )
                return

            if user_input > self.computer_input:
                max_value = user_input
                print(
                    f"You're above. The correct value is between {least_value} and {max_value}"
                )
            elif user_input < self.computer_input:
                least_value = user_input
                print(
                    f"You're below. The correct value is between {least_value} and {max_value}"
                )


def main():
    print("\nHi!, Welcome to the Number Guessing Game.\n")
    print("What game difficulty would you like?:\n  ")
    print("1. Easy: 1 ~ 10")
    print("2. Medium: 1 ~ 30")
    print("3. Hard: 1 ~ 50")
    print("4. Insane: 1 ~ 100")
    print("5. Omo: 1 ~ 1000")
    print("6. Ewo: 1 ~ 10000\n")

    game = Game()
    game.game_logic()


if __name__ == "__main__":
    main()
