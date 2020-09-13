# -*- coding: utf8 -*-
class SudokuAbs1:
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


    #def checkAbsNumbers(self, place, matrix, ):



    def canPutNumberOnPlaceWithAbs1(self, place, matrix, num, absolutes):
        stack = []

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
                #print ('Find', abs1, a, b)

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
        J=int(place[1]/3)*3

        for p in range(I, I+3):
            for q in range(J, J+3):
                stack.append( matrix[p][q] )

        stack = list(set(stack))

        if(0<len(absnums)):
            if (num not in stack)and(num in absnums):
                return True
            else:
                return False
        else:
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


    def fillMatrixIntoNumbersWithAbs1(self, matrix, numbers, places, absolutes):
        #print(numbers)
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
                        if(self.canPutNumberOnPlaceWithAbs1(place, matrix, num, absolutes)):
                            candidate.append(num)
                if(len(candidate)<5):
                    for c in candidate:
                        idx_place=places.index(place)
                        idx_num=numbers.index(c)
                        places.remove(place)
                        numbers.remove(c)
                        matrix[place[0]][place[1]]=c
                        if self.fillMatrixIntoNumbersWithAbs1(matrix, numbers, places, absolutes):
                            return True
                        matrix[place[0]][place[1]]=0
                        numbers.insert(idx_num, c)
                        places.insert(idx_place, place)
                    #if(len(candidate)==1):
                    return False
            return False




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


    


    sudoku = SudokuAbs1()
    if(sudoku.fillMatrixIntoNumbersWithAbs1(matrix, sudoku.searchLackingNumbers(matrix), sudoku.searchEmptyPlaces(matrix), absolutes)):
        print('SUCCESS!!')
    else:
        print("FAIL")