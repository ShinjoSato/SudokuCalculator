function setStatus(progress){
    Status+=progress;
    if(Status==0){
        //枠組み制作状態
        hideDuplicateSquareField();
        $("#bt-regress").css("display","none");
        $("#input-number").css("display","none");
        $("#bt-select").css("display","initial");
        $("#fr-size").css("display","initial");

        $("#bt-progress").text("枠決定");
        if(progress<0){
            $('.input-area').html("");
            $('.input-area').removeAttr('style');
            console.log("deleteしたい！:",Status);
        }
    }else if(Status==1){
        //問題入力状態
        $("#bt-regress").css("display","initial");
        $("#bt-progress").css("display","initial");
        $("#input-number").css("display","initial");
        $("#bt-select").css("display","none");
        $("#fr-size").css("display","none");

        $("#bt-regress").text("枠選択");
        $("#bt-progress").text("計算");
        if(0<progress){
            hideDuplicateSquareField();
            layoutDuplicateSquaresField();
        }
    }else if(Status==2){
        //結果出力
        $("#bt-progress").css("display","none");
        pasteDuplicateMatrixesOnSquares();
        setStatus(-1);
    }
    //console.log("Status:",Status);
}

//It only executes at first.
function moldSelectArea(){
    let class_name='.mold-square';
    let doc='';
    let size=$("#fr-size option:selected").val();
    $(class_name).html("");
    $(".mold-square").css("grid-template-columns","repeat("+size+", 18px)");
    $(".mold-square").css("grid-template-rows","repeat("+size+", 18px)");
    for(let i=0; i<size; i++)
        for(let j=0; j<size; j++)
            doc+='<div class="index-'+i+'-'+j+'" style="border: 1px solid #cecece;"  onclick=insertIntoGroupLists('+i+','+j+')></div>';
    $(class_name).html(doc);
    drawSquareBorder();
}

$(function(){
    $("#fr-size").change(function(){
        console.log($("#fr-size option:selected").text(),"!!");
        moldSelectArea();
    });
});

function getAllSides(){
    let top=1000, right=0, bottom=0, left=999;
    for(let list of GroupLists)
        for(let l of list){
            if(l[0]<top)
                top=l[0];
            if(bottom<l[0])
                bottom=l[0];
            if(l[1]<left)
                left=l[1];
            if(right<l[1])
                right=l[1];
        }
    return {'top':top, 'bottom':bottom, 'left':left, 'right':right};
}

function revertToPreviousStatus(){
    if(0<GroupLists.length){
        for(let list of GroupLists[GroupLists.length-1])
            $(".index-"+list[0]+"-"+list[1]).css('border', '1px solid #cecece');
        GroupLists.pop();
    }
    drawSquareBorder();
}

function drawSquareBorder(){
    for(let list of GroupLists)
        for(let i=0; i<list.length; i++){
            if(i<Length)
                $(".index-"+list[i][0]+"-"+list[i][1]).css('border-top', '2px solid green');
            if(list.length-(Length+1)<i)
                $(".index-"+list[i][0]+"-"+list[i][1]).css('border-bottom', '2px solid green');
            if(i%Length==0)
                $(".index-"+list[i][0]+"-"+list[i][1]).css('border-left', '2px solid green');
            if(i%Length==Length-1)
                $(".index-"+list[i][0]+"-"+list[i][1]).css('border-right', '2px solid green');
        }
}

function insertIntoGroupLists(x,y){
    let list=[];
    for(let i=0; i<Length; i++)
        for(let j=0; j<Length; j++)
            list.push([(x+i),(y+j)]);
    GroupLists.push(list);
    drawSquareBorder();
}

function hideDuplicateSquareField(){
    $('.mold-square').css('display', ($('.mold-square').css('display')=='none')? 'grid': 'none');
}

function layoutDuplicateSquaresField(){
    const sides=getAllSides();
    $('.input-area').css('grid-template-rows', 'repeat('+String(sides['bottom']-sides['top']+1)+', 40px)');
    $('.input-area').css('grid-template-columns', 'repeat('+String(sides['right']-sides['left']+1)+', 40px)');
    let docm='';
    for(let i=0; i<(sides['bottom']-sides['top'])+1; i++){
        for(let j=0; j<(sides['right']-sides['left'])+1; j++){
            let cname=''
            let style="";
            let beEditable=''
            for(let group=0; group<GroupLists.length; group++)
                for(let g=0; g<GroupLists[group].length; g++){
                    let mod_x=(GroupLists[group][g][0]-sides['top']);
                    let mod_y=(GroupLists[group][g][1]-sides['left']);
                    if(mod_x==i && mod_y==j){
                        let x=GroupLists[group][g][0]-GroupLists[group][0][0];
                        let y=GroupLists[group][g][1]-GroupLists[group][0][1];
                        let cls=group+'-'+x+'-'+y;
                        cname+=cls+' ';
                        style+="background-color: #5e9e5e; text-align: center; font-size: 26px; font-family: 'Leckerli One', cursive; color:#e0e0e0;";
                        beEditable='contenteditable="true" onclick="clickToInputNumber(`'+cls+'`);"'
                    }
                }
            if(cname.length==0)
                cname='none';
            docm+="<div class='"+cname+"' style='"+style+"' "+beEditable+"></div>";
        }
        $('.input-area').html(docm);
        colorDuplicateSquares();
    }
}

function clickToInputNumber(class_name){
    let num=Number($("#input-number").val());
    if(num<0)
        $('.'+class_name).text("");
    else if(0<num)
        $('.'+class_name).text(num);
}

function colorDuplicateSquares(){
    const tmp_scale=9;
    for(let g=0; g<GroupLists.length; g++)
        for(let i=0; i<tmp_scale; i++)
            for(let j=0; j<tmp_scale; j++)
                $('.'+g+'-'+i+'-'+j).css("border","1px dashed #e0e0e0");
    const sqrt_scale=Math.sqrt(tmp_scale);
    for(let g=0; g<GroupLists.length; g++)
        for(let i=0; i<tmp_scale; i++)
            for(let j=0; j<tmp_scale; j++){
                if(i%sqrt_scale==0)
                    $('.'+g+'-'+i+'-'+j).css("border-top","1px solid #e0e0e0");
                if(i%sqrt_scale==sqrt_scale-1)
                    $('.'+g+'-'+i+'-'+j).css("border-bottom","1px solid #e0e0e0");
                if(j%sqrt_scale==0)
                    $('.'+g+'-'+i+'-'+j).css("border-left","1px solid #e0e0e0");
                if(j%sqrt_scale==sqrt_scale-1)
                    $('.'+g+'-'+i+'-'+j).css("border-right","1px solid #e0e0e0");

            }
    for(let g=0; g<GroupLists.length; g++)
        for(let i=0; i<tmp_scale; i++)
            for(let j=0; j<tmp_scale; j++){
                if(i==0)
                    $('.'+g+'-'+i+'-'+j).css("border-top","3px solid #bbbbbb");
                if(i==tmp_scale-1)
                    $('.'+g+'-'+i+'-'+j).css("border-bottom","3px solid #bbbbbb");
                if(j==0)
                    $('.'+g+'-'+i+'-'+j).css("border-left","3px solid #bbbbbb");
                if(j==tmp_scale-1)
                    $('.'+g+'-'+i+'-'+j).css("border-right","3px solid #bbbbbb");
            }
}

function getDuplicateGroups(){
    let groups=[];
    for(let g=0; g<GroupLists.length; g++){
        let oneG=[];
        for(let i=0; i<9; i++){
            let rows=[];
            for(let j=0; j<9; j++){
                let percel=[];
                class_name=g+'-'+i+'-'+j;
                let cnames=$('.'+class_name).attr('class').split(' ');
                if(2<cnames.length){
                    for(let l=0; l<cnames.length-1; l++)
                        if(class_name!=cnames[l]){
                            let list=cnames[l].split('-');
                            percel.push([Number(list[0]), Number(list[1]), Number(list[2])]);
                        }
                }
                rows.push(percel);
            }
            oneG.push(rows);
        }
        groups.push(oneG);
    }
    return groups;
}

function calcDuplicateMatrixes(){
    let s= new Duplication();
    return s.start(
        getDuplicateMatrixes(),
        getDuplicateGroups()
    );
}

function getDuplicateMatrixes(){
    let matrixes=[];
    let tmp_scale=9;
    for(let m=0; m<GroupLists.length; m++){
        let matrix=[];
        for(let i=0; i<tmp_scale; i++){
            let rows=[];
            for(let j=0; j<tmp_scale; j++)
                rows.push(Number($('.'+m+'-'+i+'-'+j).text()));
            matrix.push(rows);
        }
        matrixes.push(matrix);
    }
    return matrixes;
}

function pasteDuplicateMatrixesOnSquares(){
    try{
        const result=calcDuplicateMatrixes();
        for(let g=0; g<GroupLists.length; g++)
            for(let i=0; i<9; i++)
                for(let j=0; j<9; j++)
                    $('.'+g+'-'+i+'-'+j).text(result[g][i][j]);
    }catch(e){
        console.log(e);
        alert("計算に失敗しました。\nもう一度入力内容をご確認ください。");
    }
}