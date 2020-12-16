from src.Sudoku import Sudoku

from src.Abs1 import Abs1
from src.Chain import Chain
from src.Cross import Cross
from src.Duplication import Duplication
from src.Inequality import Inequality
from src.TwoTone import TwoTone
from src.Zigzag import Zigzag

def main(values):
    result=[]
    print("matrix",values["matrix"])
    print(values["type"])
    print(values["group"])
    
    if(values['type']=='sudoku'):
        sudoku=Sudoku()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'],sudoku.searchLackingNumbers(values['matrix']),sudoku.searchEmptyPlaces(values['matrix']))
    elif(values['type']=='abs1'):
        sudoku=Abs1()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']), values['group'])
    elif(values['type']=='chain'):
        sudoku = Chain()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']), values['group'])
    elif(values['type']=='cross'):
        sudoku = Cross()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']),range=5)
    elif(values['type']=='duplicate'):
        sudoku = Duplication()
        result=sudoku.fillMatrixesIntoNumbers(values['matrix'], sudoku.searchLackingNumbersSet(values['matrix']), sudoku.searchEmptyPlacesSet(values['matrix']), values['group'])
    elif(values['type']=='inequal'):
        sudoku = Inequality()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']), values['group'])
    elif(values['type']=='twotone'):
        sudoku = TwoTone()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']), values['group'])
    elif(values['type']=='zigzag'):
        sudoku = Zigzag()
        result=sudoku.fillMatrixIntoNumbers(values['matrix'], sudoku.searchLackingNumbers(values['matrix']), sudoku.searchEmptyPlaces(values['matrix']), values['group'])

    if not(result==[]):
        print('Succeed :)')
    else:
        print('Fail :(')
    return result


if __name__ == '__main__':
    values={
        'type': 'duplicate',
        'matrix': [
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
        ],
        'group': [
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
    }

    values={
        'type': 'twotone',
        'matrix':[
            [0,0,0,  9,0,0,  0,0,4],
            [0,0,7,  0,2,0,  0,3,0],
            [1,0,0,  7,0,5,  0,0,9],

            [0,8,0,  0,0,0,  0,9,0],
            [7,0,9,  0,1,0,  3,0,2],
            [0,6,0,  0,0,0,  0,1,0],

            [9,0,0,  4,0,2,  0,0,8],
            [0,4,0,  0,8,0,  9,0,0],
            [2,0,0,  0,0,6,  0,0,0]
        ],
        'group': [
            [0,0,0,  0,0,1,  1,0,0],
            [0,1,0,  1,0,0,  0,0,0],
            [0,0,1,  0,1,0,  0,0,0],

            [0,0,0,  1,0,0,  0,0,2],
            [0,1,0,  0,0,0,  0,2,0],
            [1,0,0,  0,0,2,  0,0,0],

            [0,0,0,  0,2,0,  2,0,0],
            [0,0,0,  0,0,2,  0,2,0],
            [0,0,2,  2,0,0,  0,0,0]
        ]
    }

    values={
        'type': 'zigzag',
        'matrix': [
            [0,5,0,  7,0,1,  0,2,0],
            [0,0,3,  0,2,0,  9,0,0],
            [0,3,0,  0,0,0,  0,7,0],

            [7,0,0,  2,0,9,  0,0,3],
            [0,4,5,  0,0,0,  1,9,0],
            [6,0,0,  9,0,4,  0,0,1],

            [3,0,6,  0,9,0,  4,0,5],
            [0,7,0,  4,0,6,  0,1,0],
            [1,0,0,  0,8,0,  0,0,2]
        ],
        'group': [
            [1,1,1,  1,2,3,  3,3,3],
            [4,1,2,  2,2,2,  2,3,5],
            [4,1,1,  1,2,3,  3,3,5],

            [4,4,4,  1,2,3,  5,5,5],
            [4,6,4,  4,2,5,  5,9,5],
            [6,6,6,  4,7,5,  9,9,9],

            [6,7,7,  7,7,7,  7,7,9],
            [6,8,8,  8,7,8,  8,8,9],
            [6,6,6,  8,8,8,  9,9,9]
        ]
    }

    """
    values={
        'type': 'chain',
        'matrix': [
            [1,0,0,  0,0,0],
            [0,0,0,  0,0,1],
            [4,0,0,  0,0,0],

            [0,0,6,  0,0,2],
            [0,0,0,  0,0,0],
            [5,0,0,  3,0,0]
        ],
        'group': [
            [[0,0], [0,1], [1,1], [2,0], [2,2], [3,3]],
            [[0,3], [0,4], [0,5], [1,4], [2,3], [2,5]],
            [[1,0], [2,1], [1,2], [3,0], [3,2], [4,1]],

            [[0,2], [1,3], [2,4], [1,5], [3,5], [4,4]],
            [[3,1], [4,0], [5,0], [5,1], [5,2], [4,2]],
            [[3,4], [4,3], [5,3], [5,4], [5,5], [4,5]]
        ]
    }

    values={
        'type': 'inequal',
        'matrix': [
            [0,0,0,  0,0,0],
            [0,0,0,  2,0,0],
            [0,0,0,  0,2,0],

            [0,6,0,  0,0,0],
            [0,0,6,  0,0,0],
            [0,0,0,  0,0,0]
        ],
        'group':[
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
    }

    values={
        'type': 'abs1',
        'matrix': [
            [0,1,0,  8,0,0,  0,0,0],
            [0,0,0,  2,3,7,  0,5,0],
            [0,5,2,  0,0,0,  0,0,4],

            [0,0,0,  7,0,0,  0,0,8],
            [0,0,1,  0,0,0,  4,0,0],
            [5,0,0,  0,0,6,  0,0,0],

            [6,0,0,  0,0,0,  8,1,0],
            [0,3,0,  5,7,8,  0,0,0],
            [0,0,0,  0,0,9,  0,4,0]
        ],
        'group': [
            [[0,0],[1,0]],  [[0,2],[1,2]],  [[0,2],[0,3]],  [[0,4],[0,5]],  [[0,7],[0,8]],
            [[0,8],[1,8]],  [[1,1],[2,1]],  [[2,0],[3,0]],  [[2,1],[3,1]],  [[2,3],[3,3]],
            [[2,6],[2,7]],  [[3,6],[3,7]],  [[3,4],[4,4]],  [[4,0],[4,1]],  [[4,4],[4,5]],
            [[4,5],[4,6]],  [[4,7],[4,8]],  [[4,7],[4,8]],  [[5,1],[5,2]],  [[5,2],[5,3]],
            [[5,3],[6,3]],  [[6,3],[6,4]],  [[6,8],[7,8]],  [[7,0],[8,0]],  [[7,1],[7,2]],
            [[6,2],[7,2]],  [[7,2],[7,3]],  [[7,4],[8,4]],  [[8,1],[8,2]],  [[8,6],[8,7]],
            [[8,7],[8,8]]
        ]
    }

    values = {
        'type':'cross',
        'matrix':[
            [0,1,0,  0,5,0,  0,2,0],
            [5,0,0,  6,0,3,  0,0,7],
            [0,3,0,  0,0,0,  0,1,0],

            [7,0,0,  0,0,0,  0,0,2],
            [0,5,0,  2,0,4,  0,9,0],
            [0,2,0,  0,0,0,  0,8,0],

            [4,0,0,  0,0,0,  0,0,5],
            [9,0,0,  5,0,2,  0,0,8],
            [0,7,5,  0,4,0,  9,3,0]
        ]
    }


    values={
        'type':'sudoku',
        'matrix':[
            [0,1,0,  0,5,0,  0,2,0],
            [5,0,0,  6,0,3,  0,0,7],
            [0,3,0,  0,0,0,  0,1,0],

            [7,0,0,  0,0,0,  0,0,2],
            [0,5,0,  2,0,4,  0,9,0],
            [0,2,0,  0,0,0,  0,8,0],

            [4,0,0,  0,0,0,  0,0,5],
            [9,0,0,  5,0,2,  0,0,8],
            [0,7,5,  0,4,0,  9,3,0]
        ]
    }
    """

    main(values)