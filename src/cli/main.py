# Full Calculator App Project

# Libs


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        self.get_user_input()
        pass

    def get_user_input(self):
        prompt = "What do you want to calculate\n:  "
        user_input = input(prompt)
        self.validate_input(user_input)
        pass

    def validate_input(self, input: str):
        input = input.strip()

        try:
            symbol_list = []

            for _ in self.SYMBOLS:
                if _ in input:
                    symbol_list.append(_)

            print(symbol_list)
            # if input.isdigit():
            #     pass
        except:
            print(f"{_} isn't a valid operator")
        pass

    # Addition method
    def add(self):
        pass

    # Subtraction method
    def sub(self):
        pass

    # Multiplication method
    def mul(self):
        pass

    # Division method
    def div(self):
        pass

    # Exponentiation method
    def expo(self):
        pass

    # Modulus method
    def mod(self):
        pass


def main():
    calc_app()


if __name__ == "__main__":
    main()
