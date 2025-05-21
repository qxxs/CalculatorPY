# Working Calculator using Python
## The Log

**This is practice for coding using python, to touch up on different subroutines, and will eventually implement class coding and for loops.**

import random

array = ["accident", "horse", "birds", "cat", "plane"]

word = random.choice(array)  



while True:
    userAnswer = input("Enter a five letter word: ")
    if userAnswer == word:
        print("Well done!")
        break
    else:
        print("Try again")