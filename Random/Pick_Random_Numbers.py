import random

print(random.randint(0,10)) # De la 0 la 10 incluzand 0 si 10

answer = random.randint(1,3)

if answer == 0:
    print (f'Answer is {answer}, which is not 0')

if answer == 1:
    print (f'Answer is {answer}, which is Yes')

if answer == 2:
    print (f'Answer is {answer}, which is Maybe')