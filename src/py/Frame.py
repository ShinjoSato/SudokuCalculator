# -*- coding: utf8 -*-
from Sudoku import Sudoku
class Frame(Sudoku):
    def canPutNumberOnPlace(self, place, matrix, num, groups):
        #Frame
        gSum=groups[place[0]][place[1]][1]-num
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(gSum<0):
                    return False
                if(groups[i][j][0]==groups[place[0]][place[1]][0] and [i,j]!=place):
                    if(matrix[i][j]==num):
                        return False
                    gSum-=matrix[i][j]

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
    #Question 244 extends
    matrix = [
        [0,0,0,  0,0,4,  0,0,0],
        [0,8,0,  1,0,0,  5,0,0],
        [0,4,2,  0,5,0,  0,0,1],

        [2,0,0,  4,0,0,  0,7,0],
        [0,0,0,  7,0,2,  0,0,0],
        [0,1,0,  0,0,5,  0,0,6],

        [8,0,0,  0,1,0,  4,9,0],
        [0,0,9,  0,0,8,  0,5,0],
        [0,0,0,  9,0,0,  0,0,0]
    ]

    groups=[
        [[1,9],[2,14],[2,14],     [2,14],[3,9],[3,9],     [4,18],[4,18],[4,18]],
        [[1,9],[5,15],[5,15],     [6,9],[3,9],[7,14],     [7,14],[8,10],[8,10]],
        [[9,11],[10,7],[6,9],     [6,9],[11,12],[12,18],  [12,18],[13,9],[13,9]],

        [[9,11],[10,7],[15,15],    [15,15],[11,12],[11,12],  [12,18],[16,19],[16,19]],
        [[14,13],[14,13],[15,15],  [17,15],[17,15],[18,3],   [18,3],[16,19],[19,13]],
        [[20,16],[21,8],[22,11],   [22,11],[23,14],[23,14],  [24,6],[25,13],[19,13]],

        [[20,16],[21,8],[27,12],   [29,11],[30,7],[30,7],    [24,6],[25,13],[19,13]],
        [[20,16],[26,13],[27,12],  [29,11],[29,11],[31,15],  [31,15],[33,8],[33,8]],
        [[26,13],[26,13],[28,20],  [28,20],[28,20],[32,9],   [32,9],[34,9],[34,9]]
    ]

    #Question 248 extends
    matrix=[
        [0,0,0,   7,0,4,   0,0,0],
        [0,3,0,   0,0,0,   0,8,0],
        [1,0,0,   3,0,6,   0,0,5],

        [0,0,0,   0,0,0,   0,0,0],
        [5,0,6,   0,0,0,   8,0,3],
        [0,7,0,   0,0,0,   0,6,0],

        [0,0,0,   1,0,8,   0,0,0],
        [0,1,0,   0,0,0,   0,2,0],
        [0,0,0,   2,0,7,   0,0,0]
    ]
    groups=[
        [[1,11],[2,14],[2,14],   [3,15],[3,15],[4,7],   [5,7],[6,10],[6,10]],
        [[1,11],[2,14],[7,12],   [7,12],[4,7],[4,7],   [5,7],[8,14],[8,14]],
        [[9,5],[9,5],[10,18],   [11,9],[12,19],[12,19],   [13,12],[14,12],[15,7]],

        [[16,13],[10,18],[10,18],   [11,9],[12,19],[13,12],   [13,12],[14,12],[15,7]],
        [[16,13],[17,8],[17,8],   [18,21],[19,16],[19,16],   [19,16],[20,10],[21,12]],
        [[22,7],[23,12],[18,21],   [18,21],[24,8],[25,14],   [25,14],[20,10],[21,12]],

        [[22,7],[23,12],[26,3],   [26,3],[24,8],[25,14],   [27,14],[27,14],[28,15]],
        [[29,13],[30,4],[30,4],   [31,11],[31,11],[32,20],   [32,20],[27,14],[28,15]],
        [[29,13],[33,17],[33,17],   [31,11],[34,10],[34,10],   [32,20],[35,5],[35,5]]
    ]

    sudoku = Frame()
    result=sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), groups)
    if not(result==[]):
        print('SUCCESS!!')
    else:
        print("FAIL")