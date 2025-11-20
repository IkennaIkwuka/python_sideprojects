# Full Basic Calculator App Project

# Libs
import sys
import time
from decimal import Decimal  # noqa: F401


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

        user_input = input(prompt).strip()

        operands, operators = self.validate_str(user_input)

        expr: str = self.eval_str(operands, operators)

        try:
            result = eval(expr)
            typewriteEffect(f"\n{expr} = {result}", 0.05)
        except OverflowError:
            self.fix_str(expr)

    def fix_str(self, expr: str):
        typewriteEffect("\nYour expression ran into an overflow error.")
        typewriteEffect("\nThis can be due to:")
        typewriteEffect("  - Huge exponent")
        typewriteEffect("  - Combined with true division '/'")
        typewriteEffect("\nThe program will now 'fix' your expression.")

        typewriteEffect("\n...Wrapping operands in 'Decimal()' function", 0.01)
        time.sleep(2)

        values = expr.split()

        for i in range(0, len(values), 2):
            # adds Decimal() wrap to operands to prevent overflow
            values[i] = f"Decimal({values[i]})"

        print("\nSuccessful")

        expr = " ".join(values)

        result = eval(expr)

        typewriteEffect(f"\n{expr} = {result}", 0.05)

    def eval_str(self, operands: list[str], operators: list[str]):
        expr = ""

        for ops, opt in zip(operands, operators):
            expr += ops + " " + opt + " "

        expr += f"{operands[-1]}"

        # converts "^" to "**" for eval() to work with "^" in python
        expr = expr.replace("^", "**")

        return expr

    def check_operator(self, operator: str):
        standalone = {"+", "*", "-", "/"}

        for sep in standalone:
            if operator == sep:
                return True
            continue
        return False

    def check_operand(self, operand: str):
        if operand.isdigit():
            return True

        if operand == "/":
            return True

        inner_sep = {".", "%", "^", "/"}

        for sep in inner_sep:
            if sep == operand:
                return False
            if sep in operand:
                left, right = operand.split(sep, 1)
                if left.isdigit() and right.isdigit():
                    return True
                return False
            continue
        return False

    def validate_str(self, user_input: str):
        values = user_input.split()
        operands: list[str] = []
        operators: list[str] = []

        # checks whether last inputted value is not a number or not
        if not self.check_operand(values[-1]):
            raise ValueError(
                f"Input: {values}\n\tError: You cannot end with '{values[-1]}'"
            )

        for i, val in enumerate(values):
            # checks the order of values inputted alternating operands/operator
            # By order of operand | operator | operand | operator | etc
            if i % 2 == 0:
                if not self.check_operand(val):
                    raise ValueError(
                        f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                    )
                operands.append(val)
            else:
                if not self.check_operator(val):
                    raise ValueError(
                        f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                    )
                operators.append(val)

        return operands, operators


if __name__ == "__main__":
    calc_app()
