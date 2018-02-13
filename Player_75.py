
def Action(player, other_1, other_2):
    
    if other_1 and other_2:
        player1 = 0
        player2 = 0
        for i in other_1:
            if not i:
                player1 += 1
                
        for j in other_2:
            if not j:
                player2 += 1
                
        if(player1 >= 2 or player2 >= 2):
            if(not other_1[-1] or not other_2[-1]):
                return False
        
    return True
