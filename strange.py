import sys
import random

from letters import LETTERS_DICT


class LettersMap:
    def __getitem__(self, item):
        if isinstance(item, int):
            item = chr(item)
        if item in LETTERS_DICT:
            return random.choice(LETTERS_DICT[item])
        elif (upper_item := item.upper()) in LETTERS_DICT:
            return random.choice(LETTERS_DICT[upper_item])
        else:
            return item


def make_it_strange(text: str) -> str:
    return text.translate(LettersMap())


if __name__ == '__main__':
    text = sys.argv[1]
    print(make_it_strange(text))
