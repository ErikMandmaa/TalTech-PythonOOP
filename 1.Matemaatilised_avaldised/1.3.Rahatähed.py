"""Banknotes needed for amount."""


def banknotes(amount: int) -> int:
    """
    How many banknotes are required for the amount.

    Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

    Given the amount, return how many banknotes does it take to cover the sum. Task is to cover the sum with as little
    banknotes as possible.

    The amount of different banknotes is not limited in the machine.

    Example:
    The amount is 72€
    We use four banknotes to cover it. The banknotes are 50€, 20€, 1€ and 1€.
    The result is 4.
    """
    count = 0
    for note in [100, 50, 20, 10, 5, 1]:
        count += amount // note
        amount %= note
    return count


if __name__ == '__main__':
    print(banknotes(1))  # 1
    print(banknotes(6))  # 2
    print(banknotes(72))  # 4
    print(banknotes(0))  # 0