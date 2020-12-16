# -*- coding: utf8 -*-
'''
16x16: range=3
12x12: range=5
'''
from math import sqrt,floor,ceil
class Sudoku:
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

    def canPutNumberOnPlace(self, place, matrix, num):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )
        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )
        #MxN (M<=N)
        height=floor(sqrt(len(matrix)))
        width=ceil(sqrt(len(matrix[0])))
        I=int(place[0]/height)*height
        J=int(place[1]/width)*width
        for p in range(I, I+height):
            for q in range(J, J+width):
                stack.append( matrix[p][q] )
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

    def fillMatrixIntoNumbers(self, matrix, numbers, places, range=5):
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
                        if(self.canPutNumberOnPlace(place, matrix, num)):
                            candidate.append(num)
                if(len(candidate)<range):
                    for c in candidate:
                        #Insert a number
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        #Recursion
                        result=self.fillMatrixIntoNumbers(matrix, numbers, places, range)
                        if not(result==[]):
                            return result
                        #Remove a number
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    return []
            return []


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

    #Question211
    matrix = [
        [ 2,12, 7, 0,   0,15, 4, 0,   0,16, 5, 0,   0,14, 9, 3],
        [15, 8, 0, 0,   9, 1,14, 0,   0, 7,12, 2,   0, 0, 5,11],
        [ 4, 0, 5, 0,   0, 0, 0,12,   6, 0, 0, 0,   0, 1, 0, 2],
        [ 0, 0, 0,11,   2, 0, 0, 5,  14, 0, 0, 4,  15, 0, 0, 0],

        [ 0, 6, 0, 5,  16, 0, 0, 0,   0, 0, 0, 9,   2, 0, 1, 0],
        [ 8, 1, 0, 0,   0, 5,13, 0,   0, 3,10, 0,   0, 0,11,12],
        [ 3,16, 0, 0,   0, 8, 2, 0,   0,14, 1, 0,   0, 0, 6, 4],
        [ 0, 0, 2, 9,   0, 0, 0, 7,   8, 0, 0, 0,   3,10, 0, 0],

        [ 0, 0,12, 1,   0, 0, 0, 4,  11, 0, 0, 0,   8, 6, 0, 0],
        [ 6,14, 0, 0,   0, 3, 1, 0,   0, 2, 8, 0,   0, 0, 4, 9],
        [10, 2, 0, 0,   0,16, 5, 0,   0,13, 4, 0,   0, 0,15, 1],
        [ 0, 3, 0,15,  14, 0, 0, 0,   0, 0, 0,16,   5, 0, 2, 0],

        [ 0, 0, 0, 2,  11, 0, 0, 1,   3, 0, 0,10,   4, 0, 0, 0],
        [ 5, 0, 6, 0,   0, 0, 0,16,  12, 0, 0, 0,   0, 2, 0,15],
        [ 1, 7, 0, 0,   5, 9, 8, 0,   0, 4, 2,13,   0, 0,10, 6],
        [16, 4, 9, 0,   0,10, 6, 0,   0, 1,11, 0,   0, 8, 3,13]
    ]

    #Question 209
    matrix = [
        [ 0, 9, 0, 0,   5, 4, 7,11,   0, 0, 1, 0],
        [10, 1, 7, 0,   0, 0, 0, 0,   0, 5, 4,12],
        [ 0, 2, 0, 0,   0,12, 3, 0,   0, 0, 8, 0],

        [ 0, 0, 0, 4,   9, 0, 0, 7,   2, 0, 0, 0],
        [12, 0, 0, 1,  10, 0, 0, 2,   3, 0, 0,11],
        [ 9, 0, 2, 0,   0, 0, 0, 0,   0, 4, 0,10],

        [ 8, 0,12, 0,   0, 0, 0, 0,   0, 3, 0, 7],
        [ 3, 0, 0,10,   7, 0, 0, 9,   4, 0, 0, 2],
        [ 0, 0, 0, 5,   4, 0, 0,12,   1, 0, 0, 0],

        [ 0,12, 0, 0,   0,11,10, 0,   0, 0, 3, 0],
        [ 4,11, 5, 0,   0, 0, 0, 0,   0, 6,10, 9],
        [ 0,10, 0, 0,  12, 9, 8, 4,   0, 0, 2, 0]
    ]

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

    sudoku=Sudoku()
    result=fillMatrixIntoNumbers(matrix, searchLackingNumbers(matrix), searchEmptyPlaces(matrix),range=3)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")