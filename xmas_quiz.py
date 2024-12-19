print("Merry Christmas!")

start_quiz = input("Do you want to start the quiz? ")
if start_quiz.lower() != "yes":
    print("Exiting program!")
    quit()
else:
    print("Okay! Let's go!")

score = 0
num_questions = 3

answer = input("What is the name of the reindeer that leads Santa's sleigh? ")
if answer.lower() == "rudolph":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input('In "The Polar Express", Tom Hanks played how many roles? ')
if answer.lower() == "6" or answer.lower() == "six":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What traditional Christmas decoration is actually a parasitic plant? ")
if answer.lower() == "mistletoe":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percentage = round((score / num_questions) * 100, 2)
print("You scored " + str(score) + "/" + str(num_questions) + " (" + str(percentage) + "%)")