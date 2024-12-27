import curses
from curses import wrapper

def main(standard_output_screen):
    standard_output_screen.clear()
    standard_output_screen.addstr("Hello world!")
    standard_output_screen.refresh()
    standard_output_screen.getkey()

wrapper(main)
    