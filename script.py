# ExamTopic Answer Parser - script.py - 29/01/2022

import re
import random

raw = open("./raw.txt").read()
raw = raw.replace("\n", "")
raw = re.split(r"Question+", raw)

questions = []

for item in raw:
    question = {}

    # Get question number
    questionNumber = re.findall("#[0-9]*", item)
    if questionNumber != []:
        question["number"] = questionNumber[0]

    # Get question body
    questionBody = re.findall("(?<=Topic 1).*(?=A\.)", item)
    if questionBody != []:
       question["body"] = questionBody[0].strip()

    # Get Choices
    questionChoices = re.findall("(?=A\.).*(?=Correct Answer)", item)
    if questionChoices != []:
        questionChoices = re.split("(?=[\s][A-Z]\.)", questionChoices[0])
        questionChoices = [choice.strip() for choice in questionChoices]
        question["choices"] = questionChoices

    # Get answer
    questionAnswer = re.findall("(?<=Correct Answer: ).*[A-Z]", item)
    if questionChoices != []:
        question["answer"] = questionAnswer[0]

    questions.append(question)

# Shuffle questions
random.shuffle(questions)
numberOfQs = int(input("How many questions would you like to do?: "))
score = 0

for x in range (0, numberOfQs):
    print("\n"*100)
    print("""
{}/{} ({}).

{}\n""".format(x + 1, numberOfQs, questions[x]["number"], questions[x]["body"]))

    for choice in questions[x]["choices"]:
        print(choice)
    
    answer = input("\n> ")

    print("\n"*100)
    for choice in questions[x]["choices"]:
        print(choice)
    print("""\n
Your input: {}
Correct Answer: {}
    """.format(answer.upper(), questions[x]["answer"]))

    userNext = input("\n(Press enter to continiue)")

    if answer.upper() == questions[x]["answer"]:
        score += 1

percent = (score/numberOfQs)*100
if percent >= 80:
    status = "PASSED"
else:
    status = "FAILED"

print("\n"*100)
print("""
Score: {}/{}
Percent: {}
Status: {}""".format(score, numberOfQs, percent, status))

