#!/usr/bin/env python
from brain_games.games import prime
from brain_games import cli


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    name = cli.welcome_user()
    prime.game_prime(name)


if __name__ == '__main__':
    main()
