#06-09-24
#Animal trivia quiz
import time as t
print('Welcome to daily animal trivia!!')
playing=input('Do you wanna play? y/n?')
if playing.lower() == 'y':
    print('Okay, lets play!! :)')
else:
    print('Okay, maybe some other time!')
    exit()
score=0
n=0
#1st question
answer=input('What is the largest mammal in the world? ')
if answer.lower()== 'blue whale':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#2nd question
answer=input('Which bird is known for its impressive courtship dance and is native to New Guinea? ')
if answer.lower()== 'bird of paradise':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#3rd question
answer=input('What type of animal is a Komodo dragon? ')
if answer.lower()== 'lizard':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#4th question
answer=input('What is the fastest land animal in the world? ')
if answer.lower()== 'cheetah':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#5th question
answer=input('How many hearts does an octopus have? ')
if answer.lower()== 'three':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#6th question
answer=input('What is the only mammal capable of true flight? ')
if answer.lower()== 'bat':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#7th question
answer=input('Which animal is known to have the longest lifespan in the wild? ')
if answer.lower()== 'tortoise':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#8th question
answer=input('What is the primary diet of a giant panda? ')
if answer.lower()== 'bamboo':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#9th question
answer=input('Which marine animal is known for its ability to change color and blend into its surroundings? ')
if answer.lower()== 'octopus':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

#10th question
answer=input('What kind of animal is the largest member of the weasel family? ')
if answer.lower()== 'wolverine':
    print('Correct!')
    score+=1
    n+=1
else:
    print('Incorrect!')
    n+=1

if score >= 7:
    print('YOUR SCORE: ' + str(score) + ' PERCENTAGE: ' + str((score/n) * 100) +'% '+ 'Great Job! :)' )
elif score >= 4:
    print('YOUR SCORE: ' + str(score) + ' PERCENTAGE: ' + str((score/n) * 100) +'% '+ 'Could Be Better :/' )
else:
    print('YOUR SCORE: ' + str(score) + ' PERCENTAGE: ' + str((score/n) * 100) +'% '+ 'You Need Some Work :(' )

