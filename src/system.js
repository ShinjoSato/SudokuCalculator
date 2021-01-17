var grouplist=[], groups=[], options=[]; 
createInequalityHTML();
createInequalityGroup();

//Check current directory.
let currentWorkingDirectory = process.cwd();
console.log(currentWorkingDirectory);

/**
 * This sends three values: type, matrix and group to the server then receives the answer.
 */
function postMatrix(size){
    //Organize the data.
    var matrix=[];
    /*The line below is essential for the future version.
    if($('[name=rule]').val()=="inequal"){
        matrix=createInequalityMatrix();
        options=createInequalityGroup();
    }else{
        for(i=0; i<Math.sqrt($(".square .square div").length); i++)
            matrix.push([]);
        for(i=0; i<Math.sqrt($(".square .square div").length); i++)
            for(j=0; j<Math.sqrt($(".square .square div").length); j++){
                INDEX=Math.sqrt(matrix.length)*Math.floor(i/Math.sqrt(matrix.length))+Math.floor(j/Math.sqrt(matrix.length));
                matrix[INDEX].push(Number($(".square .square div").eq(matrix.length*i+j).text()));
            }
    }
    */
    for(i=0; i<Math.sqrt($(".square .square div").length); i++)
        matrix.push([]);
    for(i=0; i<Math.sqrt($(".square .square div").length); i++)
        for(j=0; j<Math.sqrt($(".square .square div").length); j++){
            INDEX=Math.sqrt(matrix.length)*Math.floor(i/Math.sqrt(matrix.length))+Math.floor(j/Math.sqrt(matrix.length));
            matrix[INDEX].push(Number($(".square .square div").eq(matrix.length*i+j).text()));
        }
    
    const json={
        /*The line below is essential for the future version.
        'type':$('[name=rule]').val(),
        */
        'type':'sudoku',
        'matrix':matrix,
        'group':options
    }

    //POST the JSON value.
    var xhr = new XMLHttpRequest();
    //xhr.open('POST', $("[name=ipaddress]").val());
    xhr.open('POST', "http://127.0.0.1:3333");
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    xhr.send( JSON.stringify(json) );
    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            console.log( JSON.parse(xhr.responseText) );
            const result=JSON.parse(xhr.responseText);
            /*The line below is essential for the future version.
            if($('[name=rule]').val()=="inequal")
                for(i=0; i<6; i++)
                    for(j=0; j<6; j++)
                        $(".square11x11 .parcel").eq(6*i+j).text(result["result"][i][j]);
            else
                for(i=0; i<Math.sqrt($(".square .square div").length); i++)
                    for(j=0; j<Math.sqrt($(".square .square div").length); j++){
                        var point=modifyIJ(i,j);
                        $(".square .square div").eq(matrix.length*i+j).text(result["result"][point["i"]][point["j"]]);
                    }
            */
           console.log(result, $(".square .square div").length);
            for(i=0; i<Math.sqrt($(".square .square div").length); i++)
                for(j=0; j<Math.sqrt($(".square .square div").length); j++){
                    var point=modifyIJ(i,j,size);
                    $(".square .square div").eq(matrix.length*i+j).text(result["result"][point["i"]][point["j"]]);
                }
        }
    }
}

function postMatrix2nd(size){
    //Organize the data.
    let matrix=[];
    for(i=0; i<Math.sqrt($(".square .square div").length); i++)
        matrix.push([]);
    for(i=0; i<Math.sqrt($(".square .square div").length); i++)
        for(j=0; j<Math.sqrt($(".square .square div").length); j++){
            INDEX=Math.sqrt(matrix.length)*Math.floor(i/Math.sqrt(matrix.length))+Math.floor(j/Math.sqrt(matrix.length));
            matrix[INDEX].push(Number($(".square .square div").eq(matrix.length*i+j).text()));
        }
    //Get the result
    let sudoku=new Sudoku();
    result=sudoku.start(matrix);
    //result=fillMatrixIntoNumbers(matrix, searchLackingNumbers(matrix), searchEmptyPlaces(matrix),3);
    for(i=0; i<Math.sqrt($(".square .square div").length); i++)
        for(j=0; j<Math.sqrt($(".square .square div").length); j++){
            var point=modifyIJ(i,j,size);
            $(".square .square div").eq(matrix.length*i+j).text(result[point["i"]][point["j"]]);
        }
}


/**
 * This changes a text in the "inequality button" into the opposite symbol.
 * @param {number} index The index number of the "inequality button" from 0 to 59.
 */
function changeComparison(index){
    var classname=".square11x11 button";
    var symbol=$(classname).eq(index).text();
    $(classname).eq(index).text(
        (symbol==`<` || symbol=='>')?
            (symbol=="<")? `>`: `<`:
            (symbol=="∧")? '∨': "∧"
    );
}

/**
 * This creates HTML design of "Inequality" on the window.
 * @returns {string}
 */
function createInequalityHTML(){
    var txt="", count_div=0, count_button=0;
    txt+='<div class="border square square11x11">';
    for(var i=0; i<11; i++)
        for(var j=0; j<11; j++)
            if(i%2==0){
                txt+=(j%2==0)? '<div class="parcel" contenteditable="true"></div>': '<button onclick="changeComparison('+count_button+');">&lt;</button>';
                (j%2==0)? count_div+=1: count_button+=1;
            }else{
                txt+=(j%2==0)? '<button onclick="changeComparison('+count_button+');">&or;</button>': '<div></div>';
                count_button+=(j%2==0)? 1: 0;
            }
    txt+='</div>';
    return txt;
}

/**
 * This creates a matrix by loading the numbers on the window.
 * @returns {int[6][6]}
 */
function createInequalityMatrix(){
    var mtrx=[];
    for(var i=0; i<6; i++){
        line=[];
        for(var j=0; j<6; j++)
            line.push (Number($(".square11x11 .parcel").eq(6*i+j).text()) );
        mtrx.push(line);
    }
    return mtrx;
}

/**
 * This creates a list of numberes representing an inequal.
 * @returns {int[11][n], n=5 (if even), 6 (if odd)}
 */
function createInequalityGroup(){
    var count=0;
    var gp=[];
    for(var i=0; i<11; i++){
        line=[];
        for(j=0; j<((i%2==0)? 5: 6); j++){
            line.push(
                ($(".square11x11 button").eq(count).text()=="<" || $(".square11x11 button").eq(count).text()=="∧")? 1: -1
            );
            count+=1;
        }
        gp.push(line);
    }
    return gp;
}

/**
 * This renews the field on the window then no numbers remain on the field.
 */
function renewField(size, rule){
    //var size=$('[name=size]').val();
    var text="";
    //if($('[name=rule]').val()=="inequal")
    if(rule=="inequal")
        text+=createInequalityHTML();
    else{
        text+="<div class='border square square"+size+"x"+size+"'>";
        for(i=0; i<size; i++){
            text+="<div class='border square square"+Math.sqrt(size)+"x"+Math.sqrt(size)+"'>";
            for(j=0; j<size; j++)
                text+='<div contenteditable="true" onclick="clickDiv('+(size*i+j)+');"></div>';
            text+="</div>";
        }
        text+="</div>";
    }
    $('.field').html(text);
}

/**
 * This reorders the numbers on the field to be adopted to the server.
 * @param {int} index The index number of the field on the window.
 * @param {int} size The size of the field.
 * @returns {int[2]} 
 */
function convertIndexInMatrix(index,size){
    const i=Math.floor(index/size), j=index-size*i, point=modifyIJ(i,j, size);
    return [point["i"],point["j"]];
}

/**
 * This calcuates a number to be adopted to the server.
 * @param {int} i The index of sizeXsize square.
 * @param {int} j The index in sizeXsize square.
 * @returns {{x:int, y:int}}
 */
function modifyIJ(i,j,size){
    //var size=$("[name=size]").val();
    return {
        "i":Math.sqrt(size)*Math.floor(i/Math.sqrt(size))+Math.floor(j/Math.sqrt(size)), 
        "j":Math.sqrt(size)*(i%Math.sqrt(size))+(j%Math.sqrt(size))
    };
}

/**
 * This removes a number from the group.
 * @param {int[2]} point The index of row and column.
 * @param {int} index The index of order.
 */
function removeFrom(point,index){
    $(".square .square div").eq(index).css("background-color","#dee8ff");
    grouplist.splice(indexIn(point,grouplist),1);
}

/**
 * This inserts a number into the group.
 * @param {int} index The index of order.
 */
function addInto(index){
    $(".square .square div").eq(index).css("background-color","pink");
    grouplist.push(convertIndexInMatrix(index, $("[name=size]").val()));
}

/**
 * By clicking on the square, this includes the number in the group if the number belongs no group or excludes from the group.
 * @param {int} index The index of order. 
 */
function clickDiv(index){
    /*The line below is essential for the future version.
    const point=convertIndexInMatrix(index, $("[name=size]").val());
    (include(point,grouplist))? removeFrom(point,index): addInto(index);
    */
}

/**
 * This returns a number which bigger than -1 if the nuber isn't be included to no group.
 * @param {int[2]} object The index of row and column.
 * @param {int[n][list[int[2]]]} list The list of groups including int[2]. 
 * @returns {x, -1<=x<=size}
 */
function indexIn(object,list){
    for(var i=0; i<list.length;i++)
        if(object.toString()==list[i].toString())
            return i;
    return -1;
}

/**
 * This checks if the object includes a group then returns true or false.
 * @param {int[2]} object The index of row and column. 
 * @param {int[n][list[int[2]]]} list The list of groups including int[2].
 * @returns {boolean}
 */
function include(object,list){
    return (indexIn(object,list)==-1)? false: true;
}

function grouping(size, rule){
    colors=["lightgreen","yellow","#ffbd83","#9eeeae","rgb(116, 242, 255)","#e0a8ff","#ffa0da", "#8eca89", "#ea9f8d"];
    groups.push(grouplist);
    nums=[];
    for(var i=0; i<grouplist.length; i++){
        var list=modifyIJ(grouplist[i][0], grouplist[i][1], size);
        $(".square .square div").eq(list["i"]*size+list["j"]).css("background-color",colors[(groups.length-1)%9]);
        nums.push(list["i"]*size+list["j"]);
    }
    grouplist=[];
    if(1<groups.length)
        optGroup(size, rule);
}

function optGroup(size, rule){
    //const size=$('[name=size]').val();
    var mtx=[];
    switch(rule.toString()){
        case 'twotone':
            for(var i=0; i<size; i++){
                line=[];
                for(var j=0; j<size; j++){
                    if(include([i,j],groups[0]))
                        line.push(1);
                    else if(include([i,j],groups[1]))
                        line.push(2);
                    else
                        line.push(0);
                }
                mtx.push(line);
            }
            options=mtx;
            break;
        case 'zigzag':
            for(var i=0; i<size; i++){
                line=[];
                for(var j=0; j<size; j++)
                    for(var g=0; g<groups.length; g++)
                        if(include([i,j],groups[g]))
                            line.push(g+1);
                mtx.push(line);
            }
            options=mtx;
            break;
        case "abs1":
            options=groups;
            break;
    }
}