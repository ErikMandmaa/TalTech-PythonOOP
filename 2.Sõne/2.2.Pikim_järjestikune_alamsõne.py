"""Find the length of the longest substring of the same symbols."""


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    Examples:
    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("xaaaxbbxccxdxbb") => 3
    max_block("") => 0

    :param s: The input string. Example: "hoopla"
    :return: The length of the largest block of identical adjacent characters. Example: 2
    """
    if not s:
        return 0

    max_len = 1
    current = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current += 1
        else:
            current = 1

        if current > max_len:
            max_len = current

    return max_len


if __name__ == "__main__":
    print(max_block("hoopla"))  # 2
    print(max_block("abbCCCddBBBxx"))  # 3
    print(max_block("xaaaxbbxccxdxbb"))  # 3