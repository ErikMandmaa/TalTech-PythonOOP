"""Swap subwords."""


def swap_subword(s: str, subword: str) -> str:
    """
    If subword exists in s, reverse the first occurrence of s and return the modified string.

    Otherwise return original s.

    Examples:
    swap_subword("abcde", "bc") => "acbde"
    swap_subword("abcabc", "bc") => "acbabc"

    :param s: Original string. Example: "abcde"
    :param subword: Subword to reverse, length > 0. Example: "bc"
    :return: Modified string with the first occurrence of subword reversed, or original string if not found.
    """
    i = s.find(subword)
    if i != -1:
        return s[:i] + subword[::-1] + s[i + len(subword):]
    return s


if __name__ == "__main__":
    print(swap_subword("abcde", "bc"))  # acbde
    print(swap_subword("abcabc", "bc"))  # acbabc
    print(swap_subword("hello", "zz"))  # hello