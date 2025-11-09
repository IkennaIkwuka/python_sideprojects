# Full Basic Calculator App Project


# Libs
from decimal import Decimal
import time_utils as tUtils


class calc_app:
    SYMBOLS = ("+", "-", "*", "/", "^", "%")

    def __init__(self) -> None:
        print("App Starts...\n")
        print("Welcome to the Basic Calculator Terminal App\n")

        prompt = "What do you want to calculate\n:  "

        user_input = input(prompt)

        operands, operators = self.validate_input(user_input)

        eval_expr = self.eval_input(operands, operators)

        try:
            eval_result = eval(eval_expr)

            print(eval_expr + f" = {eval_result}")

        except OverflowError:
            eval_expr_split = self.fix_input(eval_expr)

            eval_expr_new = ""

            for i in eval_expr_split:
                eval_expr_new += f"{i} "

            eval_result = eval(eval_expr_new)

            print(f"\n{eval_expr} = {eval_result}")

    def fix_input(self, eval_expr: str):
        tUtils.typewriter("\nYour expression ran into an overflow error.")
        tUtils.typewriter("\nThis can be due to:")
        tUtils.typewriter("  - Huge exponent")
        tUtils.typewriter("  - Combined with true division '/'")

        tUtils.typewriter("\nThe program will now 'fix' your expression.")
        tUtils.typewriter("\n...Wrapping operands in 'Decimal()' function", 0.1)

        tUtils.sleep(2)

        print("\nsuccess")

        tUtils.typewriter(
            "\n...Adding parentheses to exponentiation and division expressions", 0.1
        )

        tUtils.sleep(2)

        print("\nsuccess")

        eval_expr = eval_expr.strip()
        eval_expr_split = eval_expr.split()

        for i, _ in enumerate(eval_expr_split):
            if i % 2 == 0:
                # adds Decimal() wrap to operands to avoid overflow error
                eval_expr = eval_expr.replace(_, f"Decimal({_})")

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

        return eval_expr_split

    def eval_input(self, operands: list[str], operators: list[str]):
        eval_expr = ""

        for ops, opt in zip(operands, operators):
            eval_expr += ops + " " + opt + " "

        eval_expr += f"{operands[-1]}"

        # converts "^" to "**" for eval() to work with "^" in python
        eval_expr = eval_expr.replace("^", "**")

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
