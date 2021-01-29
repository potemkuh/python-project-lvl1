#!/usr/bin/env python
from brain_games.games import gcd
from brain_games import cli


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name = cli.welcome_user()
    gcd.game_nod(name)


if __name__ == '__main__':
    main()
