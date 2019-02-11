import random
import time

def intro():
    print('Welcome to QuizTEP')
    print('QuizTEP is a knowledge game in which two players are participating.')
    print('Game rules:\nEach player selects two of the five categories.')
    print('In every category, player must answer three questions.\nThe player with the most correct answers wins.')
    print('IMPORTANT NOTE:Use only digits to choose which category you want to play or to choose your answer.In case you will use letter the game it\'s gonna stop working')
    print('Good luck, Have Fun!!')
#--------Player Input---------#
def playername(name): 
    playername=input('Player {} enter your name.\nUsername:'.format(name))
    return playername

#----------Importing the texts--------#
def pickRandomQuestion(category):
        f=open(category + ".txt","r")
        contents =f.readlines()
        # print(contents)
        questionList = []
        for i in range(0, len(contents), 6):
                questionList.append([contents[i],contents[i+1],contents[i+2],contents[i+3],contents[i+4],contents[i+5]])


     



        # ------------ choose a random question to ask player --------------#
    
        turn = 0
        correct = 0
        while turn <= 2:
            rand = random.randint(0, len(questionList)-1)

            print(questionList[rand][0])
            for i in range(1, 5):
                    print( str(i) + '. ' + questionList[rand][i])

            answer = int(input('Answer: '))
            

            # check if answer is correct

            if answer == int(questionList[rand][5]):
                    print('Correct!')
                    correct = correct + 1
            else:
                    print('Wrong!')

            questionList.pop(rand)
            turn = turn + 1
        
        return correct


             
#------------Choosing Category-------------#
def chooseCategory(name,categoryList): #sunartisi(parametroi)
    print('\n{} it\'s your turn to choose a category:'.format(name))
    while True:                                                  #while wste na epanalamvanei tin diadikasia se periptwsh la8os input tou xrhsth
        for i in range(0,len(categoryList)):                     #len= mikos listas(posa stoixeia exei 0,1,2,3,4)
                print (str(i+1) + '. ' + categoryList[i]) #
        
        selectedCat=int(input('Your pick: ')) 
        stop=len(categoryList)+1                              #stop=metavliti opou auksanoume to mikos tis listas apo 5 stoixeia se 6
        x=range(1,stop)                                       #x=metavliti opou dilonoume tin sunartisi range kai san parametrous to 1(pou ksekinaei h lista)kai stop diladi 6
        chosenCategory=list(x)                                #chosencategory metavliti h opoia dimiourgoume mia lista opou vazoume tin metavliti "x"

        if (selectedCat in chosenCategory):
                               
                if (len(categoryList)>1):                        #vazoume mikos listas stin periptwsi pou menei 1 stoixeio na min ektupwnei to print)
                        
                    category = categoryList[selectedCat-1]
                    categoryList.pop(selectedCat-1)               #diagrafoume apo tin lista to stoixeio pou dialekse o xrhsths                                     
                    return category
                
                
        else:
                print('Invalid answer.Please choose again')
        
#------------Timer-----------#
def timeStamp():

    timer = time.time()
    return timer
 
 
#------------MAIN-----------#
def main():
    categoryList=['Geography', 'History', 'Cinema', 'Technology','Music']
    
    p1Correct = 0
    p2Correct = 0
    
    intro()
   
    player1name = playername("1")  #metavliti-player1name & playername("1")sunartisi(parametros)
   
    player2name = playername("2")
   
    category = chooseCategory(player1name,categoryList)
    
    p1Timer_a = timeStamp()
    p1Correct = pickRandomQuestion(category)
    p1Timer_a = timeStamp() - p1Timer_a

    category = chooseCategory(player2name,categoryList)

    p2Timer_a = timeStamp()
    p2Correct = pickRandomQuestion(category)
    p2Timer_a = timeStamp() - p2Timer_a
    
    category = chooseCategory(player1name,categoryList)
    
    p1Timer_b = timeStamp()
    p1Correct = pickRandomQuestion(category) + p1Correct
    p1Timer_b = timeStamp() - p1Timer_b

    category = chooseCategory(player2name,categoryList)

    p2Timer_b = timeStamp()
    p2Correct = pickRandomQuestion(category) + p2Correct
    p2Timer_b = timeStamp() - p2Timer_b
    
    p1Time = int(p1Timer_a + p1Timer_b)
    p2Time = int(p2Timer_a + p2Timer_b)
    
    print('{} correct answers: {}. Time:  {}  seconds'.format(player1name,p1Correct,p1Time))
    print('{} correct answers: {}. Time:  {}  seconds'.format(player2name,p2Correct,p2Time))

    if(p1Correct > p2Correct):
        print('{} is the winner with {} correct answers'.format(player1name,p1Correct))
        print('Total time:{} seconds.'.format(p1Time))
    elif(p2Correct > p1Correct):
        print('{} is the winner with {} correct answers'.format(player2name,p2Correct))
        print('Total time:{} seconds.'.format(p2Time))
    else:
        print('Players have same amount of correct answers.\nThe player with the best time wins.')
        if p1Time < p2Time:
            print('{} is the winner with {} correct answers'.format(player1name,p1Correct))
            print('Total time:{} seconds.'.format(p1Time))
        elif p2Time < p1Time:
            print('{} is the winner with {} correct answers'.format(player2name,p2Correct))
            print('Total time:{} seconds.'.format(p2Time))
        else:
            print('It\'s a draw')


    
main()
