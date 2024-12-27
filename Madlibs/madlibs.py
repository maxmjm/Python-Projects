with open("story.txt", "r") as file:
    story = file.read()

words_in_file = set()
start_of_word = -1

target_start = "<"
target_end = ">"
