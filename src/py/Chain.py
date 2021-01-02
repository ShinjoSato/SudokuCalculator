# -*- coding: utf8 -*-
from src.py.Sudoku import Sudoku
class Chain(Sudoku):
    def searchLackingNumbers(self, matrix):
        stack = []
        for i in matrix:
            for j in i:
                if(j != 0):
                    stack.append(j)
        stack_all = []
        num_limit = 6      
        pack_num  = int(len(matrix)*len(matrix[0])/6)
        for i in range(1,1 + num_limit):
            for j in range(0,pack_num):
                stack_all.append(i)
        for i in stack:
            stack_all.remove(i)
        return  stack_all

    def canPutNumberOnPlace(self, place, matrix, num, groups):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )
        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )
        #chain
        for group in groups:
            if place in group:
                for g in group:
                    stack.append(matrix[g[0]][g[1]])
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
                        #Input a number
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
    #Question 181
    matrix = [
        [1,0,0,  0,0,0],
        [0,0,0,  0,0,1],
        [4,0,0,  0,0,0],

        [0,0,6,  0,0,2],
        [0,0,0,  0,0,0],
        [5,0,0,  3,0,0]
    ]

    chains = [
        [[0,0], [0,1], [1,1], [2,0], [2,2], [3,3]],
        [[0,3], [0,4], [0,5], [1,4], [2,3], [2,5]],
        [[1,0], [2,1], [1,2], [3,0], [3,2], [4,1]],

        [[0,2], [1,3], [2,4], [1,5], [3,5], [4,4]],
        [[3,1], [4,0], [5,0], [5,1], [5,2], [4,2]],
        [[3,4], [4,3], [5,3], [5,4], [5,5], [4,5]]
    ]


    sudoku = Chain()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), chains)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")