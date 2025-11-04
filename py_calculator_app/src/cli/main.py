# Full Calculator App Project

# Libs


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        prompt = "What do you want to calculate\n:  "
        user_input = input(prompt)
        self.validate_input(user_input)

    # def get_user_input(self):
    #     prompt = "What do you want to calculate\n:  "
    #     user_input = input(prompt)
    #     self.validate_input(user_input)
    #     pass

    def validate_input(self, input: str):
        input = input.strip()

        operands = []
        operators = []

        for _ in input.split():
            if not _.isdigit() and _ not in self.SYMBOLS:
                raise ValueError(f"This is invalid. '{_}'")

        for _ in self.SYMBOLS:
            if _ in input:
                operators.append(_)

        for _ in input.split():
            if _.isdigit():
                operands.append(_)

        print(operands)
        print(operators)
        #     if self.SYMBOLS not in input.split():
        #         print("Yes")
        #     else:
        #         print("No")
        # # print(input.split())
        # print(len(input.split()))

        # for _ in (input):
        #     print(f"{_}")

        # if input.isdecimal():
        #     print("decimal")
        # if input.isnumeric():
        #     print("numeric")
        # if input.isdigit():
        #     print("digit")
        # if input.isalnum():
        #     print("alphanum")
        # if input.isalpha():
        #     print("alpha")

        # try:
        #     symbol_list = []

        #     for _ in self.SYMBOLS:
        #         if _ in input:
        #             symbol_list.append(_)

        #     print(symbol_list)
        #     # if input.isdigit():
        #     #     pass
        # except:
        #     print(f"{_} isn't a valid operator")
        # pass

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
    print("App Starts...\n")
    print("Welcome to the Basic Calculator Terminal App\n")
    calc_app()


if __name__ == "__main__":
    main()
