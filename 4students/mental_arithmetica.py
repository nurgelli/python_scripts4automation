import random
import time
import sys


def display_and_sum(count, interval):
    total_sum = 0
    for i in range(count):
        number = random.randint(1,10)
        print(f'{number}')
        total_sum += number
        time.sleep(interval)
        
    return total_sum

def main():
    
    range_inp = input('Please enter count of displaying number: ').strip()
    interval_inp = input('Please enter the interval time between each displaying of numbers: ').strip()
    
    start_inp = input('Are you ready? yes/no: ').strip().lower()
    if start_inp == 'yes':
        time.sleep(4)
        call_func = display_and_sum(int(range_inp), int(interval_inp))
        print(f'Correct answer is: {call_func}')
    else:
        print("Maybe, next time!")
        sys.exit()
  
main()