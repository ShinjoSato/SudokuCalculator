class Sudoku{
    constructor(){}

    start(matrix){
        return this.fillMatrixIntoNumbers(
            matrix, 
            this.searchLackingNumbers(matrix), 
            this.searchEmptyPlaces(matrix),
            3
        );
    }

    searchLackingNumbers(matrix){
        let stack=[];
        for(let i of matrix)
            for(let j of i)
                if(j!=0)
                    stack.push(j);
        let stack_all=[];
        const num_limit = matrix.length;
        const pack_num = Math.floor(matrix.length * matrix[0].length / num_limit);
        for(let i=1; i<1+num_limit; i++)
            for(let j=0; j<pack_num; j++)
                stack_all.push(i)
        for(let i of stack)
            stack_all=this.removeNumFromList(i,stack_all)
        return stack_all;
    }

    removeNumFromList(num,list){
        for(let i=0; i<list.length; i++)
            if(num==list[i]){
                list.splice(i,1);
                break;
            }
        return list;
    }

    canPutNumberOnPlace(place, matrix, num){
        let stack=[];
        //columns
        for(let p=0; p<matrix.length; p++)
            stack.push( matrix[p][place[1]] );
        //rows
        for(let q=0; q<matrix[place[0]].length; q++)
            stack.push( matrix[place[0]][q] );
        //MxN
        const height=Math.floor(Math.sqrt(matrix.length)),
            width=Math.ceil(Math.sqrt(matrix[0].length)),
            I=Math.floor(place[0]/height)*height,
            J=Math.floor(place[1]/width)*width;
        for(let p=I; p<I+height; p++)
            for(let q=J; q<J+width; q++)
                stack.push(matrix[p][q]);
        //remove duplication numbers
        stack.filter(function(x,i,self){
            return self.indexOf(x)===i;
        });
        return (stack.indexOf(num)==-1)? true: false;
    }

    searchEmptyPlaces(matrix){
        let places=[];
        for(let i=0;i<matrix.length; i++)
            for(let j=0;j<matrix[i].length; j++)
                if(matrix[i][j]==0)
                    places.push([i,j]);
        return places
    }

    printMatrix(matrix){
        for(let rows of matrix)
            console.log(rows);
    }

    fillMatrixIntoNumbers(matrix, numbers, places, range){
        if(numbers.length==0){
            this.printMatrix(matrix);
            return matrix;
        }else{
            for(let place of places){
                let initial=0;
                let candidate=[];
                for(let num of numbers){
                    if(initial!=num){
                        initial=num;
                        if(this.canPutNumberOnPlace(place,matrix,num))
                            candidate.push(num)
                    }
                }
                if(candidate.length<range){
                    for(let c of candidate){
                        //Insert a number
                        let idx_place=places.indexOf(place);
                        let idx_num=numbers.indexOf(c);
                        places.splice(places.indexOf(place), 1);
                        numbers.splice(numbers.indexOf(c), 1);
                        matrix[place[0]][place[1]]=c;
                        //Recursion
                        let result=this.fillMatrixIntoNumbers(matrix, numbers, places, range);
                        if(0<result.length)
                            return result;
                        //Remove a  number
                        matrix[place[0]][place[1]]=0;
                        numbers.splice(idx_num, 0, c);
                        places.splice(idx_place, 0, place);
                    }
                    return [];
                }
            }
            return [];
        }
    }

    compareListWithList(list_a, list_b){
        if(list_a.length==list_b.length)
            for(let i=0; i<list_a.length; i++){
                if(list_a[i]!=list_b[i])
                    return false;
            }
        else
            return false;
        return true;
    }

    containList(list_all, list){
        for(all of list_all){
            if(compareListWithList(all,list))
                return true;
        }
        return false;
    }

    indexOfListInSets(sets, list){
        let index=0;
        for(let s of sets){
            if(s[0]==list[0]&&s[1]==list[1])
                return index;
            else
                index+=1;
        }
        return -1;
    }
}


class Duplication extends Sudoku {
    constructor(){
        super();
    }

    start(matrix, groups){
        return this.fillMatrixesIntoNumbers(
            matrix, 
            this.searchLackingNumbersSet(matrix), 
            this.searchEmptyPlacesSet(matrix),
            groups
        );
    }

    searchLackingNumbersSet(matrixes){
        let numbersSet=[];
        for(let matrix of matrixes){
            numbersSet.push(super.searchLackingNumbers(matrix));
        }
        return numbersSet;
    }

    canPutNumberOnDuplicationPlace(place, matrixes, id, num, duplications){
        if(!super.canPutNumberOnPlace(place,matrixes[id],num))
            return false;
        if(0<duplications[id][place[0]][place[1]].length)
            for(let g=0; g<duplications[id][place[0]][place[1]].length; g++)
                //the size of matrix < num
                if(matrixes[ duplications[id][place[0]][place[1]][g][0] ].length <num)
                    return false
        for(let i=0; i<duplications[id][place[0]][place[1]].length; i++){
            let matrix_id=duplications[id][place[0]][place[1]][i][0];
            let dup_place=[duplications[id][place[0]][place[1]][i][1], duplications[id][place[0]][place[1]][i][2]];
            if(!super.canPutNumberOnPlace(dup_place, matrixes[matrix_id], num))
                return false;
        }
        return true;
    }

    searchEmptyPlacesSet(matrixes){
        let placesSet=[];
        for(let matrix of matrixes){
            placesSet.push(super.searchEmptyPlaces(matrix));
        }
        return placesSet;
    }

    fillMatrixesIntoNumbers(matrixes, numbersSet, placesSet, duplications){
        let len_numbers=0;
        for(let numbers of numbersSet){
            len_numbers+=numbers.length
        }
        if(len_numbers==0){
            return matrixes;
        }else{
            //iはcandidateの個数の閾値で、選択肢が少ないところを深掘りさせるためのfor文
            for(let i=0; i<placesSet.length; i++){
                for(let place of placesSet[i]){
                    let initial=0;
                    let candidate=[];
                    for(let num of numbersSet[i]){
                        if(initial != num){
                            initial=num;
                            if(this.canPutNumberOnDuplicationPlace(place, matrixes, i, num, duplications))
                                candidate.push(num);
                        }
                    }
                    if(candidate.length<3){
                        for(let c of candidate){
                            let idx_place=placesSet[i].indexOf(place);
                            let idx_num=numbersSet[i].indexOf(c);
                            placesSet[i].splice(placesSet[i].indexOf(place), 1);
                            numbersSet[i].splice(numbersSet[i].indexOf(c),1);
                            matrixes[i][place[0]][place[1]]=c;
                            //重複されているなら
                            if(0<duplications[i][place[0]][place[1]].length){
                                //重複箇所に加える
                                let dup_matrix_id_list=[];
                                let dup_place_list=[];
                                let idx_dup_place_list=[];
                                let idx_dup_num_list=[];
                                for(let g=0; g<duplications[i][place[0]][place[1]].length; g++){
                                    dup_matrix_id_list.push(duplications[i][place[0]][place[1]][g][0]);
                                    dup_place_list.push([duplications[i][place[0]][place[1]][g][1], duplications[i][place[0]][place[1]][g][2]]);
                                    idx_dup_place_list.push(super.indexOfListInSets(placesSet[dup_matrix_id_list[g]], dup_place_list[g]));
                                    idx_dup_num_list.push(numbersSet[dup_matrix_id_list[g]].indexOf(c));
                                }
                                
                                for(let g=0; g<duplications[i][place[0]][place[1]].length; g++){
                                    placesSet[dup_matrix_id_list[g]].splice(super.indexOfListInSets(placesSet[dup_matrix_id_list[g]], dup_place_list[g]), 1);
                                    numbersSet[dup_matrix_id_list[g]].splice(numbersSet[dup_matrix_id_list[g]].indexOf(c),1 );
                                    matrixes[dup_matrix_id_list[g]][dup_place_list[g][0]][dup_place_list[g][1]]=c;
                                }
                                //Recursion
                                let result=this.fillMatrixesIntoNumbers(matrixes, numbersSet, placesSet, duplications);
                                if(0<result.length)
                                    return result;
                                //重複箇所のを省く
                                for(let g=0; g<duplications[i][place[0]][place[1]].length; g++){
                                    matrixes[dup_matrix_id_list[g]][dup_place_list[g][0]][dup_place_list[g][1]]=0;
                                    numbersSet[dup_matrix_id_list[g]].splice(idx_dup_num_list[g], 0, c);
                                    placesSet[dup_matrix_id_list[g]].splice(idx_dup_place_list[g],0,dup_place_list[g]);
                                }
                            }else{
                                //Recursion
                                let result=this.fillMatrixesIntoNumbers(matrixes, numbersSet, placesSet, duplications);
                                if(0<result.length)
                                    return result;
                            }
                            matrixes[i][place[0]][place[1]]=0;
                            numbersSet[i].splice(idx_num, 0, c);
                            placesSet[i].splice(idx_place, 0, place);
                        }
                        return [];
                    }
                }
            }
            return [];
        }
    }
}


let matrixes=[
    [//1
        [2,0,0,  5,0,0],
        [0,5,0,  0,0,3],

        [0,0,0,  0,5,0],
        [0,4,6,  0,0,2],

        [6,0,0,  1,0,0],
        [0,0,0,  0,0,0]
    ],[//2
        [0,0,0,  0,7,0,  0,0,0],
        [1,0,0,  4,0,9,  0,5,0],
        [0,0,5,  0,0,0,  0,0,8],

        [0,2,0,  0,5,0,  9,0,1],
        [5,0,4,  0,0,6,  8,0,0],
        [3,0,0,  1,0,0,  0,6,0],

        [0,5,0,  0,6,0,  0,0,9],
        [0,0,2,  7,0,4,  0,0,0],
        [4,3,0,  0,1,0,  0,0,0]
    ],[//3
        [7,0,9,  0,8,0,  0,2,0],
        [4,0,0,  3,0,6,  9,0,0],
        [0,1,0,  0,0,7,  0,5,6],

        [9,0,1,  0,7,0,  5,0,0],
        [0,5,0,  6,0,0,  1,0,8],
        [0,0,8,  0,0,5,  0,4,0],

        [5,0,0,  0,1,0,  0,0,0],
        [8,0,6,  7,0,0,  4,0,0],
        [0,0,0,  2,0,8,  0,0,0]
    ],[//4
        [0,0,0,  7,0,2,  0,0,0],
        [0,0,0,  0,1,0,  7,0,0],
        [0,0,4,  0,8,3,  0,0,0],

        [0,2,0,  1,0,0,  6,0,4],
        [0,0,1,  0,9,4,  0,3,0],
        [0,3,0,  5,0,0,  8,0,0],

        [0,0,2,  0,0,0,  1,7,0],
        [0,0,0,  2,0,8,  0,0,9],
        [0,5,7,  0,6,0,  3,0,0]
    ],[//5
        [7,3,0,  0,0,4,  0,0,0],
        [0,0,9,  2,0,0,  1,0,0],
        [6,0,0,  0,9,0,  7,0,0],

        [0,5,0,  9,1,0,  6,0,0],
        [0,9,6,  0,0,8,  0,7,0],
        [1,8,0,  3,0,0,  0,0,0],

        [0,7,4,  0,5,0,  8,0,0],
        [9,0,0,  0,8,2,  0,1,0],
        [0,0,8,  7,0,0,  4,0,2]
    ],[//6
        [0,0,12,0,    11,0,0,3,   0,10,0,0],
        [0,0,4,6,      0,0,0,0,    2,11,0,0],
        [0,0,0,11,    0,4,2,0,    12,0,0,0],

        [11,0,3,0,    5,0,0,1,    0,4,0,10],
        [0,12,0,0,    4,0,0,2,    0,0,6,0],
        [10,0,0,4,    0,9,7,0,    1,0,0,3],

        [0,10,0,0,    3,0,0,5,    0,0,2,0],
        [0,0,8,9,    0,0,0,0,    3,6,0,0],
        [7,11,0,0,    0,12,6,0,   0,0,10,5],

        [0,0,0,12,    0,7,4,0,    10,0,0,0],
        [0,0,9,0,    6,0,0,12,    0,8,0,0],
        [0,0,0,5,    0,11,3,0,    6,0,0,0]
    ],[//7
        [0,5,0,  0,1,0,  2,0,7],
        [0,0,7,  4,0,2,  0,0,5],
        [6,2,0,  7,0,0,  0,9,0],

        [0,0,1,  0,4,0,  3,0,2],
        [9,0,6,  0,0,5,  0,8,0],
        [0,4,0,  3,0,0,  9,0,0],

        [0,0,0,  0,7,0,  0,0,3],
        [0,0,2,  0,0,1,  4,0,6],
        [0,0,0,  6,0,4,  0,0,0]
    ],[//8
        [0,0,0,  1,0,7,  0,0,0],
        [0,0,8,  0,2,0,  0,0,0],
        [0,0,0,  8,3,0,  1,0,0],

        [3,0,7,  0,0,6,  0,2,0],
        [0,1,0,  7,5,0,  6,0,0],
        [0,0,9,  0,0,8,  0,4,0],

        [0,9,1,  0,0,0,  2,0,0],
        [4,0,0,  2,0,9,  0,0,0],
        [0,0,2,  0,7,0,  3,5,0]
    ],[//9
        [0,0,0,  0,4,0,  0,0,0],
        [0,7,0,  2,0,3,  0,0,9],
        [3,0,0,  0,0,0,  4,0,0],

        [5,0,3,  0,2,0,  0,8,0],
        [0,0,8,  3,0,0,  9,0,1],
        [0,9,0,  0,0,6,  0,0,5],

        [7,0,0,  0,3,0,  0,4,0],
        [0,0,0,  1,0,2,  5,0,0],
        [0,0,0,  0,6,0,  0,1,7]
    ],[//10
        [0,0,5,  0,0,1],
        [4,0,0,  0,5,0],

        [0,2,0,  0,0,0],
        [1,0,0,  2,4,0],

        [0,0,2,  0,0,5],
        [0,0,0,  0,0,0]
    ],[//11
        [0,0,0,  9,0,0,  0,7,3],
        [0,0,9,  0,0,1,  4,0,0],
        [0,0,5,  0,4,0,  0,0,6],

        [0,0,2,  0,1,9,  0,8,0],
        [0,1,0,  4,0,0,  2,9,0],
        [0,0,0,  0,0,7,  0,4,1],

        [0,0,1,  0,3,0,  7,5,0],
        [0,3,0,  1,9,0,  0,0,4],
        [2,0,4,  0,0,5,  1,0,0]
    ]
]
let duplications=[
    [//1
        [[],[],[],  [],[],[]],
        [[],[],[],  [],[],[]],

        [[],[],[],  [],[],[]],
        [[],[],[],  [],[],[]],

        [[],[],[],  [],[],[]],
        [[],[],[[1,0,0]],  [[1,0,1]],[[1,0,2]],[[1,0,3]]],
    ],[//2
        [[[0,5,2]],[[0,5,3]],[[0,5,4]],  [[0,5,5]],[],[],  [[2,8,0]],[[2,8,1]],[[2,8,2]]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [[3,0,0]],[[3,0,1]],[[3,0,2]]],
        [[],[],[],  [],[],[],  [[3,1,0]],[[3,1,1]],[[3,1,2]]]
    ],[//3
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[[5,0,0]],[[5,0,1]]],
        [[],[],[],  [],[],[],  [],[[5,1,0]],[[5,1,1]]],
        [[[1,0,6]],[[1,0,7]],[[1,0,8]],  [],[],[],  [],[[5,2,0]],[[5,2,1]]]
    ],[//4
        [[[1,7,6]],[[1,7,7]],[[1,7,8]],  [],[],[],  [],[[5,9,0]],[[5,9,1]]],
        [[[1,8,6]],[[1,8,7]],[[1,8,8]],  [],[],[],  [],[[5,10,0]],[[5,10,1]]],
        [[],[],[],  [],[],[],  [],[[5,11,0]],[[5,11,1]]],

        [[[4,0,8]],[],[],  [],[],[],  [],[],[]],
        [[[4,1,8]],[],[],  [],[],[],  [],[],[]],
        [[[4,2,8]],[],[],  [],[],[],  [],[],[]],

        [[[4,3,8]],[],[],  [],[],[],  [],[],[]],
        [[[4,4,8]],[],[],  [],[],[],  [],[],[]],
        [[[4,5,8]],[],[],  [],[],[],  [],[],[]]
    ],[//5
        [[],[],[],  [],[],[],  [],[],[[3,3,0]]],
        [[],[],[],  [],[],[],  [],[],[[3,4,0]]],
        [[],[],[],  [],[],[],  [],[],[[3,5,0]]],

        [[],[],[],  [],[],[],  [],[],[[3,6,0]]],
        [[],[],[],  [],[],[],  [],[],[[3,7,0]]],
        [[],[],[],  [],[],[],  [],[],[[3,8,0]]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]]
    ],[//6
        [[[2,6,7]],[[2,6,8]],[],[],   [],[],[],[],   [],[],[[6,6,0]],[[6,6,1]]],
        [[[2,7,7]],[[2,7,8]],[],[],   [],[],[],[],   [],[],[[6,7,0]],[[6,7,1]]],
        [[[2,8,7]],[[2,8,8]],[],[],   [],[],[],[],   [],[],[[6,8,0]],[[6,8,1]]],

        [[],[],[],[],   [],[],[],[],   [],[],[],[]],
        [[],[],[],[],   [],[],[],[],   [],[],[],[]],
        [[],[],[],[],   [],[],[],[],   [],[],[],[]],

        [[],[],[],[],   [],[],[],[],   [],[],[],[]],
        [[],[],[],[],   [],[],[],[],   [],[],[],[]],
        [[],[],[],[],   [],[],[],[],   [],[],[],[]],

        [[[3,0,7]],[[3,0,8]],[],[],   [],[],[],[],   [],[],[[7,0,0]],[[7,0,1]]],
        [[[3,1,7]],[[3,1,8]],[],[],   [],[],[],[],   [],[],[[7,1,0]],[[7,1,1]]],
        [[[3,2,7]],[[3,2,8]],[],[],   [],[],[],[],   [],[],[[7,2,0]],[[7,2,1]]]
    ],[//7
        [[],[],[],  [],[],[], [],[],[]],
        [[],[],[],  [],[],[], [],[],[]],
        [[],[],[],  [],[],[], [],[],[]],

        [[],[],[],  [],[],[], [],[],[]],
        [[],[],[],  [],[],[], [],[],[]],
        [[],[],[],  [],[],[], [],[],[]],

        [[[5,0,10]],[[5,0,11]],[],  [],[],[], [],[],[]],
        [[[5,1,10]],[[5,1,11]],[],  [],[],[], [],[],[]],
        [[[5,2,10]],[[5,2,11]],[],  [],[],[], [[8,0,0]],[[8,0,1]],[[8,0,2]]]
    ],[//8
        [[[5, 9,10]],[[5, 9,11]],[],  [],[],[],  [[8,7,0]],[[8,7,1]],[[8,7,2]]],
        [[[5,10,10]],[[5,10,11]],[],  [],[],[],  [[8,8,0]],[[8,8,1]],[[8,8,2]]],
        [[[5,11,10]],[[5,11,11]],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[[10,0,0]]],
        [[],[],[],  [],[],[],  [],[],[[10,1,0]]],
        [[],[],[],  [],[],[],  [],[],[[10,2,0]]],

        [[],[],[],  [],[],[],  [],[],[[10,3,0]]],
        [[],[],[],  [],[],[],  [],[],[[10,4,0]]],
        [[],[],[],  [],[],[],  [],[],[[10,5,0]]]
    ],[//9
        [[[6,8,6]],[[6,8,7]],[[6,8,8]],  [],[],[[9,5,0]],  [[9,5,1]],[[9,5,2]],[[9,5,3]]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[[7,0,6]],[[7,0,7]],[[7,0,8]],  [],[],[],  [],[],[]],
        [[[7,1,6]],[[7,1,7]],[[7,1,8]],  [],[],[],  [],[],[]]
    ],[//10
        [[],[],[],  [],[],[]],
        [[],[],[],  [],[],[]],

        [[],[],[],  [],[],[]],
        [[],[],[],  [],[],[]],

        [[],[],[],  [],[],[]],
        [[[8,0,5]],[[8,0,6]],[[8,0,7]],  [[8,0,8]],[],[]]
    ],[//11
        [[[7,3,8]],[],[],  [],[],[],  [],[],[]],
        [[[7,4,8]],[],[],  [],[],[],  [],[],[]],
        [[[7,5,8]],[],[],  [],[],[],  [],[],[]],

        [[[7,6,8]],[],[],  [],[],[],  [],[],[]],
        [[[7,7,8]],[],[],  [],[],[],  [],[],[]],
        [[[7,8,8]],[],[],  [],[],[],  [],[],[]],

        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]],
        [[],[],[],  [],[],[],  [],[],[]]
    ]
]

let s= new Duplication();
let result=s.start(matrixes,duplications);
if(result.length!=0)
    console.log("SUCCESS");
else
    console.log("FAIL");
console.log(result);