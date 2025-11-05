# Full Calculator App Project

# Libs


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        prompt = "What do you want to calculate\n:  "
        user_input = input(prompt)
        # print(self.validate_input(user_input))
        operands, operators, input_length = self.validate_input(user_input)
        # self.eval_input(input_length)
        for i, k in operands, operators:
            print(f"i.{i}")
            print(f"k.{k}")
            pass

    def eval_input(self, obj_length):
        test_list = []
        for evens in range(0, obj_length, 2):
            for odds in range(1, obj_length, 2):
                pass

    def validate_input(self, user_input: str):
        user_input = user_input.strip()
        values = user_input.split()
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

        return operands, operators, len(values)

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
