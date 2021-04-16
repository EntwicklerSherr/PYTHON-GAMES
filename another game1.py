import time
import functools
import operator
import random
import math

print('Super Fun and Simple Math quiz!')
time.sleep(2) #There will be 2 second pause before next line 
print('Answer the multiplication questions before time runs out!')
print('Timer is set to 10 seconds')
time.sleep(3) #There will be 3 second pause before next line 
print('Ready? Go!')
start_time = time.time()  #This will be time stamp for when user begins game

score = 0 #When user get correct answer, 7

#Logic, I decided to use while loops since i find them simpler to work with. To discuss code during meeting

while True:


    numbers_list = []
    for x in range(2):
        value = random.randint(1,9)
        numbers_list.append(value)3
        

    answer = functools.reduce(operator.mul, numbers_list, 1)
    print('Multiply these numbers', numbers_list)

    guess = int(input())

    if guess == answer:
        score = score + (1 )
        continue

    else:
        print('Game over! The answer was', answer)
        elapsed_time = time.time() - start_time
        print('Your score was', score, 'In only', elapsed_time)
        break

