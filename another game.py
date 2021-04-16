import time
import functools
import operator
import random
import math

print('Super Fun and Simple Math quiz!')
time.sleep(2)
print('Answer the multiplication questions before time runs out!')
print('Timer is set to 10 seconds')
time.sleep(3)
print('Ready? Go!')
start_time = time.time()

score = 0

#Logic, I decided to use while loops since i find them simpler to work with. To discuss code during meeting

while True:
    difficulty_setting = 2
    difficulty_progression = math.floor(score/10)
    overall_difficulty = difficulty_setting + difficulty_progression

#using random number from between 1 and 9 to make it less predictable. 

    numbers_list = []
    for x in range(overall_difficulty):
        value = random.randint(1,9)
        numbers_list.append(value)

    answer = functools.reduce(operator.mul, numbers_list, 1)
    print('Multiply these numbers', numbers_list)

    guess = int(input())

    if guess == answer:
        score = score + (1 * overall_difficulty)
        continue

    else:
        print('Game over! The answer was', answer)
        elapsed_time = time.time() - start_time
        print('Your score was', score, 'In only', elapsed_time)
        break

