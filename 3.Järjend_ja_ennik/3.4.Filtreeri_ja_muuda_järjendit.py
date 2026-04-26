"""Filter and modify."""


def filter_and_modify(data: list, threshold) -> list:
    """
    Filter a list of tuples to include only those where the sum of the elements is less than or equal to the given threshold.

    Examples:
    filter_and_modify([(1, 2), (3, 4), (5, 6)], 5) => [(1, 2)]
    filter_and_modify([(1, -2), (-3, 4), (-1, -1)], 1) => [(1, -2), (-3, 4), (-1, -1)]
    filter_and_modify([(0, 2), (1, 5), (2, 7)], 0) => []

    :param data: A list of tuples, where each tuple contains numeric elements. Example: [(1, 2), (3, 4), (5, 6)]
    :param threshold: Maximum allowed sum of tuple elements. Example: 5
    :return: A list of tuples where the sum of elements is less than or equal to the threshold. Example: [(1, 2)]
    """
    result = []

    for tpl in data:
        if sum(tpl) <= threshold:
            result.append(tpl)

    return result


if __name__ == '__main__':
    print(filter_and_modify([(1, 2), (3, 4), (5, 6)], 5))  # [(1, 2)]
    print(filter_and_modify([(1, -2), (-3, 4), (-1, -1)], 1))  # [(1, -2), (-3, 4), (-1, -1)]