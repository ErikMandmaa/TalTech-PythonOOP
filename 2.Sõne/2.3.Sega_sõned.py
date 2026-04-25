"""Mix string."""


def mix_string(s1: str, s2: str) -> str:
    """
    Given two strings s1 and s2, create a mixed string by alternating between str1 and str2 chars.

    Examples:
    mix_string("AAA", "bbb") -> "AbAbAb"
    mix_string("AA", "") -> "AA"
    mix_string("mxdsrn", "ie tig") -> "mixed string"

    :param s1: The first string. Example: "AAA"
    :param s2: The second string. Example: "bbb"
    :return: A new string created by alternating characters from s1 and s2. Example: "AbAbAb"
    """
    result = []
    max_len = max(len(s1), len(s2))

    for i in range(max_len):
        if i < len(s1):
            result.append(s1[i])
        if i < len(s2):
            result.append(s2[i])

    return ''.join(result)


if __name__ == '__main__':
    print(mix_string("AAA", "bbb"))  # AbAbAb
    print(mix_string("AA", ""))  # AA
    print(mix_string("mxdsrn", "ie tig"))  # mixed string