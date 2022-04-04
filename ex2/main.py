import functools
from typing import Iterator


def generate_all_perfect_dividers(divider: int) -> Iterator[int]:
    while True:
        if divider == functools.reduce(lambda total, new_div: total + new_div,
                                       filter(lambda num: divider % num == 0, range(1, divider // 2 + 1))):
            yield divider
        divider += 1


def print_all_dividers_equals_to_sum_of_their_divisors() -> None:
    for perfect_divider in generate_all_perfect_dividers(6):
        print(perfect_divider)


if __name__ == '__main__':
    print_all_dividers_equals_to_sum_of_their_divisors()

