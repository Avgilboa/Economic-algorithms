import doctest

##Run on the terminal -  python -m doctest -v weighted_round_robin.py

def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    
    """" 
    Test diffrent situations:
    
    rights = [1,2,4]
    valuations = [[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y = 0.5
    TEST 1:
    ROUND 1: 
            player 0    player 1    player 2
    rights      2           4           8
            Player 3 win and take item(4) value: 66
    num items:  0           0           2
    
    ROUND 2: 
            player 0    player 1    player 2
    rights      2           4          2.66
            Player 1 win and take item(3) value: 55
    num items:  0           1           1
    
    ROUND 3: 
            player 0    player 1    player 2
    rights      2           1.33       2.66
            Player 2 win and take item(1) value: 33
    num items:  0           1           2
    
    ROUND 4: 
            player 0    player 1    player 2
    rights      2         1.33         1.6
            Player 0 win and take item(2) value: 22
    num items:  1           1           2
    
    ROUND 5: 
            player 0    player 1    player 2
    rights    0.66        1.33         1.6
            Player 2 win and take item(0) value: 11
    num items:  1           1           3
    
    >>> weighted_round_robin([1,2,4], [[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]], 0.5)
    {0: {'player': 2, 'item_number': 4, 'value': 66}, 1: {'player': 1, 'item_number': 3, 'value': 55}, 2: {'player': 2, 'item_number': 1, 'value': 33}, 3: {'player': 0, 'item_number': 2, 'value': 22}, 4: {'player': 2, 'item_number': 0, 'value': 11}}
    
    TEST 2: - Jefreson algo (same value of each item different rights):
    
    rights = [40,135,325]
    valuations = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
    y = 1
    ROUND 1: 
            player 0    player 1    player 2
    rights    40           135         325
            Player 3 win and take one item(0)
    num items:  0           0           1
    
    ROUND 2: 
            player 0    player 1    player 2
    rights:  40           135         162.5
            Player 3 win and take one item(1)
    num items:  0           0           2
    
    ROUND 3: 
            player 0    player 1    player 2
    rights:   40           135        108.33
            Player 1 win and take one item(2)
    num items:  0           1           2
    
    ROUND 4: 
            player 0    player 1    player 2
    rights:   40          67.5        108.33
            Player 2 win and take one item(3)
    num items:  0           1           2
    
    ROUND 5: 
            player 0    player 1    player 2
    rights:   40          67.5        80.25
            Player 2 win and take one item(4)
    num items:  0           1           3
    
    >>> weighted_round_robin([40,135,325], [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], 1)
    {0: {'player': 2, 'item_number': 0, 'value': 1}, 1: {'player': 2, 'item_number': 1, 'value': 1}, 2: {'player': 1, 'item_number': 2, 'value': 1}, 3: {'player': 2, 'item_number': 3, 'value': 1}, 4: {'player': 2, 'item_number': 4, 'value': 1}}


    TEST 3: - (same value of each item and same rights):
    
    rights = [1,1,1]
    valuations = [[1,1,1], [1,1,1], [1,1,1]]
    y = 0.3
   
   Each round random player (in my code is order with index logic) take item and his value will be : value / 0.3 + num_of_items
    
    >>> weighted_round_robin([1,1,1], [[1,1,1], [1,1,1], [1,1,1]], 0.3)
    {0: {'player': 0, 'item_number': 0, 'value': 1}, 1: {'player': 1, 'item_number': 1, 'value': 1}, 2: {'player': 2, 'item_number': 2, 'value': 1}}

    EST 4: - (different value of each item and same rights):
    rights = [100,100,100]
    valuations = [[10,21,1], [30,19,1], [21,19,13]]
    y = 0.5
    
    ROUND 1: 
            player 0    player 1    player 2
    rights    100         100        100
            Equal - my algorithem will choose player 0 to start and he will take item(1)
    num items:  1           0           0
    
    ROUND 2: 
            player 0    player 1    player 2
    rights   66.66         100        100
            Equal(1,2) - my algorithem will choose player 1 to start and he will take item(0)
    num items:  1           1           0
    ROUND 2: 
            player 0    player 1    player 2
    rights   66.66       66.66        100
            player 2 wins and take the item that remain(2)
    num items:  1           1           1
    >>> weighted_round_robin([100,100,100], [[10,21,1], [30,19,1], [21,19,13]], 0.5)
    {0: {'player': 0, 'item_number': 1, 'value': 21}, 1: {'player': 1, 'item_number': 0, 'value': 30}, 2: {'player': 2, 'item_number': 2, 'value': 13}}
    """
    num_players = len(valuations)
    num_items = len(valuations[0])
    items_for_player = [0] * num_players
    
    ans ={}
    
    
    for num_round in range(num_items):
        value_of_calc, index_turn = find_turn(rights, y , items_for_player)
        
        items_for_player[index_turn] += 1
        
        max_index, max_value_item = max(enumerate(valuations[index_turn]) , key= lambda x : x[1])
        
        # print(f"player {index_turn} takes item {max_index} with value {max_value_item}")
        
        ans[num_round] = {
            "player": index_turn ,
            "item_number": max_index,
            "value": max_value_item
        }
        
        for list_player in valuations:
            list_player[max_index] = 0
        
    print(ans)
        
            
        
def find_turn(rights, y, item_player):
    max_value, max_index = float('-inf'), 0
    for index,value in enumerate(rights):
        calc_value = value / ( y + item_player[index])
        if calc_value > max_value:
            max_index = index
            max_value = calc_value
    return max_value, max_index





