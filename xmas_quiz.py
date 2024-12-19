print("Merry Christmas!")

start_quiz = input("Do you want to start the quiz? ")
if start_quiz.lower() != "yes":
    print("Exiting program!")
    quit()
else:
    print("Okay! Let's go!")

score = 0
num_questions = 3