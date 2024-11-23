import json
import sys
import random


welcome = input('Welcom, are you ready for the test (yes/no): ')
 

if welcome.lower() != 'yes':
    print('Maybe next time!')
    sys.exit()
else:
    try:
        with open('quiz_data.json', 'r') as file:
            data = json.load(file)
        print('Let\'s jump in!')
        
        def get_quiz():
            questions = data['questions']
            random.shuffle(questions)
            selected_question = questions[:1]
            score = 0
            for question in selected_question:
                print(question['question'])
                for option in question['options']:
                    print(option)
                student_answer = input("Your answer (just enter the Letter): ").strip().upper()
                if student_answer != question['answer']:
                    print('Wrong answer, try again!')
                    sys.exit()
                else:
                    print("Well done!")
                    score += 1
                    
                
            print(f'Your score: {score}/1')
    except FileNotFoundError:
        print(f'The file was not found')
    except json.JSONDecodeError:
        print("The was an error decoding the JSON")
    except Exception as e:
        print(f'An unexpected error occured: {e}')

while True:
    get_quiz()

file.close()