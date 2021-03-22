#!/usr/bin/env python
from brain_games import start_game
from brain_games.games import prime


def main():
    start_game.play(prime.question_and_answer)



if __name__ == '__main__':
    main()
