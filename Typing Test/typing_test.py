import curses
from curses import wrapper

def main(standard_output_screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    standard_output_screen.clear()
    standard_output_screen.addstr("Hello world!", curses.color_pair(1))
    standard_output_screen.refresh()
    standard_output_screen.getkey()

wrapper(main)
    