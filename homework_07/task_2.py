from math import sqrt


def square(square_side: int) -> dict:
    """
    Simple function to calculate square perimeter, square area and square diagonal basing on provided square side.
    :param square_side: value of one square side, should be an integer.
    :return: dictionary with calculated square perimeter, square area and square diagonal
    """
    return {"perimeter": square_side*4,
            "square area": square_side**2,
            "diagonal": square_side * sqrt(2)}
