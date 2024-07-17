from stanfordkarel import *
import os

def put_5_beepers():
    for i in range(5):
        put_beeper()

def main():
    """ Karel code goes here! """
    for i in range(4):
        put_5_beepers()
        move()
        move()
        move()
        turn_left()

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_06'))