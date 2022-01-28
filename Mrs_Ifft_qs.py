# Title
print("\nWelcome to the Mr.s Ifft questionnaire!")

# opening the file
questionnaire_file = open('Mrs_Ifft_qs.txt', 'w')

# Questions
questionnaire_simple_questions = [
    "Whats your favorite project you've coded?",
    "Do you enjoy teaching at parker?",
    "What class do you enjoy teaching the most?",
    "What are some of your hobbies?",
]

# Adding to the file
for question in questionnaire_simple_questions:
    print("\n" + question)
    answer = input("Please answer here: ")
    questionnaire_file.write(question + "\n\n")
    questionnaire_file.write(answer + "\n\n\n")
