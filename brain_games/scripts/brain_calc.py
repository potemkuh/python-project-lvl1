#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import calc


def main():
    print('What is the result of the expression?')
    start_game.play(calc)


if __name__ == '__main__':
    main()
