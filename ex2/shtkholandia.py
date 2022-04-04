from typing import IO


def find_special_state(text_file: IO[str]):
    """
    Find the state that all of its characters are in one line in a regular keyboard
    :param text_file: A text file including names of countries in USA
    :return: The name of the country that we can write in one line in the keyboard
    """
    my_set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\n'}
    my_set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n'}
    my_set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', '\n'}

    for my_set_line in [my_set1, my_set2, my_set3]:
        for country in text_file:
            if set(country).intersection(my_set_line):
                return country
        text_file.seek(0)


if __name__ == '__main__':
    with open("resources/states.txt") as my_text_file:
        print(find_special_state(my_text_file))
