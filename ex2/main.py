import functools


def generate_divisors_of_a_number(number: int):
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            yield i


def generate_all_integers_greater_than_six():
    integer = 6
    while True:
        yield integer
        integer += 1


def print_all_numbers_equals_to_sum_of_their_divisors():
    for i in generate_all_integers_greater_than_six():
        if i == functools.reduce(lambda total, new_div: total + new_div, generate_divisors_of_a_number(i)):
            print(i)


if __name__ == '__main__':
    print_all_numbers_equals_to_sum_of_their_divisors()

