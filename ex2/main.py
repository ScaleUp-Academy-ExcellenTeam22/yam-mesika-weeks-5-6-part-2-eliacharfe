import functools
from typing import Iterator


def generate_all_perfect_dividers(divider: int = 2) -> Iterator[int]:
    """
    Generator that generates all positive integers greater(or equals) to the integer passed to
    the function, that the sum of their divisors are equals to them ("perfect dividers").
    :param divider: The start integer
    :return: An iterator of the "perfect dividers"
    """
    while True:
        if divider == functools.reduce(lambda total, new_div: total + new_div,
                                       filter(lambda num: divider % num == 0, range(1, divider // 2 + 1))):
            yield divider
        divider += 1


def print_all_dividers_equals_to_sum_of_their_divisors() -> None:
    """
    Print all positive integers that the sum of their divisors are equals to them
    """
    for perfect_divider in generate_all_perfect_dividers(6):
        print(perfect_divider)


if __name__ == '__main__':
    print_all_dividers_equals_to_sum_of_their_divisors()
