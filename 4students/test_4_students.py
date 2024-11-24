import json
import sys
import random

welcome = input('Welcome, are you ready for the test (yes/no): ')
 

if welcome.lower() != 'yes':
    print('Maybe next time!')
    sys.exit()
else:
    try:
        with open('quiz_data.json', 'r') as file:
            data = json.load(file)
        # print('Let\'s jump in!')
        
        def get_quiz():
            questions = data['questions']
            random.shuffle(questions)
            selected_question = questions[:1]
                                    
            for question in selected_question:
                print(f'\n{question['question']}')
                
                for option in question['options']:
                    print(option)
                
                student_answer = input("Your answer (just choice letter): ").strip().upper()
                if student_answer == question['answer']:
                    print('\n Well done!')
                else:
                    print('\n Wrong answer!')                
    except FileNotFoundError:
        print(f'The file was not found')
    except json.JSONDecodeError:
        print("The was an error decoding the JSON")
    except Exception as e:
        print(f'An unexpected error occured: {e}')

file.close()

while True:
    get_quiz()
    retry = input().strip()
    if retry == '':
        print("Pressed Enter! Continuing...")
    elif retry == 'exit':
        print("Exiting the program. Goodby!")
        break
        
