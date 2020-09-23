# -*- coding: utf8 -*-
from src.Sudoku import Sudoku
class TwoTone(Sudoku):
    def canPutNumberOnPlace(self, place, matrix, num, twotone):
        stack = []
        #twotone
        if(0<twotone[place[0]][place[1]]):
            for i in range(0, len(twotone)):
                for j in range(0, len(twotone[i])):
                    if(twotone[place[0]][place[1]] == twotone[i][j]):
                        stack.append( matrix[i][j] )
        stack = list(set(stack))
        if(num not in stack)and(super().canPutNumberOnPlace(place, matrix, num)):
            return True
        else:
            return False

    def fillMatrixIntoNumbers(self, matrix, numbers, places, groups):
        if(len(numbers)==0):
            super().printMatrix(matrix)
            return matrix
        else:
            #iはcandidateの個数の閾値で、選択肢が少ないところを深掘りさせるためのfor文
            for place in places:
                initial=0
                candidate=[]
                for num in numbers:
                    if(initial != num):
                        initial=num
                        if(self.canPutNumberOnPlace(place, matrix, num, groups)):
                            candidate.append(num)
                if(len(candidate)<4):
                    for c in candidate:
                        #Insert a number
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        #Recursion
                        result=self.fillMatrixIntoNumbers(matrix, numbers, places, groups)
                        if not(result==[]):
                            return result
                        #Remove a number
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    return []
            return []


if __name__ == "__main__":
    #Question 228
    matrix = [
        [0,0,0,  9,0,0,  0,0,4],
        [0,0,7,  0,2,0,  0,3,0],
        [1,0,0,  7,0,5,  0,0,9],

        [0,8,0,  0,0,0,  0,9,0],
        [7,0,9,  0,1,0,  3,0,2],
        [0,6,0,  0,0,0,  0,1,0],

        [9,0,0,  4,0,2,  0,0,8],
        [0,4,0,  0,8,0,  9,0,0],
        [2,0,0,  0,0,6,  0,0,0]
    ]

    twotone = [
        [0,0,0,  0,0,1,  1,0,0],
        [0,1,0,  1,0,0,  0,0,0],
        [0,0,1,  0,1,0,  0,0,0],

        [0,0,0,  1,0,0,  0,0,2],
        [0,1,0,  0,0,0,  0,2,0],
        [1,0,0,  0,0,2,  0,0,0],

        [0,0,0,  0,2,0,  2,0,0],
        [0,0,0,  0,0,2,  0,2,0],
        [0,0,2,  2,0,0,  0,0,0]
    ]
    

    sudoku = TwoTone()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), twotone)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")