print("Hello Seniors")
print("Jai Hind Everyone")
print("Welcome To The Quiz Wizard")
question_bank = [
    {"text": "Which symbol is used to denote a single-line comment in Python?", "answer": "C"},
    {"text": "Which of the following is the correct way to declare a variable and assign the integer value 10 to it in Python?", "answer": "C"},
    {"text": "Which of the following is a mutable data type in Python?", "answer": "A"},
    {"text": "What keyword is used to define a function in Python?", "answer": "B"},
    {"text": "What does the len() function return when applied to a list [1, 2, 3, 4]?", "answer": "B"},
    {"text": "Which of the following statements about Python indentation is true?", "answer": "D"},
    {"text": "What is the purpose of the input() function in Python?", "answer": "A"}
]
options = [
    ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
    ["A. int x = 10;", "B. x := 10;", "C. x = 10", "D. var x = 10;"],
    ["A. lists", "B. tuple", "C. str (String)", "D. int (Integer)"],
    ["A. function", "B. def", "C. func", "D. define"],
    ["A. 1", "B. 4", "C. 3", "D. 0"],
    [
        "A. Indentation is optional and used for readability only.",
        "B. Indentation is handled automatically by the interpreter and doesn't need explicit attention.",
        "C. Indentation is only required for loops and conditional statements.",
        "D. Indentation is used to define code blocks and is mandatory."
    ],
    [
        "A. To read input from the user via the console.",
        "B. To display output on the console",
        "C. To convert a string to an integer.",
        "D. To perform mathematical calculations."
    ]
]
def checking(guess, correct):
    if guess == correct:
        return True, "Boom! You nailed it!"
    else:
        return False, " Better luck next time!"
score = 0
for q in range(len(question_bank)):
    print(f"\nQ{q+1}: {question_bank[q]['text']}")
    
    for opt in options[q]:
        print(opt)
    
    answer = input(" \nBlast off with your choice (A/B/C/D): ").upper()
    
    correct = question_bank[q]["answer"]
    is_correct, message = checking(answer, correct)
    
    print(message)
    
    if is_correct:
        score += 1
print(f"\n Quiz Over! Your final score is {score}/{len(question_bank)}")
