"""Count odds and evens."""


def count_odds_and_evens(numbers: list) -> tuple:
    """
    Count how many odd and even numbers are in the list.

    The task is to count how many odd and even numbers does the given list contain.
    Result should be displayed as tuple (odds, evens)

    Examples:
    count_odds_and_evens([1, 2, 3]) => (2, 1)
    count_odds_and_evens([1, 3]) => (2, 0)

    :param numbers: List of integers. Example: [1, 2, 3]
    :return: A tuple with two integers: (number of odd numbers, number of even numbers). Example: (2, 1)
    """
    odds = 0
    evens = 0

    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1

    return odds, evens


if __name__ == '__main__':
    print(count_odds_and_evens([1, 2, 3]))  # (2, 1)
    print(count_odds_and_evens([1, 3]))  # (2, 0)
    print(count_odds_and_evens([2, 4, 6]))  # (0, 3)