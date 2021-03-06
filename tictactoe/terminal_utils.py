'''
ANSI Codes Reference https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
'''

import sys
import time


def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def print_error(msg):
    write(f"\033[31m{msg}\033[0m")
    time.sleep(2)
    write("\033[2K\r")


def print_info(msg):
    write(msg)
    time.sleep(3)
    write("\033[2K\r")


def print_win(player):
    write(f"๐ฅPlayer \033[32m{player}\033[0m Wins!๐\n\n")


def print_tie():
    write(f"๐\033[33mGame Tied\033[0m๐\n\n")
