import random

answers = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.",
           "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

random_number = random.randint(1, len(answers))
question = input("Question: ")
print("Answer: " + answers[random_number-1])
