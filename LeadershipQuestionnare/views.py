import json

# Load questions from JSON file
with open('questions.json') as f:
    questions = json.load(f)

# Load user progress from JSON file
with open('progress.json') as f:
    user_progress = json.load(f)

# Define function to ask questions
def ask_questions():
    # Check if user has completed all questions
    if user_progress['completed']:
        print('You have already completed all the questions. Here are your outcomes:')
        show_outcomes()
        return

    # Check if user has saved progress
    if user_progress['current_question'] > 0:
        print('Welcome back! You have previously completed {} questions out of {}.'.format(
            user_progress['current_question'], len(questions)))
        resume = input('Do you want to resume where you left off? (y/n) ')
        if resume.lower() == 'y':
            question_num = user_progress['current_question']
        else:
            question_num = 0
    else:
        question_num = 0

    # Ask questions and record user answers
    num_correct = 0
    for i in range(question_num, len(questions)):
        question = questions[i]['question']
        answer = questions[i]['answer']
        user_answer = input(question + ' ')
        if user_answer.lower() == answer.lower():
            print('Correct!')
            num_correct += 1
        else:
            print('Incorrect. The correct answer is {}.'.format(answer))

        # Update user progress
        user_progress['current_question'] = i + 1
        user_progress['percent_complete'] = round((i + 1) / len(questions) * 100, 2)

        # Check if user has completed all questions
        if i == len(questions) - 1:
            user_progress['completed'] = True

        # Save user progress after each question
        with open('progress.json', 'w') as f:
            json.dump(user_progress, f)

        # Give user the option to quit after each question
        quit = input('Press q to quit or any other key to continue. ')
        if quit.lower() == 'q':
            break

    # Show outcomes when user has completed all questions
    if user_progress['completed']:
        print('Congratulations! You have completed all the questions. Here are your outcomes:')
        show_outcomes()

# Define function to show outcomes
def show_outcomes():
    # Load outcomes from JSON file
    with open('outcomes.json') as f:
        outcomes = json.load(f)

    # Calculate score and determine outcome
    score = round(num_correct / len(questions) * 100, 2)
    for outcome in outcomes:
        if score >= outcome['min_score']:
            print(outcome['title'])
            print(outcome['description'])
            break

# Start the quiz
ask_questions()

