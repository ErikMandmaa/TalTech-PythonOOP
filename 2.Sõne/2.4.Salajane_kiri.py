"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    Examples:
    secret_letter("sOMEteSTLETTer8") => True
    secret_letter("thisisNOTvaliD4") => False
    secret_letter("TOOMANYnumbers99") => False

    :param letter: secret letter
    :return: validation
    """
    upper_count = 0
    lower_count = 0
    digit_sum = 0

    for ch in letter:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
        elif ch.isdigit():
            digit_sum += int(ch)

    if not (lower_count < upper_count):
        return False
    if not (digit_sum <= upper_count):
        return False
    if not (digit_sum >= lower_count):
        return False

    return True


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True