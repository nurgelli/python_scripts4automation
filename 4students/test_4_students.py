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
        for q in data.values():
            random_questions = random.sample(q, 1)
        print(random_questions)
    except FileNotFoundError:
        print(f'The file was not found')
    except json.JSONDecodeError:
        print("The was an error decoding the JSON")
    except Exception as e:
        print(f'An unexpected error occured: {e}')



file.close()