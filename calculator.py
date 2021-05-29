from operator import truediv, mul, add, sub


class Calculator:

    def __init__(self, operator, number1, number2):
        self.operator = operator
        self.number1 = number1
        self.number2 = number2

    def calculator_operators(operator, number1, number2):
        operators = {"+": add, "-": sub, "*": mul, "/": truediv}
        method = operators.get(str(operator), lambda number1, number2: None)
        return method(number1, number2)

    @staticmethod
    def calculator_interface():
        operation = None
        allowed_operations = ["+", "-", "*", "/"]
        while operation not in allowed_operations:
            operation = input(
                """
            Enter the operation you want to perform
            Addition = +
            Subtraction = -
            Multiplication = *
            Division = /
            """
            )

        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        try:
            result = Calculator.calculator_operators(operation, number1, number2)
        except ZeroDivisionError:
            print("You cannot divide by zero")
        else:
            print(result)


if __name__ == '__main__':
    Calculator.calculator_interface()
