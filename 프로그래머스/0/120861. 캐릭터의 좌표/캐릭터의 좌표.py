direct = {'left':[-1,0],'right':[1,0],'up':[0,1],'down':[0,-1]}
 
def solution(keyinput, board):
    result = [0,0]
    
    for key in keyinput:
        row, col = direct[key]
        
        newR = result[0] + row
        newC = result[1] + col
        
        if -(board[0]//2)<=newR<=(board[0]//2) and -(board[1]//2)<=newC<=(board[1]//2):
            result[0] = newR
            result[1] = newC
        
    return result