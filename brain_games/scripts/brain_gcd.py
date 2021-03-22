#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import gcd


def main():
    start_game.play(gcd.question_and_answer)


if __name__ == '__main__':
    main()
