#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import even


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game.play(even)


if __name__ == '__main__':
    main()
