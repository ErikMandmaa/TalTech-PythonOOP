"""Get max nums."""


def get_max_nums(nums):
    """
    Return list with maximum numbers from the original list.

    Examples:
    get_max_nums([1, 2, 34, 4, 5, 34, 34]) => [34, 34, 34]
    get_max_nums([-1, -1, -1, -1, -1, -6]) => [-1, -1, -1, -1, -1]
    get_max_nums([3, 4, 5, 6, 3]) => [6]
    get_max_nums([6]) => [6]
    get_max_nums([]) => []

    :param nums: list of integers.
    :return: list of maximum numbers from the original list.
    """
    if not nums:
        return []
    m = max(nums)
    return [x for x in nums if x == m]


if __name__ == '__main__':
    print(get_max_nums([1, 2, 34, 4, 5, 34, 34]))  # [34, 34, 34]
    print(get_max_nums([-1, -1, -1, -1, -1, -6]))  # [-1, -1, -1, -1, -1]
    print(get_max_nums([3, 4, 5, 6, 3]))  # [6]
    print(get_max_nums([6]))  # [6]
    print(get_max_nums([]))  # []