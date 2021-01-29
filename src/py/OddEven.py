# -*- coding: utf8 -*-
from Sudoku import Sudoku
class OddEven(Sudoku):
    def canPutNumberOnPlace(self, place, matrix, num, odd_even):
        #Odd or Even
        if(num%2!=odd_even[place[0]][place[1]]):
            return False
        if(super().canPutNumberOnPlace(place, matrix, num)):
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
    #Question 117 extends
    matrix = [
        [5,2,0,  0,7,0,  0,0,6],
        [0,0,4,  0,0,9,  0,0,7],
        [7,0,0,  2,0,0,  3,4,0],

        [0,0,5,  8,0,1,  0,0,3],
        [0,4,0,  0,0,0,  0,9,0],
        [1,0,0,  5,0,7,  4,0,0],

        [0,7,3,  0,0,8,  0,0,1],
        [9,0,0,  7,0,0,  2,0,0],
        [6,0,0,  0,3,0,  0,7,8]
    ]

    oddeven = [
        [1,0,1,  0,1,1,  0,1,0],
        [1,0,0,  0,1,1,  1,0,1],
        [1,0,1,  0,0,1,  1,0,1],

        [0,1,1,  0,0,1,  1,0,1],
        [0,0,1,  1,0,0,  1,1,1],
        [1,1,0,  1,1,1,  0,0,0],

        [0,1,1,  1,0,0,  0,1,1],
        [1,1,0,  1,1,0,  0,1,0],
        [0,1,0,  1,1,0,  1,1,0]
    ]
    
    #Question 121 extends
    matrix=[
        [0,0,1,  4,0,2,  0,0,0],
        [4,0,2,  0,5,0,  0,0,9],
        [0,7,0,  0,0,9,  0,0,0],

        [0,4,0,  0,0,0,  0,2,5],
        [0,0,7,  5,0,8,  4,0,0],
        [1,6,0,  0,0,0,  0,9,0],

        [0,0,0,  8,0,0,  0,5,0],
        [2,0,0,  0,6,0,  7,0,3],
        [0,0,0,  7,0,1,  2,0,0]
    ]

    oddeven=[
        [0,1,1,  0,1,0,  1,1,0],
        [0,0,0,  1,1,0,  1,1,1],
        [1,1,1,  1,0,1,  0,0,0],

        [1,0,0,  0,1,1,  1,0,1],
        [1,0,1,  1,1,0,  0,1,0],
        [1,0,1,  0,0,1,  0,1,1],

        [1,1,0,  0,0,0,  1,1,1],
        [0,1,0,  1,0,1,  1,0,1],
        [0,1,1,  1,1,1,  0,0,0]
    ]

    #Question 161 extends
    matrix=[
        [0,0,3,  0,0,2,  1,0,0],
        [0,0,8,  3,0,0,  0,6,0],
        [9,0,0,  0,6,1,  0,2,0],

        [0,1,0,  9,0,0,  2,0,0],
        [8,0,0,  0,0,0,  0,0,1],
        [0,0,5,  0,0,3,  0,4,0],
        
        [0,6,0,  7,9,0,  0,0,2],
        [0,7,0,  0,0,6,  3,0,0],
        [0,0,1,  5,0,0,  9,0,0]
    ]
    oddeven=[
        [0,0,1,  0,1,0,  1,1,1],
        [1,0,0,  1,1,1,  0,0,1],
        [1,1,1,  0,0,1,  0,0,1],

        [0,1,0,  1,0,1,  0,1,1],
        [0,1,0,  0,0,1,  1,1,1],
        [1,1,1,  0,1,1,  0,0,0],

        [1,0,0,  1,1,0,  1,1,0],
        [1,1,1,  1,0,0,  1,0,0],
        [0,0,1,  1,1,0,  1,1,0]
    ]

    #Question 164 extends
    matrix=[
        [8,0,0,  0,0,0,  0,5,0],
        [0,9,0,  0,0,0,  0,8,0],
        [0,0,5,  0,2,0,  6,0,7],

        [0,5,0,  0,6,3,  0,0,1],
        [0,3,0,  2,0,9,  0,7,0],
        [1,0,0,  5,7,0,  0,6,0],

        [5,0,1,  0,4,0,  8,0,0],
        [0,6,0,  0,0,0,  0,2,0],
        [0,2,0,  0,0,0,  0,0,9]
    ]
    oddeven=[
        [0,1,1,  0,1,0,  1,1,0],
        [0,1,0,  1,1,1,  1,0,0],
        [1,0,1,  1,0,0,  0,1,1],

        [1,1,1,  0,0,1,  0,0,1],
        [0,1,0,  0,1,1,  1,1,0],
        [1,0,0,  1,1,0,  1,0,1],

        [1,1,1,  1,0,0,  0,1,0],
        [1,0,1,  1,0,1,  0,0,1],
        [0,0,0,  0,1,1,  1,1,1]
    ]

    sudoku = OddEven()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), oddeven)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")