"""
Created on Sun Jul 14 10:17:48 2019

@author: Carlos Villa
"""
import numpy as np

# This game is a take on a 21 Card Trick. 21 numbers are randomly placed
# in a 7x3 matrix. The player thinks of a number and enters the column that 
# the number is in. This step is repeated three times. Finally, the number
# that the user was thinking of is revealed.

class NumberTrick:
    
    def __init__(self):
        pass
    
    @staticmethod
    def shuffCards(grid, turn):
        
        # Prompt for player input
        if turn == 1:
            col = int(input('Pick a number. What column it is in (1, 2, or 3)?: '))
            print('\n')
        else:
            col = int(input('What column is your number in now (1, 2, or 3)?: '))
            print('\n')
    
        # Stays in loop until user provides valid entry
        while col == 0 or col > 3:
            col = int(input('That is not a valid column! Try again genius (1, 2, or 3): '))
            print('\n')
        
        # Elements in columns are aranged in reverse, and the selected coulumn
        # is aranged between the other two columns. The newly aranged matrix is
        # flattened into 1-D array by columns.
        if col == 1:
            numbers = np.array([grid[::-1,1],grid[::-1,col-1],grid[::-1,2]])
        elif col == 2:
            numbers = np.array([grid[::-1,0],grid[::-1,col-1],grid[::-1,2]])
        else:
            numbers = np.array([grid[::-1,0],grid[::-1,col-1],grid[::-1,1]])
        
        numbers = numbers.flatten()
        
        return numbers
    
    def start(self):
        
        #Create array from 1-21, shuffle
        numbers = np.arange(1,22)
        np.random.shuffle(numbers)
        
        #Round 1
        turn = 1
        grid_1 = numbers.reshape(7,-1)
        print('\n',grid_1)
        numbers_1 = self.shuffCards(grid_1, turn)
        
        #Round 2  
        turn += 1
        grid_2 = numbers_1.reshape(7, -1)
        print(grid_2)
        numbers_2 = self.shuffCards(grid_2, turn)
        
        #Round 3
        turn += 1
        grid_3 = numbers_2.reshape(7, -1)
        print(grid_3) 
        numbers_3 = self.shuffCards(grid_3, turn)
        
        #Result
        print('Your number is {}!'.format(numbers_3[10]))
        
NumberTrick().start()
