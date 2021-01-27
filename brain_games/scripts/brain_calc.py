#!/usr/bin/env python
from brain_games import cli
from brain_games.games import calc


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name = cli.welcome_user()
    calc.calculator(name)


if __name__ == '__main__':
    main()
