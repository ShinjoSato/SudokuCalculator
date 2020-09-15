# -*- coding: utf8 -*-
class Sudoku:
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


    def canPutNumberOnPlace(self, place, matrix, num, inequalities):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )

        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )

        #inequality
        #To Up
        if(0<place[0]):
            if(0<matrix[place[0]-1][place[1]]):
                if(0<inequalities[2*place[0]-1][place[1]]):
                    if not(matrix[place[0]-1][place[1]] < num):
                        return False
                else:
                    if not(num < matrix[place[0]-1][place[1]]):
                        return False
        #To Down
        if(place[0]<len(matrix)-1):
            if(0<matrix[place[0]+1][place[1]]):
                if(0<inequalities[2*place[0]+1][place[1]]):
                    if not(num < matrix[place[0]+1][place[1]]):
                        return False
                else:
                    if not(matrix[place[0]+1][place[1]] < num):
                        return False
        #To Left
        if(0<place[1]):
            if(0<matrix[place[0]][place[1]-1]):
                if(0<inequalities[2*place[0]][place[1]-1]):
                    if not(matrix[place[0]][place[1]-1] < num):
                        return False
                else:
                    if not(num < matrix[place[0]][place[1]-1]):
                        return False
        #To Right
        if(place[1]<len(matrix[place[0]])-1):
            if(0<matrix[place[0]][place[1]+1]):
                if(0<inequalities[2*place[0]][place[1]]):
                    if not(num < matrix[place[0]][place[1]+1]):
                        return False
                else:
                    if not(matrix[place[0]][place[1]+1] < num):
                        return False


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


    def fillMatrixIntoNumbers(self, matrix, numbers, places, inequalities):
        if(len(numbers)==0):
            self.printMatrix(matrix)
            return True
        else:
            #iはcandidateの個数の閾値で、選択肢が少ないところを深掘りさせるためのfor文
            for place in places:
                initial=0
                candidate=[]
                for num in numbers:
                    if(initial != num):
                        initial=num
                        if(self.canPutNumberOnPlace(place, matrix, num, inequalities)):
                            candidate.append(num)
                if(len(candidate)<7):
                    for c in candidate:
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        if self.fillMatrixIntoNumbers(matrix, numbers, places, inequalities):
                            return True
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    return False
            return False




if __name__ == "__main__":

    #Question 192
    matrix = [
        [0,0,0,  0,0,0],
        [0,0,0,  2,0,0],
        [0,0,0,  0,2,0],

        [0,6,0,  0,0,0],
        [0,0,6,  0,0,0],
        [0,0,0,  0,0,0]
    ]

    inequalities = [
        [-1, 1, 1, -1, 1],
        [-1, 1, -1, -1, 1, -1],
        [1, -1, -1, 1, -1],
        [1, -1, 1, 1, -1, -1],
        [-1, 1, -1, -1, -1],

        [-1, 1, -1, 1, 1, 1],
        [1, -1, 1, -1, -1],
        [-1, -1, 1, -1, 1, 1],
        [-1, 1, -1, 1, -1],
        [1, 1, -1, -1, -1, 1],

        [-1, -1, -1, 1, 1]
    ]


    


    sudoku = Sudoku()
    if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), inequalities)):
        print('SUCCESS!!')
    else:
        print("FAIL")