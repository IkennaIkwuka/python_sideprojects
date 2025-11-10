# Full Basic Calculator App Project

# Libs
import sys
import time
from decimal import Decimal


def typewriteEffect(text: str, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        typewriteEffect("App Starts...\n")
        typewriteEffect("Welcome to the Basic Calculator Terminal App\n")

        prompt = "What do you want to calculate\n:  "

        user_input = input(prompt)

        operands, operators = self.validate_input(user_input)

        eval_expr: str | None = self.eval_input(operands, operators)

        if isinstance(eval_expr, str):
            self.fix_input(eval_expr)

    def fix_input(self, eval_expr: str):
        typewriteEffect("\nYour expression ran into an overflow error.")
        typewriteEffect("\nThis can be due to:")
        typewriteEffect("  - Huge exponent")
        typewriteEffect("  - Combined with true division '/'")
        typewriteEffect("\nThe program will now 'fix' your expression.")

        typewriteEffect("\n...Wrapping operands in 'Decimal()' function", 0.01)
        time.sleep(2)

        eval_expr = eval_expr.strip()

        for i, _ in enumerate(eval_expr.split()):
            if i % 2 == 0:
                # adds Decimal() wrap to operands to avoid overflow error
                eval_expr = eval_expr.replace(_, f"Decimal({_})")

        print("\nSuccessful")

        typewriteEffect(
            "\n...Adding parentheses to exponentiation and division expressions", 0.01
        )
        time.sleep(2)

        eval_expr_split = eval_expr.split()

        # adds parentheses to division and exponentiation sub-expressions to resolve overflow error
        if "**" in eval_expr_split:
            idx = eval_expr_split.index("**")
            eval_expr_split.insert(idx - 1, "(")
            eval_expr_split.insert(idx + 3, ")")

        if "/" in eval_expr_split:
            idx = eval_expr_split.index("/")
            eval_expr_split.insert(idx - 1, "(")
            eval_expr_split.insert(idx + 3, ")")

        print("\nSuccessful")

        eval_expr_new = ""

        for i in eval_expr_split:
            eval_expr_new += f"{i} "

        eval_result = eval(eval_expr_new)

        typewriteEffect(f"\n{eval_expr} = {eval_result}", 0.05)

    def eval_input(self, operands: list[str], operators: list[str]):
        eval_expr = ""

        for ops, opt in zip(operands, operators):
            eval_expr += ops + " " + opt + " "

        eval_expr += f"{operands[-1]}"

        # converts "^" to "**" for eval() to work with "^" in python
        eval_expr = eval_expr.replace("^", "**")

        try:
            eval_result = eval(eval_expr)

            typewriteEffect(f"\n{eval_expr} = {eval_result}", 0.05)

        except OverflowError:
            return eval_expr

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
            else:
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


if __name__ == "__main__":
    calc_app()
