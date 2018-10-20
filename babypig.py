import random

questions =[
    'how old are you?',
    'were are you from?',
    'were is your mom?'
]
question = random.choice(questions)
answer = input (question).strip().lower

while answer != 'just because':
    answer = input('why?').strip().lower()



