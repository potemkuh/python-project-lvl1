#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import progression


def main():
    print('What number is missing in the progression?')
    start_game.play(progression)


if __name__ == '__main__':
    main()
