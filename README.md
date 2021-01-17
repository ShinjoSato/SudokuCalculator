# Sudoku Calculator

## Profile

author: Shinjo Sato

start: 2020/09/05

latest: 2020/12/19

# Colors
- Square ![](https://via.placeholder.com/16/5e9e5e/FFFFFF/?text=%20) `#5e9e5e`
- Border color (except out frame) ![](https://via.placeholder.com/16/e0e0e0/FFFFFF/?text=%20) `#e0e0e0`
- Out frame color ![](https://via.placeholder.com/16/bbbbbb/FFFFFF/?text=%20) `#bbbbbb`

# ToDo

1. Implimenting sudoku calculator program in Javascript to distribute to customers whose computer doesn't include Python.

## Detail

The class plays Sudoku Puzzles.

- Strategy
    1. Finding the all lacking numbers in the Sudoku Puzzle.
    2. Finding all places which are empty or contain 0 respectively.
    3. For each empty places, checking numbers which can be put on the place according to the Sudoku rule and add the numbers into a list. If the length of the list is smaller than 5, input a number in the list into the place in order and start Strategy 3 recursively.
    4. If the Sudoku puzzle is completed, the final state shows.

- Classes

    |function|argument|return|description|
    |:-|:-|:-|:-|
    |$canPutNumbersOnPlace$|$place$:int[2], $matrix$:int[8][8]; $num$:int|boolean|It check whether $num$ can be put on $place$ in $matrix$ then return $True$ if it's possible; $False$ if it's impossible.|
    |$fillMatrixIntoNumbers$|$matrix$:int[8][8], $numbers$:int[], $places$:list[int[2]]|void|It fills $matrix$ into $numbers$ on $places$ according to $canPutNumbersOnPlaces$.|
    |$searchLackingNumbers$|$matrix$:int[8][8]|int[]|It search lacking numbers in $matrix$ then return the list of the number|

- Input

    ```txt:data
    [ [6,4,0,  0,0,0,  0,1,7],
    [2,0,0,  0,0,0,  0,0,6],
    [0,0,0,  0,3,0,  0,0,0],

    [0,1,0,  5,0,8,  0,2,0],
    [0,0,7,  0,0,0,  6,0,0],
    [0,2,0,  9,0,4,  0,8,0],

    [0,0,0,  0,9,0,  0,0,0],
    [1,0,0,  0,0,0,  0,0,9],
    [9,5,0,  0,0,0,  0,4,2] ]
    ```

    ```sh
    $time python3 Sudoku.py
    ```

- Output

    ```txt
    6  4  3  2  8  9  5  1  7  
    2  8  9  7  5  1  4  3  6  
    5  7  1  4  3  6  2  9  8  
    4  1  6  5  7  8  9  2  3  
    8  9  7  1  2  3  6  5  4  
    3  2  5  9  6  4  7  8  1  
    7  3  4  8  9  2  1  6  5  
    1  6  2  3  4  5  8  7  9  
    9  5  8  6  1  7  3  4  2  
    SUCCESS!!

    real    6m43.540s
    user    6m42.137s
    sys     0m0.309s
    ```

## Server Note

## Command

```sh
#Sudoku
curl -XPOST 'http://localhost:3333/test' -d '{"type": "sudoku","matrix":[[0,1,0,  0,5,0,  0,2,0],[5,0,0,  6,0,3,  0,0,7],[0,3,0,  0,0,0,  0,1,0],[7,0,0,  0,0,0,  0,0,2],[0,5,0,  2,0,4,  0,9,0],[0,2,0,  0,0,0,  0,8,0],[4,0,0,  0,0,0,  0,0,5],[9,0,0,  5,0,2,  0,0,8],[0,7,5,  0,4,0,  9,3,0]]}'

#Duplication
curl -XPOST 'http://localhost:3333/test' -d '{"type": "duplicate", "matrix": [[[6,0,1,  0,0,3,  0,0,5],[0,5,0,  1,9,0,  8,0,0],[3,0,0,  0,7,0,  0,0,9],[0,0,3,  0,0,9,  0,6,0],[1,0,6,  0,3,0,  0,5,2],[0,4,0,  6,0,1,  0,0,0],[8,3,0,  0,6,0,  0,0,0],[0,0,5,  0,0,7,  0,0,0],[2,0,0,  3,0,0,  0,0,0]],[[0,0,0,  0,0,6,  0,0,8],[0,0,0,  2,0,0,  5,0,0],[0,0,0,  0,1,0,  0,9,6],[0,0,0,  1,0,8,  0,6,0],[1,3,0,  0,7,0,  8,0,9],[0,7,0,  6,0,0,  1,0,0],[4,0,0,  0,6,0,  0,0,5],[0,0,5,  0,9,1,  0,4,0],[2,0,0,  8,0,0,  3,0,1]]], "group": [[[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [1,0,0],[1,0,1],[1,0,2]],[[],[],[],  [],[],[],  [1,1,0],[1,1,1],[1,1,2]],[[],[],[],  [],[],[],  [1,2,0],[1,2,1],[1,2,2]]],[[[0,6,6],[0,6,7],[0,6,8],  [],[],[],  [],[],[]],[[0,7,6],[0,7,7],[0,7,8],  [],[],[],  [],[],[]],[[0,8,6],[0,8,7],[0,8,8],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]],[[],[],[],  [],[],[],  [],[],[]]]]}'

#Abs1
curl -XPOST 'http://localhost:3333/test' -d '{"type":"abs1", "matrix":[[0,1,0,  8,0,0,  0,0,0],[0,0,0,  2,3,7,  0,5,0],[0,5,2,  0,0,0,  0,0,4],[0,0,0,  7,0,0,  0,0,8],[0,0,1,  0,0,0,  4,0,0],[5,0,0,  0,0,6,  0,0,0],[6,0,0,  0,0,0,  8,1,0],[0,3,0,  5,7,8,  0,0,0],[0,0,0,  0,0,9,  0,4,0]],"group":[[[0,0],[1,0]],  [[0,2],[1,2]],  [[0,2],[0,3]],  [[0,4],[0,5]],  [[0,7],[0,8]],[[0,8],[1,8]],  [[1,1],[2,1]],  [[2,0],[3,0]],  [[2,1],[3,1]],  [[2,3],[3,3]],[[2,6],[2,7]],  [[3,6],[3,7]],  [[3,4],[4,4]],  [[4,0],[4,1]],  [[4,4],[4,5]],[[4,5],[4,6]],  [[4,7],[4,8]],  [[4,7],[4,8]],  [[5,1],[5,2]],  [[5,2],[5,3]],[[5,3],[6,3]],  [[6,3],[6,4]],  [[6,8],[7,8]],  [[7,0],[8,0]],  [[7,1],[7,2]],[[6,2],[7,2]],  [[7,2],[7,3]],  [[7,4],[8,4]],  [[8,1],[8,2]],  [[8,6],[8,7]],[[8,7],[8,8]]]}'

#Chain
curl -XPOST 'http://localhost:3333/test' -d '{"type": "chain", "matrix": [[1,0,0,  0,0,0],[0,0,0,  0,0,1],[4,0,0,  0,0,0],[0,0,6,  0,0,2],[0,0,0,  0,0,0],[5,0,0,  3,0,0]],"group":[[[0,0], [0,1], [1,1], [2,0], [2,2], [3,3]],[[0,3], [0,4], [0,5], [1,4], [2,3], [2,5]],[[1,0], [2,1], [1,2], [3,0], [3,2], [4,1]],[[0,2], [1,3], [2,4], [1,5], [3,5], [4,4]],[[3,1], [4,0], [5,0], [5,1], [5,2], [4,2]],[[3,4], [4,3], [5,3], [5,4], [5,5], [4,5]]]}'

#Cross
curl -XPOST 'http://localhost:3333/test' -d '{"type":"cross","matrix":[[0,1,0,  0,5,0,  0,2,0],[5,0,0,  6,0,3,  0,0,7],[0,3,0,  0,0,0,  0,1,0],[7,0,0,  0,0,0,  0,0,2],[0,5,0,  2,0,4,  0,9,0],[0,2,0,  0,0,0,  0,8,0],[4,0,0,  0,0,0,  0,0,5],[9,0,0,  5,0,2,  0,0,8],[0,7,5,  0,4,0,  9,3,0]]}'

#Inequality
curl -XPOST 'http://localhost:3333/test' -d '{"type":"inequal","matrix":[[0,0,0,  0,0,0],[0,0,0,  2,0,0],[0,0,0,  0,2,0],[0,6,0,  0,0,0],[0,0,6,  0,0,0],[0,0,0,  0,0,0]], "group":[[-1, 1, 1, -1, 1],[-1, 1, -1, -1, 1, -1],[1, -1, -1, 1, -1],[1, -1, 1, 1, -1, -1],[-1, 1, -1, -1, -1],[-1, 1, -1, 1, 1, 1],[1, -1, 1, -1, -1],[-1, -1, 1, -1, 1, 1],[-1, 1, -1, 1, -1],[1, 1, -1, -1, -1, 1],[-1, -1, -1, 1, 1]]}'

#TwoTone
curl -XPOST 'http://localhost:3333/test' -d '{"type":"twotone","matrix":[[0,0,0,  9,0,0,  0,0,4],[0,0,7,  0,2,0,  0,3,0],[1,0,0,  7,0,5,  0,0,9],[0,8,0,  0,0,0,  0,9,0],[7,0,9,  0,1,0,  3,0,2],[0,6,0,  0,0,0,  0,1,0],[9,0,0,  4,0,2,  0,0,8],[0,4,0,  0,8,0,  9,0,0],[2,0,0,  0,0,6,  0,0,0]],"group":[[0,0,0,  0,0,1,  1,0,0],[0,1,0,  1,0,0,  0,0,0],[0,0,1,  0,1,0,  0,0,0],[0,0,0,  1,0,0,  0,0,2],[0,1,0,  0,0,0,  0,2,0],[1,0,0,  0,0,2,  0,0,0],[0,0,0,  0,2,0,  2,0,0],[0,0,0,  0,0,2,  0,2,0],[0,0,2,  2,0,0,  0,0,0]]}'

#Zigzag
curl -XPOST 'http://localhost:3333/test' -d '{"type":"zigzag","matrix":[[0,5,0,  7,0,1,  0,2,0],[0,0,3,  0,2,0,  9,0,0],[0,3,0,  0,0,0,  0,7,0],[7,0,0,  2,0,9,  0,0,3],[0,4,5,  0,0,0,  1,9,0],[6,0,0,  9,0,4,  0,0,1],[3,0,6,  0,9,0,  4,0,5],[0,7,0,  4,0,6,  0,1,0],[1,0,0,  0,8,0,  0,0,2]],"group":[[1,1,1,  1,2,3,  3,3,3],[4,1,2,  2,2,2,  2,3,5],[4,1,1,  1,2,3,  3,3,5],[4,4,4,  1,2,3,  5,5,5],[4,6,4,  4,2,5,  5,9,5],[6,6,6,  4,7,5,  9,9,9],[6,7,7,  7,7,7,  7,7,9],[6,8,8,  8,7,8,  8,8,9],[6,6,6,  8,8,8,  9,9,9]]}'
```

O curl -XPOST 'http://localhost:3333/test' -d '{ "question": "Weather is" }'

X curl -XPOST 'http://localhost:3333/test' -d "{ 'question': 'Weather is' }"

### Check port numbers on MacOS
```sh
lsof -i -P | grep "LISTEN"
```

### Reference
- [[python3] 簡易サーバでJSONデータ受け渡し　[POST]](https://qiita.com/tkj/items/1338ad081038fa64cef8)
  

## Task

- Solve Question207 in src/CrossAddition.py.