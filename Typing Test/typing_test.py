import curses
from curses import wrapper

def start_screen(standard_output_screen):
    standard_output_screen.clear()
    standard_output_screen.addstr("Welcome to the Typing Speed Test!")
    standard_output_screen.addstr("\nPress any key to begin!")
    standard_output_screen.refresh()
    key = standard_output_screen.getkey()

def wpm_typing_test(standard_output_screen):
    target_text = "Hello world this is some text for the app!"
    current_text = []

    while True:
        standard_output_screen.clear()
        standard_output_screen.addstr(target_text)

        for char in current_text:
            standard_output_screen.addstr(char, curses.color_pair(1))

        standard_output_screen.refresh()

        key = standard_output_screen.getkey()

        if ord(key) == 27: # Escape key
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
            else:
                current_text.append(key)

def main(standard_output_screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(standard_output_screen)
    wpm_typing_test(standard_output_screen)

wrapper(main)
    