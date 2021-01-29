# -*- coding: utf8 -*-
from Sudoku import Sudoku
class Zigzag(Sudoku):
    def canPutNumberOnPlace(self, place, matrix, num, groups):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )
        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )
        #zig-zag
        for i in range(0, len(groups)):
            for j in range(0, len(groups[i])):
                if(groups[place[0]][place[1]] == groups[i][j]):
                    stack.append( matrix[i][j] )
        stack = list(set(stack))
        if num not in stack:
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
                if(len(candidate)<5):
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

    #Question 278
    matrix = [
        [0,0,8,  0,6,0,  7,0,0],
        [0,2,0,  0,0,0,  0,8,0],
        [2,0,7,  0,0,0,  5,0,4],

        [0,4,0,  0,0,0,  0,2,0],
        [6,0,0,  0,7,0,  0,0,9],
        [0,0,2,  5,0,4,  6,0,0],

        [4,0,5,  0,0,0,  3,0,8],
        [0,3,0,  0,4,0,  0,1,0],
        [0,0,0,  4,0,8,  0,0,0]
    ]

    groups = [
        [[0,0], [0,1], [1,1], [2,1], [3,1], [2,2], [1,3], [2,3], [3,3]],
        [[0,2], [1,2], [0,3], [0,4], [0,5], [0,6], [1,4], [2,4], [1,6]],
        [[0,7], [0,8], [1,7], [2,7], [3,7], [2,6], [1,5], [2,5], [3,5]],

        [[1,0], [2,0], [3,0], [4,0], [5,0], [4,1], [4,2], [3,2], [4,3]],
        [[3,4], [4,4], [5,4], [6,4], [7,4], [6,2], [6,3], [6,5], [6,6]],
        [[1,8], [2,8], [3,8], [4,8], [5,8], [4,7], [4,6], [4,5], [3,6]],

        [[5,1], [5,2], [5,3], [6,0], [6,1], [7,0], [8,0], [8,1], [8,2]],
        [[7,1], [7,2], [7,3], [8,3], [8,4], [8,5], [7,5], [7,6], [7,7]],
        [[5,5], [5,6], [5,7], [6,7], [6,8], [7,8], [8,8], [8,7], [8,6]]
    ]

    #Question 221
    matrix = [
        [0,5,0,  7,0,1,  0,2,0],
        [0,0,3,  0,2,0,  9,0,0],
        [0,3,0,  0,0,0,  0,7,0],

        [7,0,0,  2,0,9,  0,0,3],
        [0,4,5,  0,0,0,  1,9,0],
        [6,0,0,  9,0,4,  0,0,1],

        [3,0,6,  0,9,0,  4,0,5],
        [0,7,0,  4,0,6,  0,1,0],
        [1,0,0,  0,8,0,  0,0,2]
    ]

    groups = [
        [1,1,1,  1,2,3,  3,3,3],
        [4,1,2,  2,2,2,  2,3,5],
        [4,1,1,  1,2,3,  3,3,5],

        [4,4,4,  1,2,3,  5,5,5],
        [4,6,4,  4,2,5,  5,9,5],
        [6,6,6,  4,7,5,  9,9,9],

        [6,7,7,  7,7,7,  7,7,9],
        [6,8,8,  8,7,8,  8,8,9],
        [6,6,6,  8,8,8,  9,9,9]
    ]

    #Question 082 extend
    matrix=[
        [0,0,7,  4,0,8,  9,0,0],
        [0,5,0,  0,9,0,  0,8,0],
        [2,0,0,  6,0,7,  0,0,3],

        [7,0,3,  5,0,1,  6,0,9],
        [5,8,0,  0,6,0,  0,7,1],
        [0,0,9,  0,0,0,  5,0,0],

        [0,3,4,  0,1,0,  8,2,0],
        [1,4,0,  8,0,9,  0,5,7],
        [0,7,5,  0,4,0,  1,9,0]
    ]

    groups=[
        [1,1,1,  2,2,2,  3,3,3],
        [1,1,2,  2,2,2,  2,3,3],
        [1,1,1,  1,2,3,  3,3,3],

        [4,4,4,  5,5,5,  6,6,6],
        [4,4,5,  5,5,5,  5,6,6],
        [7,4,4,  4,5,6,  6,6,9],

        [7,7,4,  8,8,8,  6,9,9],
        [7,7,8,  8,8,8,  8,9,9],
        [7,7,7,  7,8,9,  9,9,9]
    ]

    #Question 163 extends
    matrix=[
        [5,0,0,  0,1,0,  6,9,0],
        [1,0,5,  0,0,0,  2,7,9],
        [0,6,7,  4,0,9,  1,0,0],

        [0,0,0,  0,7,0,  0,8,0],
        [6,0,1,  5,0,8,  7,0,2],
        [0,7,0,  0,3,0,  0,0,0],

        [0,0,8,  9,0,6,  4,3,0],
        [9,1,4,  0,0,0,  8,0,7],
        [0,9,6,  0,4,0,  0,0,8]
    ]
    groups=[
        [1,1,1,  2,2,2,  3,3,3],
        [1,1,2,  2,2,2,  3,3,6],
        [1,1,1,  2,5,2,  3,3,6],

        [4,4,1,  5,5,5,  3,3,6],
        [4,4,4,  4,5,6,  6,6,6],
        [4,7,7,  5,5,5,  9,6,6],

        [4,7,7,  8,5,8,  9,9,9],
        [4,7,7,  8,8,8,  8,9,9],
        [7,7,7,  8,8,8,  9,9,9]
    ]

    sudoku = Zigzag()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), groups)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")