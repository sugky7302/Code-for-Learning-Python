function selectboxUpdateData(element, data){
    let select = document.getElementById("station_select") ;
    data[select.selectedIndex] = element.selectedIndex ;
}

function addEvent(element_name, event_name, event_func){
    let element = document.getElementById(element_name) ;
    element.addEventListener(event_name, event_func) ;
}

function setCheckBoxOn(name){
    let check = document.getElementById(name) ;
    check.checked = true ;
}

function setCheckBoxOff(name){
    let check = document.getElementById(name) ;
    check.checked = false ;
}

function setUltrasonicDefault(name, setting){
    // 全部清空
    for(let i = 0 ; i < 8 ; i++){
        setCheckBoxOff(name + i.toString()) ;
    }

    if(setting.length > 0){
        let ultrasonic_index = setting.split(",") ;
        
        for(let i = 0 ; i < ultrasonic_index.length ; i++){
            setCheckBoxOn(name + ultrasonic_index[i]) ;
        }
    }
}

function setActionOptions(name, index){
    let action = document.getElementById(name) ;

    // 清空動作列表
    action.options.length = 0 ;

    if(index.length > 0){
        let data = index.split(",") ;
    
        for(let i = 0 ; i < data.length ; i++){
            action.options[i] = new Option(data[i], data[i]) ;
        }   
    }
}

function setSelectBoxDefault(name, index){
    let box = document.getElementById(name) ;
    box.options[index].selected = true ;
}

function loadData(data){
    let select = document.getElementById("station_select") ;
    let selected_data = data[select.selectedIndex] ;

    // 設定類型
    setSelectBoxDefault("type_box", selected_data[1]) ;

    // 設定去程動作
    setActionOptions("go_action_select", selected_data[2]) ;

    // 設定去程雷射
    setSelectBoxDefault("go_laser_box", selected_data[3]) ;

    // 設定去程超聲波
    setUltrasonicDefault("go_ultrasonic_box", selected_data[4]) ;

    // 設定回程動作
    setActionOptions("back_action_select", selected_data[5]) ;

    // 設定回程雷射
    setSelectBoxDefault("back_laser_box", selected_data[6]) ;

    // 設定回程超聲波
    setUltrasonicDefault("back_ultrasonic_box", selected_data[7]) ;
}

function loadTest(data){
    let select = document.getElementById("station_select") ;

    // 讀取站點
    for(let i = 0 ; i < data.length; i++){
        select.options[i] = new Option(data[i][0], data[i][0]) ;
    }

    // NOTE: 監聽事件不能直接傳遞參數，必須透過匿名函數調用實際參數才行
    select.addEventListener('change', function(){
        loadData(data) ;
    }) ;

    // 對所有按鈕添加修改事件
    // 達到動態覆寫的功能
    addEvent("type_box", 'change', function(){
        selectboxUpdateData(document.getElementById("type_box"), data) ;
    })
}

function saveTest(){
    alert("Saving can't be used") ;
}

function addOption(name, description){
    let element = document.getElementById(name) ;
    if(element.options.length == 0){
        return false ; 
    }

    let input_text = prompt(description, "") ;

    if(input_text){
        element.options.add(new Option(input_text, input_text)) ;
    }
}

function removeSelectedOption(name){
    let element = document.getElementById(name) ;
    if(element.options.length > 0){
        element.options.remove(element.selectedIndex) ;
    }.
}

function addStation(){
    addOption("station_select", "請輸入要新增的站點:") ;
}

function removeSelectedStation(){
    removeSelectedOption("station_select") ;
}

function addAction(name){
    addOption(name,
              "請輸入要新增的動作:\n(0:前移 1:後移 2:左移 3:右移 200:輸送帶正轉 201:輸送帶反轉") ;
}

function addGoAction(){
    addAction("go_action_select") ;
}

function removeSelectedGoAction(){
    removeSelectedOption("go_action_select") ;
}

function addBackAction(){
    addAction("back_action_select") ;
}

function removeSelectedBackAction(){
    removeSelectedOption("gack_action_select") ;
}

function moveUp(name){
    let select = document.getElementById(name) ;
    let index = select.selectedIndex ;

    if(index > 0){
        temp = select.options[index] ;
        select.options[index] = select.options[index-1] ;
        select.options[index-1] = temp ;
    }
}

function moveUpSelectedGoAction(){
    moveUp("go_action_select") ;
}

function moveUpSelectedBackAction(){
    moveUp("back_action_select") ;
}

function moveDown(name){
    let select = document.getElementById(name) ;
    let index = select.selectedIndex ;

    if(index < (select.options.length-1)){
        temp = select.options[index] ;
        select.options[index] = select.options[index+1] ;
        select.options[index+1] = temp ;
    }
}

function moveDownSelectedGoAction(){
    moveDown("go_action_select") ;
}

function moveDownSelectedBackAction(){
    moveDown("back_action_select") ;
}
