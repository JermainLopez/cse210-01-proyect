#Jermain Lopez
from tictactoe import winner_or_draw, player1_or_2
from pytest import approx
import pytest
import random

def winner_or_draw_test():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(23):
        for i in range(9):
            x = random(19)
            m = x % 2
            if x == 0:
                list[i] = "X"
            else:
                list[i] = "O"
        w = random(10)

        assert winner_or_draw(list, w) == True or winner_or_draw(list, w) == False or winner_or_draw(list, w) == 'draw' 

def player1_or_2_test():
    for i in range(9):
        m = i % 2
        if m == 0:
            assert player1_or_2("PLayer X") == "PLayer O"
        else:
            assert player1_or_2("PLayer O") == "PLayer X"
            
pytest.main(["-v", "--tb=line", "-rN", __file__])