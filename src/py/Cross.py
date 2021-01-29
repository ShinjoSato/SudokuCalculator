# -*- coding: utf8 -*-
from Sudoku import Sudoku
class Cross(Sudoku):
    def canPutNumberOnPlace(self, place, matrix, num):
        stack = []
        num_limit=len(matrix)
        #left-up
        if(place[0]==place[1]):
            for i in range(0, num_limit):
                stack.append(matrix[i][i])
        #right-up
        if(place[0]==(num_limit-1)-place[1]):
            for i in range(0,num_limit):
                stack.append(matrix[i][(num_limit-1)-i])
        stack = list(set(stack))
        if(num not in stack)and(super().canPutNumberOnPlace(place, matrix, num)):
            return True
        else:
            return False


if __name__ == "__main__":
    #Question 139
    matrix = [
        [0,0,3,  8,0,5,  1,0,0],
        [9,0,2,  1,0,4,  6,0,5],
        [0,0,0,  0,9,0,  0,0,0],

        [0,0,4,  0,7,0,  3,0,0],
        [0,8,0,  6,0,1,  0,2,0],
        [0,6,1,  2,0,3,  8,9,0],

        [0,0,0,  0,8,0,  0,0,0],
        [0,0,7,  0,0,0,  9,0,0],
        [0,0,5,  0,6,0,  4,0,0]
    ]

    #Question 225
    matrix = [
        [0,1,0,  0,5,0,  0,2,0],
        [5,0,0,  6,0,3,  0,0,7],
        [0,3,0,  0,0,0,  0,1,0],

        [7,0,0,  0,0,0,  0,0,2],
        [0,5,0,  2,0,4,  0,9,0],
        [0,2,0,  0,0,0,  0,8,0],

        [4,0,0,  0,0,0,  0,0,5],
        [9,0,0,  5,0,2,  0,0,8],
        [0,7,5,  0,4,0,  9,3,0]
    ]

    #Question 243 extend
    matrix=[
        [0,7,2,  0,5,0,  3,4,0],
        [0,0,3,  4,0,7,  6,0,0],
        [0,0,0,  2,0,3,  0,0,0],

        [0,9,0,  0,8,0,  0,7,0],
        [4,3,0,  0,0,0,  0,1,6],
        [0,0,7,  0,4,0,  2,0,0],

        [3,2,0,  0,7,0,  0,6,4],
        [7,0,0,  5,0,2,  0,0,8],
        [0,0,1,  8,0,4,  9,0,0]
    ]

    #Question 160 extends
    matrix=[
        [0,0,0,  7,0,9,  0,0,0],
        [2,0,8,  0,5,0,  6,0,9],
        [0,9,0,  0,2,0,  0,3,0],

        [0,8,0,  0,0,0,  0,1,0],
        [9,3,0,  1,0,4,  0,2,7],
        [0,0,2,  0,9,0,  5,0,0],

        [8,0,0,  0,3,0,  0,0,2],
        [6,0,1,  5,0,7,  3,0,4],
        [0,5,4,  0,0,0,  7,6,0]
    ]

    sudoku = Cross()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix),range=5)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")