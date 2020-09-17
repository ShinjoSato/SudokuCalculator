# -*- coding: utf8 -*-
class Sudoku:
    def searchLackingNumbersSet(self, matrixes):
        numbersSet=[]
        for matrix in matrixes:
            numbersSet.append(self.searchLackingNumbers(matrix))
        return numbersSet

    def searchLackingNumbers(self, matrix):
        stack = []
        for i in matrix:
            for j in i:
                if(j != 0):
                    stack.append(j)
        stack_all = []
        num_limit = 9      
        pack_num  = int(len(matrix)*len(matrix[0])/9)
        for i in range(1,1 + num_limit):
            for j in range(0,pack_num):
                stack_all.append(i)
        for i in stack:
            stack_all.remove(i)
        return  stack_all

    def canPutNumberOnDupplicationPlace(self, place, matrixes, id, num, duplications):
        if not(self.canPutNumberOnPlace(place,matrixes[id],num)):
            return False
        if(0<len(duplications[id][place[0]][place[1]])):
            matrix_id=duplications[id][place[0]][place[1]][0]
            dup_place=[duplications[id][place[0]][place[1]][1], duplications[id][place[0]][place[1]][2]]
            if not(self.canPutNumberOnPlace(dup_place, matrixes[matrix_id], num)):
                return False
        return True

    def canPutNumberOnPlace(self, place, matrix, num):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )

        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )

        I=int(place[0]/3)*3
        J=int(place[1]/3)*3

        for p in range(I, I+3):
            for q in range(J, J+3):
                stack.append( matrix[p][q] )

        stack = list(set(stack))
        if num not in stack:
            return True
        else:
            return False


    def searchEmptyPlacesSet(self,matrixes):
        placesSet=[]
        for matrix in matrixes:
            placesSet.append(self.searchEmptyPlaces(matrix))
        return placesSet

    def searchEmptyPlaces(self, matrix):
        places = []
        #print('matrix',matrix)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(matrix[i][j] == 0):
                    places.append([i,j])
        return places


    def fillMatrixesIntoNumbers(self, matrixes, numbersSet, placesSet, duplications):
        len_numbers=0
        for numbers in numbersSet:
            len_numbers+=len(numbers)

        if(len_numbers==0):
            for matrix in matrixes:
                for rows in matrix:
                    for i in rows:
                        print(i, ' ', end=''),
                    print()
                print()
            return True
        else:
            #iはcandidateの個数の閾値で、選択肢が少ないところを深掘りさせるためのfor文
            for i in range(0,len(placesSet)):
                for place in placesSet[i]:
                    initial=0
                    candidate=[]
                    for num in numbersSet[i]:
                        if(initial != num):
                            initial=num
                            if(self.canPutNumberOnDupplicationPlace(place, matrixes, i, num, duplications)):
                                candidate.append(num)
                    if(len(candidate)<3):
                        for c in candidate:
                            idx_place=placesSet[i].index(place)
                            idx_num=numbersSet[i].index(c)
                            placesSet[i].remove(place)
                            numbersSet[i].remove(c)
                            matrixes[i][place[0]][place[1]]=c
                            #重複されているなら
                            if(0<len(duplications[i][place[0]][place[1]])):
                                #重複箇所に加える
                                dup_matrix_id=duplications[i][place[0]][place[1]][0]
                                dup_place=[duplications[i][place[0]][place[1]][1], duplications[i][place[0]][place[1]][2]]
                                idx_dup_place=placesSet[dup_matrix_id].index(dup_place)
                                idx_dup_num=numbersSet[dup_matrix_id].index(c)
                                placesSet[dup_matrix_id].remove(dup_place)
                                numbersSet[dup_matrix_id].remove(c)
                                matrixes[dup_matrix_id][dup_place[0]][dup_place[1]]=c
                                if self.fillMatrixesIntoNumbers(matrixes, numbersSet, placesSet, duplications):
                                    return True
                                #重複箇所のを省く
                                matrixes[dup_matrix_id][dup_place[0]][dup_place[1]]=0
                                numbersSet[dup_matrix_id].insert(idx_dup_num, c)
                                placesSet[dup_matrix_id].insert(idx_dup_place, dup_place)
                            else:
                                if self.fillMatrixesIntoNumbers(matrixes, numbersSet, placesSet, duplications):
                                    return True
                            matrixes[i][place[0]][place[1]]=0
                            numbersSet[i].insert(idx_num, c)
                            placesSet[i].insert(idx_place, place)
                        #if(len(candidate)==1):
                        return False
            return False




if __name__ == "__main__":

    #Question 213
    matrixes = [
        [
            [6,0,1,  0,0,3,  0,0,5],
            [0,5,0,  1,9,0,  8,0,0],
            [3,0,0,  0,7,0,  0,0,9],

            [0,0,3,  0,0,9,  0,6,0],
            [1,0,6,  0,3,0,  0,5,2],
            [0,4,0,  6,0,1,  0,0,0],

            [8,3,0,  0,6,0,  0,0,0],
            [0,0,5,  0,0,7,  0,0,0],
            [2,0,0,  3,0,0,  0,0,0]
        ],
        [
            [0,0,0,  0,0,6,  0,0,8],
            [0,0,0,  2,0,0,  5,0,0],
            [0,0,0,  0,1,0,  0,9,6],

            [0,0,0,  1,0,8,  0,6,0],
            [1,3,0,  0,7,0,  8,0,9],
            [0,7,0,  6,0,0,  1,0,0],

            [4,0,0,  0,6,0,  0,0,5],
            [0,0,5,  0,9,1,  0,4,0],
            [2,0,0,  8,0,0,  3,0,1]
        ]
    ]

    duplications = [
        [
            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],

            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],

            [[],[],[],  [],[],[],  [1,0,0],[1,0,1],[1,0,2]],
            [[],[],[],  [],[],[],  [1,1,0],[1,1,1],[1,1,2]],
            [[],[],[],  [],[],[],  [1,2,0],[1,2,1],[1,2,2]]
        ],
        [
            [[0,6,6],[0,6,7],[0,6,8],  [],[],[],  [],[],[]],
            [[0,7,6],[0,7,7],[0,7,8],  [],[],[],  [],[],[]],
            [[0,8,6],[0,8,7],[0,8,8],  [],[],[],  [],[],[]],

            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],

            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]],
            [[],[],[],  [],[],[],  [],[],[]]
        ]
    ]


    

    sudoku = Sudoku()
    if(sudoku.fillMatrixesIntoNumbers(matrixes, sudoku.searchLackingNumbersSet(matrixes), sudoku.searchEmptyPlacesSet(matrixes), duplications)):
        print('SUCCESS!!')
    else:
        print("FAIL")