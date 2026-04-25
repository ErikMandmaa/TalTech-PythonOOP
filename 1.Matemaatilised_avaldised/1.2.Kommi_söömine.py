"""Eat candy."""


def eat_candy(candy: int, is_diet: bool, christmas_time: bool) -> int:
    """
    Return how much candy will be left after eating candy.

    On a regular day you would eat 10 candy.
    If it's christmas time, you eat double the amount of normal eating amount.
    If you are on a diet, you eat 5 less than you would otherwise.
    Always leave at least 1 candy left (never eat all).
    """
    if candy == 0:
        return 0
    amount = 10

    if christmas_time:
        amount *= 2

    if is_diet:
        amount -= 5

    return max(1, candy - amount)


if __name__ == '__main__':
    print(eat_candy(10, False, False))  # 1
    print(eat_candy(100, True, False))  # 95
    print(eat_candy(100, False, True))  # 80