# -*- coding: utf8 -*-
'''
16x16: range=3
12x12: range=5
'''
from math import sqrt,floor,ceil
class Joint:
    def searchLackingNumbers(self, matrix):
        stack = []
        for i in matrix:
            for j in i:
                if(j != 0):
                    stack.append(j)
        stack_all = []
        num_limit = len(matrix)
        pack_num  = int(len(matrix)*len(matrix[0])/num_limit)
        for i in range(1,1 + num_limit):
            for j in range(0,pack_num):
                stack_all.append(i)
        for i in stack:
            stack_all.remove(i)
        return  stack_all

    def canPutNumberOnPlace(self, place, matrix, num, group):
        if(0<len(group[place[0]][place[1]])):
            for point in group[place[0]][place[1]]:
                if(0<matrix[point[0]][point[1]]):
                    if(abs(matrix[point[0]][point[1]]-num)!=1):
                        return False

        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )
        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )
        #MxN (M<=N)
        """
        height=floor(sqrt(len(matrix)))
        width=ceil(sqrt(len(matrix[0])))
        I=int(place[0]/height)*height
        J=int(place[1]/width)*width
        for p in range(I, I+height):
            for q in range(J, J+width):
                stack.append( matrix[p][q] )
        """
        #remove duplication numbers
        stack = list(set(stack))
        if num not in stack:
            return True
        else:
            return False

    def searchEmptyPlaces(self, matrix):
        places = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j] == 0):
                    places.append([i,j])
        return places

    def printMatrix(self, matrix):
        for rows in matrix:
            for i in rows:
                print(i, ' ', end=''),
            print()

    def fillMatrixIntoNumbers(self, matrix, numbers, places, groups):
        if(len(numbers)==0):
            self.printMatrix(matrix)
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
    #Question 165 extends
    matrix = [
        [0,0,5,  0,  0,0,3],
        [0,0,2,  7,  0,0,0],
        [5,0,6,  0,  7,0,0],

        [0,6,0,  0,  0,7,0],

        [0,0,7,  0,  6,0,5],
        [0,0,0,  6,  2,0,0],
        [6,0,0,  0,  5,0,0]
    ]

    groups=[
        [[],[],[],  [],  [],[],[]],
        [[],[],[],  [],  [],[],[]],
        [[],[],[],  [[3,3]],  [],[[2,6]],[[2,5]]],

        [[],[],[],  [[2,3]],  [],[],[]],

        [[],[],[],  [],  [],[],[]],
        [[],[[5,2]],[[5,1],[6,2]],  [],  [],[],[]],
        [[[6,1]],[[6,0]],[[5,2]],  [],  [],[],[]]
    ]

    sudoku = Joint()
    #if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix))):
    print(sudoku.searchEmptyPlaces(matrix))
    if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), groups)):
        print('SUCCESS!!')
    else:
        print("FAIL")