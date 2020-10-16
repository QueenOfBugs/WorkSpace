
import sys


def print_hello(name):
    """
    say hello to name

    """
    print('hello, ' + name)


if __name__ == '__main__':
    print_hello(sys.argv[1])

