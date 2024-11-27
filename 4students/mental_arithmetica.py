import random
import time
import sys




def main():
    
    range_inp = input('Range please: ').strip() 
    start_inp = input('Are you ready? yes/no: ').strip().lower() 
    
    
    def display_and_sum(count, interval):
        total_sum = 0
        for i in range(count):
            number = random.randint(1, int(range_inp))
            print(f'{number}')
            total_sum += number
            time.sleep(interval)
            
        return total_sum
    
    
    if start_inp == 'yes':
        time.sleep(4)
        call_func = display_and_sum(10, 2)
        print(f'Correct answer is: {call_func}')
    else:
        print("Maybe, next time!")
        sys.exit()
        
        
  
main()