"""Add fractions."""


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    """
    Implement a function that takes 4 parameters.

    Parameters a and b denote the first fraction like a/b.
    Parameters c and d denote the second fraction like c/d.

    Find and return a fraction in string format that is the sum of a/b and c/d.

    NB! the fraction does not have to be in the simplest form.
    NB! the answer should not contain any commas.

    Examples:
    add_fractions(1, 3, 1, 3) # 1/3 + 1/3 => there are many correct answers like "2/3" and "6/9"
    add_fractions(2, 5, 1, 5) # 2/5 + 1/5 => there are many correct answers like "3/5" and "15/25"

    :param a: Numerator of the first fraction. Example: 1
    :param b: Denominator of the first fraction. Example: 3
    :param c: Numerator of the second fraction. Example: 1
    :param d: Denominator of the second fraction. Example: 3
    :return: Sum of the two fractions as a string in the format "numerator/denominator".
    """
    numerator = a * d + c * b
    denominator = b * d
    return f"{numerator}/{denominator}"


if __name__ == "__main__":
    print(add_fractions(1, 3, 1, 3))  # 2/3
    print(add_fractions(2, 5, 1, 5))  # 3/5
    print(add_fractions(1, 3, 1, 3))  # 2/3
    print(add_fractions(2, 5, 1, 5))  # 3/5