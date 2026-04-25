"""Caught speeding."""


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """
    Return which category caught_speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    Examples:
    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category caught_speeding ticket you would get (0, 1, 2).
    """
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2


if __name__ == '__main__':
    print(caught_speeding(60, False))  # 0
    print(caught_speeding(65, False))  # 1
    print(caught_speeding(65, True))  # 0
