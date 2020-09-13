# -*- coding: utf8 -*-
class Sudoku:
    def searchLackingNumbers(self, matrix):
        stack = []
        for i in matrix:
            for j in i:
                if(j != 0):
                    stack.append(j)
        stack_all = []
        num_limit = 12      
        pack_num  = int(len(matrix)*len(matrix[0])/12)
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
            for i in range(0, 9):
                stack.append(matrix[i][i])
        
        #right-up
        if(place[0]==(9-1)-place[1]):
            for i in range(0,9):
                stack.append(matrix[i][8-i])
        '''

        I=int(place[0]/3)*3
        J=int(place[1]/4)*4

        for p in range(I, I+3):
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
        if(len(numbers)==0):
            for rows in matrix:
                for i in rows:
                    print(i, ' ', end=''),
                print()
            return True
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
                if(len(candidate)<5):
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
                    #if(len(candidate)==1):
                    return False
            return False




if __name__ == "__main__":

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


    sudoku = Sudoku()
    if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix))):
        print('SUCCESS!!')
    else:
        print("FAIL")