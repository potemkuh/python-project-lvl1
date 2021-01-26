#!/usr/bin/env python
import prompt
from brain_games import even
from brain_games import cli


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name = cli.welcome_user()
    even.parity_number(name)


if __name__ == '__main__':
    main()
