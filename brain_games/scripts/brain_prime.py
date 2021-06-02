#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import prime


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game.play(prime)


if __name__ == '__main__':
    main()
