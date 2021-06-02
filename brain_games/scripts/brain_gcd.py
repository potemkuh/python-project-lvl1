#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import gcd


def main():
    print('Find the greatest common divisor of given numbers.')
    start_game.play(gcd)


if __name__ == '__main__':
    main()
