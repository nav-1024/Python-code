import random as rm

def playGame():
    com_choice = ['rock','paper','scissor']
    lives = 0
    your_score = 0
    com_score = 0

    while lives<5:
        your_choice = input('Enter your choice : ').lower()
        rc = rm.choice(com_choice)
        if your_choice =='rock' or your_choice == 'paper' or your_choice =='scissor':
            if rc==your_choice :
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
            elif rc == 'rock' and your_choice == 'paper':
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                your_score = your_score+1
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
                lives = lives+1
            elif rc == 'rock' and your_choice == 'scissor':
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                com_score = com_score+1
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
                lives = lives+1
            elif rc == 'paper' and your_choice=='rock':
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                com_score = com_score+1
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
                lives = lives+1
            elif rc == 'paper' and your_choice=='scissor':
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                your_score = your_score+1
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
                lives = lives+1
            elif rc == 'scissor' and your_choice=='rock':
                print('Your Choice:',your_choice,'& Computer Choice:',rc)
                your_score = your_score+1
                print('Your Score:',your_score)
                print('Computer_score:',com_score)
                lives = lives+1
        else:
            print('Invalid input please enter your choice ')
        
    if your_score == com_score:
        print("Both Won, Match Tie")
    elif your_score > com_score:
        print("You won with:",your_score,"Points")
    elif your_score < com_score:
        print("Computer won with:",com_score,"Points")
        
            
playGame()