q1 = print('1) What is the nickname of the richest cybersportsman in the world?')
q2 = print('2) What pillow loses every morning and gets it back every night?')
q3 = print('3) Where the sun comes from?')

def play_game():
    zvezdochki = []
    answer = 'answer'
    q_choose = input('Which question u want to play with? (1/2/3):   ')
    
    if q_choose == '1':
        answer = 'NoTail'
        
    elif q_choose == '2':
        answer = 'Head'
        
    elif q_choose == '3':
        answer = 'East'
        
    for i in range(len(answer)):
        zvezdochki.append('*')
    
    answer_low = answer.lower()

    print(*zvezdochki)

    l_or_a = input('by letters(3 attempts) or whole anwer(1 attempt only)? (select 1/2) ')  # letter or answer
    
    br = True
    x = 3

    if l_or_a == '1':
        while br:
            
            br2 = True
            letter = input('pls enter a letter: ')
            
            for i in range(len(zvezdochki)):
                
                if letter == answer_low[i]:
                    zvezdochki[i] = letter
                    print('Well done! here is the result:', *zvezdochki)
                    if zvezdochki == list(answer_low):
                        print('Gratz, u won! ', answer)
                        br = False  
                
            
            
            if letter not in answer_low:
                
                x -= 1

                if x == 0:
                    print('u lost')
                    br = False    
                else:
                    pass
                print(f'{x} attempts left')  
                    

        

    elif l_or_a == '2':
        while True:
            
            answ = input('pls enter ur answer: ')
            if answ == answer_low:
                print('gratz, u won!!!')
                break
            elif answ != answer_low:
                print('u lost ,_,')
                
                break

def again():
    br = True
    while br:
        a = input('wanna play again? y/n: ')
        if a =='y':
            play_game()
        if a == 'n':
            br = False
            
play_game()
again()