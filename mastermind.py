# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:27:46 2023

@author: cihan
"""

import random
import functools
import sys

code = random.sample(["r", "r", "b", "b", "g", "g", "y", "y", "c", "c", "m", "m"], 4)
i = 1
while i <= 13:
    guess = list(input("MasterMind " + str(i) + " < ").lower())
    if len(guess) != 4: print("Error! Only 4 characters allowed!")
    elif not all(char in ["r", "b", "g", "y", "c", "m"] for char in guess): print("Error! Only letters (r)ed (g)reen (b)lue (m)agenta (c)yan (y)ellow allowed!")
    else :
        b = sum(1 for i, j in enumerate(code) if j == guess[i])
        w = len([char for char in code if char in guess]) - b
        print("b : " + str(b) + " w : " + str(w))
        i+=1
        if(guess == code): 
            print("You Win!")
            sys.exit()
print("You Lose!")