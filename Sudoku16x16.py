# -*- coding: utf8 -*-
class Sudoku:
    def searchLackingNumbers(self, matrix):
        stack = []
        for i in matrix:
            for j in i:
                if(j != 0):
                    stack.append(j)
        stack_all = []
        num_limit = 16      
        pack_num  = int(len(matrix)*len(matrix[0])/16)
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

        '''
        #left-up
        if(place[0]==place[1]):
            for i in range(0, 16):
                stack.append(matrix[i][i])
        
        #right-up
        if(place[0]==(16-1)-place[1]):
            for i in range(0,16):
                stack.append(matrix[i][15-i])
        '''

        I=int(place[0]/4)*4
        J=int(place[1]/4)*4

        for p in range(I, I+4):
            for q in range(J, J+4):
                stack.append( matrix[p][q] )

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


    def fillMatrixIntoNumbers(self, matrix, numbers, places):
        #print('numbers',len(numbers))
        if(len(numbers)==0):
            for rows in matrix:
                for i in rows:
                    print(i, ' ', end=''),
                print()
            return True
        else:
            for place in places:
                initial=0
                candidate=[]
                for num in numbers:
                    if(initial != num):
                        initial=num
                        if(self.canPutNumberOnPlace(place, matrix, num)):
                            candidate.append(num)
                if(len(candidate)<3):
                    for c in candidate:
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        if self.fillMatrixIntoNumbers(matrix, numbers, places):
                            return True
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    return False
            return False


if __name__ == "__main__":
    #Question 212
    matrix = [
        [ 0, 9, 0, 0,   8, 0, 0,13,  15, 0, 0, 5,   0, 0,16, 0],
        [ 7, 0, 0, 2,   0, 5, 1, 0,   0,16,13, 0,  14, 0, 0, 4],
        [16, 5, 0, 0,   0, 4, 0, 0,   0, 0, 2, 0,   0, 0,13, 6],
        [ 6, 0, 0, 0,   2, 0,10, 0,   0, 1, 0, 8,   0, 0, 0, 3],

        [ 0,13, 0,16,   0, 0, 3, 5,   1,14, 0, 0,  10, 0, 8, 0],
        [ 0, 0, 5, 0,   6, 0, 4, 0,   0,13, 0,12,   0, 1, 0, 0],
        [ 8, 2, 0, 4,   0, 1, 0,10,  16, 0, 5, 0,   6, 0,14,15],
        [ 1,10, 0, 0,  16, 0,13, 0,   0, 4, 0,15,   0, 0, 9, 5],

        [ 0, 0,13, 0,   0, 0, 6, 0,   0,10, 0, 0,   0, 7, 0, 0],
        [ 4, 1, 0,14,  10, 7, 0, 0,   0, 0,16,13,   5, 0,11, 8],
        [ 0,16,10, 8,   0, 0, 5, 1,   9, 2, 0, 0,  13,12, 4, 0],
        [ 0, 0, 6, 0,   0, 0, 9, 0,   0, 8, 0, 0,   0,16, 0, 0],

        [ 0, 0, 2, 0,   0,10, 0,14,  13, 0, 3, 0,   0, 8, 0, 0],
        [10, 3, 0, 0,   1, 0,16,11,   7, 5, 0, 4,   0, 0, 6,13],
        [13, 0,16, 1,   5, 0, 0, 6,  14, 0, 0, 2,   7,15, 0,11],
        [ 0, 0,11, 0,   4,13,12, 0,   0, 6, 1,10,   0, 3, 0, 0]
    ]

    matrix = [
        [ 0, 9, 0, 0,   8, 0, 0,13,  15, 0, 0, 5,   0, 0,16, 0],
        [ 7, 0, 0, 2,   0, 5, 1, 0,   0,16,13, 0,  14, 0, 0, 4],
        [16, 5, 0, 0,   0, 4, 0, 0,   0, 0, 2, 0,   0, 0,13, 6],
        [ 6, 0, 0,13,   2, 0,10, 0,   0, 1, 0, 8,   0, 0, 0, 3],

        [ 0,13, 0,16,   0, 0, 3, 5,   1,14, 0, 0,  10, 4, 8, 0],
        [ 0, 0, 5, 0,   6, 0, 4, 0,   0,13, 0,12,   0, 1, 0, 0],
        [ 8, 2, 0, 4,   0, 1, 0,10,  16, 0, 5, 0,   6,13,14,15],
        [ 1,10, 0, 6,  16, 0,13, 0,   0, 4, 0,15,   0, 0, 9, 5],

        [ 0, 0,13, 0,   0, 0, 6, 0,   0,10, 0, 0,   0, 7, 0, 0],
        [ 4, 1, 0,14,  10, 7, 0, 0,   0, 0,16,13,   5, 0,11, 8],
        [ 0,16,10, 8,   0, 0, 5, 1,   9, 2, 0, 0,  13,12, 4, 0],
        [ 0, 0, 6, 0,   0, 0, 9, 0,   0, 8, 0, 0,   0,16, 0, 0],

        [ 0, 0, 2, 0,   0,10, 0,14,  13, 0, 3, 0,   0, 8, 0, 0],
        [10, 3, 0, 0,   1, 0,16,11,   7, 5, 0, 4,   0, 0, 6,13],
        [13, 0,16, 1,   5, 0, 0, 6,  14, 0, 0, 2,   7,15, 0,11],
        [ 0, 0,11, 0,   4,13,12, 0,   0, 6, 1,10,   0, 3, 0, 0]
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


    sudoku = Sudoku()
    if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix))):
        print('SUCCESS!!')
    else:
        print("FAIL")