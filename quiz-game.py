
        
def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the capital of Japan?": "Tokyo",
        "What is the capital of USA?": "Washington DC"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Sorry, the correct answer is", answer)

    print("Your final score is:", score)
    print("Thanks for taking this Critical test")

quiz()
