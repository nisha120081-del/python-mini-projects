print("wwelcome to the quiz application")

quiz = [
    {"question": "capital of pakistan?", "answers": "Islamabad" },
    {"question": "2 + 2 = ?", "answers": "4" },
    {"question": "Color of sky?", "answers": "blue"},
    {"question": "5 * 3 = ?", "answers": "15"},
    {"question": "Opposite of hot?", "answers": "cold"}
]

score = 0
for i in quiz:
    print(i["question"])
    answer = input("Enter your answer:")
    if answer.lower()==i["answers"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your final score is {score} out of {len(quiz)}")



