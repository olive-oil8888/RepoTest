'''

'''

quiz = open('Do You Know Your Flowers_ Pop Quiz Python Code Text File.txt', 'r')
quizList = (quiz.read()).split('_')
key = open('ANSWERS Do You Know Your Flowers_ Pop Quiz Python Code Text File.txt', 'r')
keyList = (key.read()).split('_')

#global variables correct and iterate
correct=0
iterate= 0
'''
#make a udf specific to each question. ie for question 2, instead of just saying "incorrect" for b, it would say "unfortunately that is an STD!"
def extra(): 
    special=[]
    special[iterate]
    '''
    
input('\npress any key to start')
if input:
    for x in range(len(quizList)):
        print(quizList[iterate] ,'\n')
        #extra()
        if str(keyList[iterate])==str(input('Your Guess:')):
            print ('correct.')
            correct+=1
        else: print ('incorrect. The correct answer is', keyList[iterate])
        iterate+=1

score=(correct/15)*100
print('thank you for playing. you got', score,'%') 

