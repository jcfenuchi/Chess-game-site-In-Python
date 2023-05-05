# NÂO CRIADO AINDA :)

import numpy as np
# USAR NUMPY para mapear ???

x = np.array([[50,150,250,350,450,550,650,750]]*8)
y = np.array([[i]*8 for i in [50,150,250,350,450,550,650,750]])
print(x)
print(y)

def Convert_ally_to_enemy(y):
    for array in zip([i for i in [50,150,250,350,450,550,650,750]],[i for i in [750,650,550,450,350,250,150,50]]):
        if y == array[0]:
            print(array[1])
            return array[1]
        
def MovesKnigth(x,y):
    moves = np.array([(x+100,y+200),(x+100,y-200),(x-100,y+200),(x-100,y-200),
    (x-200,y+100),(x-200,y-100),(x+200,y+100),(x+200,y-100)])
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves

def MovesRook(x,y):
    moves = np.array(sum([[(x+100*i,y),(x-100*i,y),(x,y-100*i),(x,y+100*i)] for i in range(8) if i > 0],[]))
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves

def MovesPawn(x,y):
    moves = [(x,y-100)] if y != 650 else [(x,y-100),(x,y-200)]
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves

def MovesKing(x,y):
    moves = np.array([(x-100,y-100),(x,y-100),(x+100,y-100),
            (x-100,y),(x+100,y),(x-100,y+100),(x,y+100),(x+100,y+100)])
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves

def MovesBishop(x,y):
    moves = np.array(sum([[(x+100*i,y-100*i),(x+100*i,y+100*i),(x-100*i,y-100*i),(x-100*i,y+100*i)] for i in range(8) if i > 0],[]))
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves

def MovesQueen(x,y):
    horizontal_moves = np.array(sum([[(x+100*i,y-100*i),(x+100*i,y+100*i),(x-100*i,y-100*i),(x-100*i,y+100*i)] for i in range(8) if i > 0],[]))
    vertical_moves =  np.array(sum([[(x+100*i,y),(x-100*i,y),(x,y-100*i),(x,y+100*i)] for i in range(8) if i > 0],[]))
    moves = np.concatenate((horizontal_moves,vertical_moves))
    possible_moves = np.array([(x,y) for x,y in moves if x > 0 and y > 0 and y < 800 and x < 800])
    return possible_moves
