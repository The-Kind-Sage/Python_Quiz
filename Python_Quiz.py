questions = [
    {
        "question": "1. What is a correct syntax to output \"Hello World\" in Python?",
        "options": [
            "A. print(\"Hello World\")",
            "B. echo \"Hello World\"",
            "C. echo(\"Hello World\");",
            "D. p(\"Hello World\")"
        ],
        "answer": "A"
    },
    {
        "question": "2. How do you insert COMMENTS in Python code?",
        "options": [
            "A. #This is a comment",
            "B. //This is a comment",
            "C. /*This is a comment*/",
            "D. ##This is a comment"
        ],
        "answer": "A"
    },
    {
        "question": "3. Which method removes whitespace from both beginning and end of a string?",
        "options": [
            "A. trim()",
            "B. ptrim()",
            "C. strip()",
            "D. len()"
        ],
        "answer": "C"
    },
    {
        "question": "4. Which operator is used to compare two values?",
        "options": [
            "A. ><",
            "B. ==",
            "C. <>",
            "D. ="
        ],
        "answer": "B"
    },
    {
        "question": "5. Which collection does not allow duplicate members?",
        "options": [
            "A. List",
            "B. Tuple",
            "C. Dictionary",
            "D. Set"
        ],
        "answer": "D"
    },
    {
        "question": "6. What is the correct file extension for Python files?",
        "options": [
            "A. .pt",
            "B. .pyt",
            "C. .py",
            "D. .python"
        ],
        "answer": "C"
    },
    {
        "question": "7. How do you create a variable with the numeric value 5?",
        "options": [
            "A. x = int(5)",
            "B. int x = 5",
            "C. num x = 5",
            "D. x := 5"
        ],
        "answer": "A"
    },
    {
        "question": "8. Which keyword is used to define a function in Python?",
        "options": [
            "A. function",
            "B. def",
            "C. define",
            "D. func"
        ],
        "answer": "B"
    },
    {
        "question": "9. What does the len() function do?",
        "options": [
            "A. Calculates average",
            "B. Converts value to int",
            "C. Returns the number of characters/items",
            "D. Deletes variable"
        ],
        "answer": "C"
    },
    {
        "question": "10. Which operator is used for exponentiation in Python?",
        "options": [
            "A. ^",
            "B. power",
            "C. **",
            "D. ^^"
        ],
        "answer": "C"
    },
    {
        "question": "11. Which keyword is used to begin a loop in Python?",
        "options": [
            "A. loop",
            "B. repeat",
            "C. for",
            "D. iterate"
        ],
        "answer": "C"
    },
    {
        "question": "12. What is the output of: print(type([]))?",
        "options": [
            "A. <class 'list'>",
            "B. <type 'list'>",
            "C. list",
            "D. <class 'array'>"
        ],
        "answer": "A"
    },
    {
        "question": "13. Which module in Python is used to generate random numbers?",
        "options": [
            "A. math",
            "B. random",
            "C. numbers",
            "D. randint"
        ],
        "answer": "B"
    },
    {
        "question": "14. What symbol is used to start a code block in Python?",
        "options": [
            "A. {",
            "B. (",
            "C. :",
            "D. ->"
        ],
        "answer": "C"
    },
    {
        "question": "15. Which statement is used to handle exceptions?",
        "options": [
            "A. except",
            "B. error",
            "C. try/except",
            "D. catch"
        ],
        "answer": "C"
    }
]

score = 0
print("\n──────────────────────")
print("    📘 Python Quiz ")
print("──────────────────────\n")

for i in questions:
    print(i["question"])
    for option in i["options"]:
        print(option)
    answer = input("\nYour answer (A, B, C, D): ").strip().upper()

    while answer not in ["A", "B", "C", "D"]:
        answer = input("❌ Invalid input. Choose A, B, C, or D: ").strip().upper()

    if answer == i["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {i['answer']}.\n")

print("────────────────────────────────────────────")
print(f"🏁 QUIZ COMPLETE! Your final score is: {score} / {len(questions)}")
