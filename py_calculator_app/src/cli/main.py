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

        user_input = input(prompt)

        operands, operators = self.validate_str(user_input)

        eval_expr: str | None = self.eval_str(operands, operators)

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

    def eval_str(self, operands: list[str], operators: list[str]):
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

    def check_str(self, val: str, format: str = ""):
        if val.isdigit():
            return True

        if val == "/":
            return True if format == "args" else False

        if "/" in val:
            left, right = val.split("/", 1)
            if left.isdigit() and right.isdigit():
                return True
            return False

        if "." in val:
            left, right = val.split(".", 1)
            if left.isdigit() and right.isdigit():
                return True
            return False

        return False

    def validate_str(self, user_input: str):
        user_input = user_input.strip()
        values = user_input.split()
        operands: list[str] = []
        operators: list[str] = []

        for i, val in enumerate(values):
            # checks validity of input
            if not self.check_str(val) and val not in self.SYMBOLS:
                raise ValueError(
                    f"Input: {values}\n\tError: This is an invalid input. '{val}'"
                )

            # checks whether last inputted value is not a number or not
            if not self.check_str(values[-1]):
                raise ValueError(
                    f"Input: {values}\n\tError: You cannot end with '{values[-1]}'"
                )

            # checks the order of values inputted
            # By order of operand | operator | operand | operator | etc
            if i % 2 == 0 and not self.check_str(val, "args"):
                raise ValueError(
                    f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                )
            if i % 2 != 0 and val not in self.SYMBOLS:
                raise ValueError(
                    f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid and must follow the order of 'operand | operator | operand | operator | etc'"
                )

            if i % 2 == 0:
                operands.append(val)
            if i % 2 != 0:
                operators.append(val)

        return operands, operators


if __name__ == "__main__":
    calc_app()
