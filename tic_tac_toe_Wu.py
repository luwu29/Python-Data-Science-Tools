#how to reset variables

import sys

player1=[]
player2=[]

win_list2=[['A1','A2','A3'], ['B1','B2','B3'], ['C1','C2','C3'],
     ['A1','B2','C3'], ['C1','B2','A3'],['A2','B2','C2']]

        
        
def winning():
    for i in win_list2:
        result1=all(elem in player1 for elem in i)
        result2=all(elem in player2 for elem in i)
        if result1 or result2:
            print("YOU WIN!")
            sys.exit(0)
    
        else:
            continue


        
        
        
comp_list=['A1','A2','A3', 'B1','B2','B3', 'C1','C2','C3',
     'A1','B2','C3', 'C1','B2','A3']


def meet_condition_player1(x): 
    while x not in comp_list or x in player1+player2:
        print('Pick a position that has not been taken from {}, please!'.format(comp_list))
        x =input('Try again: ')
    while x in comp_list and x not in player1+player2:
        player1.append(x)
        break   
        
def meet_condition_player2(x):
    while x not in comp_list or x in player1+player2:
        print('Pick a position that has not been taken from {}, please!'.format(comp_list))
        x =input('Try again: ')
    while x in comp_list and x not in player1+player2:
        player2.append(x)
        break
    
    
def tic():
    player1=[]
    player2=[]
    p1_1=input('Player 1 put down a position: ')
    meet_condition_player1(p1_1)
    p2_1=input('Player 2 put down a position: ')
    meet_condition_player2(p2_1)
    p1_2=input('Player 1 put down a position: ')
    meet_condition_player1(p1_2)
    p2_2=input('Player 2 put down a position: ')
    meet_condition_player2(p2_2)
    p1_3=input('Player 1 put down a position: ')
    meet_condition_player1(p1_3)
    #check for winning
    winning()
    p2_3=input('Player 2 put down a position: ')
    meet_condition_player2(p2_3)
    winning()
    p1_4=input('Player 1 put down a position: ')
    meet_condition_player1(p1_4)
    winning()
    p2_4=input('Player 2 put down a position: ')
    meet_condition_player2(p2_4)
    winning()
    p1_5=input('Player 1 put down a position: ')
    meet_condition_player1(p1_5)
    winning()
    print('Tie!')
    
tic()
        