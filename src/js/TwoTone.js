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
}



class TwoTone extends Sudoku{
    constructor(){
        super();
    }

    start(matrix, twotone){
        return this.fillMatrixIntoNumbers(
            matrix, 
            this.searchLackingNumbers(matrix), 
            this.searchEmptyPlaces(matrix),
            twotone
        );
    }

    canPutNumberOnPlace(place, matrix, num, twotone){
        let stack = []
        //twotone
        //console.log(twotone);
        if(0<twotone[place[0]][place[1]])
            for(let i=0; i<twotone.length; i++){
                for(let j=0; j<twotone[i].length; j++){
                    if(twotone[place[0]][place[1]] == twotone[i][j])
                        stack.push( matrix[i][j] )
                }
            }
        stack.filter(function(x,i,self){
            return self.indexOf(x)===i;
        });
        return (stack.indexOf(num)==-1 && super.canPutNumberOnPlace(place, matrix, num))? true: false;
    }

    fillMatrixIntoNumbers(matrix, numbers, places, groups){
        if(numbers.length==0){
            super.printMatrix(matrix)
            return matrix
        }else{
            //iはcandidateの個数の閾値で、選択肢が少ないところを深掘りさせるためのfor文
            for(let place of places){
                let initial=0;
                let candidate=[];
                for(let num of numbers){
                    if(initial != num){
                        initial=num;
                        if(this.canPutNumberOnPlace(place, matrix, num, groups))
                            candidate.push(num);
                    }
                }
                if(candidate.length<4){
                    for(let c of candidate){
                        //Insert a number
                        let idx_place=places.indexOf(place);
                        let idx_num=numbers.indexOf(c);
                        places.splice(places.indexOf(place), 1);
                        numbers.splice(numbers.indexOf(c), 1);
                        matrix[place[0]][place[1]]=c;
                        //Recursion
                        let result=this.fillMatrixIntoNumbers(matrix, numbers, places, groups);
                        if(0<result.length)
                            return result;
                        //Remove a  number
                        matrix[place[0]][place[1]]=0;
                        numbers.splice(idx_num, 0, c);
                        places.splice(idx_place, 0, place);
                    }
                    return []
                }
            }
            return []
        }
    }
}


let matrix = [
    [0,0,0,  9,0,0,  0,0,4],
    [0,0,7,  0,2,0,  0,3,0],
    [1,0,0,  7,0,5,  0,0,9],

    [0,8,0,  0,0,0,  0,9,0],
    [7,0,9,  0,1,0,  3,0,2],
    [0,6,0,  0,0,0,  0,1,0],

    [9,0,0,  4,0,2,  0,0,8],
    [0,4,0,  0,8,0,  9,0,0],
    [2,0,0,  0,0,6,  0,0,0]
];

let twotone = [
    [0,0,0,  0,0,1,  1,0,0],
    [0,1,0,  1,0,0,  0,0,0],
    [0,0,1,  0,1,0,  0,0,0],

    [0,0,0,  1,0,0,  0,0,2],
    [0,1,0,  0,0,0,  0,2,0],
    [1,0,0,  0,0,2,  0,0,0],

    [0,0,0,  0,2,0,  2,0,0],
    [0,0,0,  0,0,2,  0,2,0],
    [0,0,2,  2,0,0,  0,0,0]
];


console.log(matrix);
let s= new TwoTone();
let result=s.start(matrix,twotone);
if(result.length!=0)
    console.log("SUCCESS");
else
    console.log("FAIL");
console.log(result);