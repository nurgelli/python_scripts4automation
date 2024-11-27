import random
import time
import sys


def main():
    
    type_game = input('Enter type of calculation 1 for addition, 2 for subtraction: ')
    range_inp = input('Enter the range like (1-?): ').strip() 
    inter_inp = input('Time interval each displays: ').strip() 
    start_inp = input('Are you ready? yes/no: ').strip().lower()
    
    # if type_game != 1 | 2:
    #     print("Please enter 1 or 2: ")
    # elif range_inp != int():
    #     print("Please enter digit: ")
    # elif inter_inp != int():
    #     print("Please enter digit: ")
        
        
    
    def display_and_sum(count, interval):
        total_sum = 0
        for i in range(count):
            number = random.randint(1, int(range_inp))
            print(f'\n{number}')
            if int(type_game) == 1:
                total_sum += number
            elif int(type_game) == 2:
                total_sum -=number
            time.sleep(interval)
            
        return total_sum
    
    if start_inp == 'yes':
        time.sleep(4)
        call_func = display_and_sum(10, int(inter_inp))
        time.sleep(5)
    else:
        print("Maybe, next time!")
        sys.exit()
        
    print(f'Correct answer is: {call_func}')
        
  
main()