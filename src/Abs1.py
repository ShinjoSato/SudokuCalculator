# -*- coding: utf8 -*-
from src.Sudoku import Sudoku
class Abs1(Sudoku):
    def canPutNumberOnPlaceWithAbs1(self, place, matrix, num, absolutes):
        #check absolute 1
        absnums = []
        for abs1 in absolutes:
            if(place in abs1):
                a = matrix[abs1[0][0]][abs1[0][1]]
                b = matrix[abs1[1][0]][abs1[1][1]]
                if(1<a):
                    absnums.append(a-1)
                if(a<9 and a!=0):
                    absnums.append(a+1)
                if(1<b):
                    absnums.append(b-1)
                if(b<9 and b!=0):
                    absnums.append(b+1)
        if(0<len(absnums)):
            if (super().canPutNumberOnPlace(place,matrix,num))and(num in absnums):
                return True
            else:
                return False
        else:
            return (super().canPutNumberOnPlace(place,matrix,num))
    
    def fillMatrixIntoNumbers(self, matrix, numbers, places, absolutes):
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
                        if(self.canPutNumberOnPlaceWithAbs1(place, matrix, num, absolutes)):
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
                        result=self.fillMatrixIntoNumbers(matrix, numbers, places, absolutes)
                        if not(result==[]) :
                            return result
                        #Remove a number
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    return []
            return []


if __name__ == "__main__":

    #Question 84
    matrix = [
        [0,1,0,  8,0,0,  0,0,0],
        [0,0,0,  2,3,7,  0,5,0],
        [0,5,2,  0,0,0,  0,0,4],

        [0,0,0,  7,0,0,  0,0,8],
        [0,0,1,  0,0,0,  4,0,0],
        [5,0,0,  0,0,6,  0,0,0],

        [6,0,0,  0,0,0,  8,1,0],
        [0,3,0,  5,7,8,  0,0,0],
        [0,0,0,  0,0,9,  0,4,0]
    ]

    absolutes = [
        [[0,0],[1,0]],  [[0,2],[1,2]],  [[0,2],[0,3]],  [[0,4],[0,5]],  [[0,7],[0,8]],
        [[0,8],[1,8]],  [[1,1],[2,1]],  [[2,0],[3,0]],  [[2,1],[3,1]],  [[2,3],[3,3]],
        [[2,6],[2,7]],  [[3,6],[3,7]],  [[3,4],[4,4]],  [[4,0],[4,1]],  [[4,4],[4,5]],
        [[4,5],[4,6]],  [[4,7],[4,8]],  [[4,7],[4,8]],  [[5,1],[5,2]],  [[5,2],[5,3]],
        [[5,3],[6,3]],  [[6,3],[6,4]],  [[6,8],[7,8]],  [[7,0],[8,0]],  [[7,1],[7,2]],
        [[6,2],[7,2]],  [[7,2],[7,3]],  [[7,4],[8,4]],  [[8,1],[8,2]],  [[8,6],[8,7]],
        [[8,7],[8,8]]
    ]


    sudoku = Abs1()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), absolutes)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")