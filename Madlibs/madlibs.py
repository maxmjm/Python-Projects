with open("story.txt", "r") as file:
    story = file.read()

words_in_file = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words_in_file.add(word)
        start_of_word = -1
