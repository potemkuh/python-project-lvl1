#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import even


def main():
    start_game.play(even)


if __name__ == '__main__':
    main()
