# Python module

## Sudoku

author: Shinjo Sato

date: 2020/09/05

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
