import curses
from curses import wrapper
import time

def start_screen(standard_output_screen):
    standard_output_screen.clear()
    standard_output_screen.addstr("Welcome to the Typing Speed Test!")
    standard_output_screen.addstr("\nPress any key to begin!")
    standard_output_screen.refresh()
    key = standard_output_screen.getkey()

def display_text(standard_output_screen, target, current, wpm = 0):
    standard_output_screen.addstr(target)
    standard_output_screen.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        colour = curses.color_pair(1)
        if char != correct_char:
            colour = curses.color_pair(2)

        standard_output_screen.addstr(0, i, char, colour)

def wpm_typing_test(standard_output_screen):
    target_text = "Hello world this is some text for the app!"
    current_text = []
    wpm = 0
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        standard_output_screen.clear()
        display_text(standard_output_screen, target_text, current_text, wpm)
        standard_output_screen.refresh()

        key = standard_output_screen.getkey()

        if ord(key) == 27: # Escape key
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(standard_output_screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(standard_output_screen)
    wpm_typing_test(standard_output_screen)

wrapper(main)
    