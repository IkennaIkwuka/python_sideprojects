# Full Calculator App Project

# Libs


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        prompt = "What do you want to calculate\n:  "
        user_input = input(prompt)
        print(self.validate_input(user_input))

    # def get_user_input(self):
    #     prompt = "What do you want to calculate\n:  "
    #     user_input = input(prompt)
    #     self.validate_input(user_input)
    #     pass

    def validate_input(self, input: str):
        input = input.strip()
        values = input.split()
        operands = []
        operators = []

        for i, val in enumerate(values):
            # checks validity of input
            if not val.isdigit() and val not in self.SYMBOLS:
                raise ValueError(
                    f"Input: {values}\n\tError: This is an invalid input. '{val}'"
                )

            # checks whether last inputted value is not a number or not
            if not values[-1].isdigit():
                raise ValueError(
                    f"Input: {values}\n\tError: You cannot end with '{values[-1]}'"
                )

            # checks the order of values inputted
            # By order of operand | operator | operand | operator | etc
            if i % 2 == 0 and not val.isdigit():
                raise ValueError(
                    f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                )
            elif i % 2 != 0 and val not in self.SYMBOLS:
                raise ValueError(
                    f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                )

            if i % 2 == 0:
                operands.append(val)
            if i % 2 != 0:
                operators.append(val)
        return operands, operators

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
