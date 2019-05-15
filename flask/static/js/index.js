function loadData(data){
    let select = document.getElementById("station_select") ;

    // 設定類型
    let go_or_back = data[select.selectedIndex][1] ;
    let type_box = document.getElementById("type_box") ;
    type_box.options[go_or_back].selected = true ;
}

function loadTest(data){
    let select = document.getElementById("station_select") ;

    // 讀取站點
    for(let i = 0 ; i < data.length; i++){
        select.options[i] = new Option(data[i][0], data[i][0]) ;
    }
}

function saveTest(){
    alert("Saving can't be used") ;
}