questions_file = open('questions.txt', 'r')
questions = questions_file.read().splitlines()
questions_file.close()

answers = []
user_answers = []
user_score = 0
for counter, question in enumerate(questions):
    answers.append(question.split("=")[1])
    current_question = question.split("=")[0]
    user_answer = input(f"{current_question}=")
    user_answers.append(user_answer)
    if user_answer == answers[counter]:
        user_score = user_score + 1

result_file = open('result.txt', 'w')
result_file.write(f"Your final score is {user_score}/{len(answers)}.")
result_file.close()