from typing import Any


def arithmetic(first_operand: int, second_operand: int, operation: str) -> Any:
    """
    Simple function to perform sum, subtraction, multiplication and division on two provided operands basing on provided
    operation. Returns string as error if provided operation is invalid.
    :param first_operand: first operand of the equation, must be an integer.
    :param second_operand: second operand of the equation, must be an integer.
    :param operation: operation to apply for operands, must be a string
    :return: integer, float (in case of division), string in case of an error
    """
    if operation == "+":
        return first_operand + second_operand
    elif operation == "-":
        return first_operand - second_operand
    elif operation == "*":
        return first_operand * second_operand
    elif operation == "/":
        return first_operand / second_operand
    else:
        return f"Not known operation: {operation}"
