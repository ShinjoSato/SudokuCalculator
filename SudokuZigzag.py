# -*- coding: utf8 -*-
class Sudoku:
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


    def canPutNumberOnPlace(self, place, matrix, num, groups):
        stack = []
        #columns
        for p in range(0,len(matrix)):
            stack.append( matrix[p][place[1]] )

        #rows
        for q in range(0,len(matrix[place[0]])):
            stack.append( matrix[place[0]][q] )

        for group in groups:
            if place in group:
                for g in group:
                    stack.append(matrix[g[0]][g[1]])


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


    def fillMatrixIntoNumbers(self, matrix, numbers, places, groups):
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
                        if(self.canPutNumberOnPlace(place, matrix, num, groups)):
                            candidate.append(num)
                if(len(candidate)<5):
                    for c in candidate:
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        if self.fillMatrixIntoNumbers(matrix, numbers, places, groups):
                            return True
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    #if(len(candidate)==1):
                    return False
            return False




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


    sudoku = Sudoku()
    if(sudoku.fillMatrixIntoNumbers(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), groups)):
        print('SUCCESS!!')
    else:
        print("FAIL")