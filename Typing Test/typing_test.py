import curses
from curses import wrapper

def start_screen(standard_output_screen):
    standard_output_screen.clear()
    standard_output_screen.addstr("Welcome to the Typing Speed Test!")
    standard_output_screen.addstr("\nPress any key to begin!")
    standard_output_screen.refresh()
    key = standard_output_screen.getkey()


def main(standard_output_screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(standard_output_screen)

wrapper(main)
    