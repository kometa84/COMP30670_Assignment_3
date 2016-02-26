import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.seater import Seater
'''
Created on 22 Feb 2016

@author: silvia
'''

def test_pattern():
    # test the pattern matching is parsing the line correctly
    seater = Seater()
    res = seater.get_cmd("occupy 957,736 through 977,890")
    assert res == ('occupy', 957, 736, 977, 890)
    
def test_number_occupied():
    # test if my function number_occupied is correct
    seater = Seater(size=5)
    seater.seat("occupy 0,0 through 4,4")
    assert seater.number_occupied()== 25

def test_empty():
    # test if my function empty is correct
    seater = Seater(size=5)
    seater.seat("occupy 0,0 through 4,4")
    seater.seat("empty 0,0 through 4,4")
    assert seater.number_occupied()== 0

def test_occupy():
    # test if my function occupy is correct
    seater = Seater(size=5)
    seater.seat("occupy 0,0 through 4,4")
    seater.seat("empty 0,0 through 4,4")
    seater.seat("occupy 0,0 through 2,2")
    assert seater.number_occupied()== 9
    
def test_toogle():
    # test if my function toogle is correct in emptying seats
    seater = Seater(size=5)
    seater.seat("occupy 0,0 through 4,4")
    seater.seat("toggle 0,0 through 2,2")
    assert seater.number_occupied()== 16

def test_toogle2():
    # test if my function toogle is correct in occupying seats
    seater = Seater(size=5)
    seater.seat("occupy 0,0 through 4,4")
    seater.seat("empty 0,0 through 4,4")
    seater.seat("toggle 0,0 through 4,4")
    assert seater.number_occupied()== 25

