//獲取預測水果資料
//$(function(){
//        $("#s3_predic_update").click(function(){
//            $.getJSON("show_food",function(data){       //getJSON傳回一個物件，不需再用JSON.parse轉物件
//                labels = data.labels
//                defaultData = data.data
//                defaultbackgroundColor = data.backgroundColor
//                setChart_food()
//            });
//        });
//    });

//$(function(){
//    //图片数组bai
//    var sArr =['static/img/child.jpeg','static/img/adult.jpeg','static/img/image1.jpg','static/img/image2.jpg','static/img/img2.jpeg'];
//    //定时更换背景
//    setInterval(function(){    
//        $("#show_age_img").css("backgroundImage","url("+sArr[fRandomBy(0,2)]+")");
//    },200); //单位毫秒
//    //设定随机数的范zhi围
//    function fRandomBy(under, over){ 
//       switch(arguments.length){ 
//         case 1: return parseInt(Math.random()*under+1); 
//         case 2: return parseInt(Math.random()*(over-under+1) + under); 
//         default: return 0; 
//       } 
//    } 
//})




// 目前水果數量 ================================================================================================

// 水果數量格線
$(function setChart_food(){
        var ctx = $('#predic_Chart');
        var myChart = new Chart(ctx, {
            type: 'horizontalBar',        // 圖表類型
            data: {
                labels: ["青江白菜","蘆筍","奇異果","西瓜","草菇","溼香菇","火龍果","甘藍","竹筍","香蕉",],
                datasets: [{
                    label: ["目前水果數量"],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                },
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true   //y軸刻度從0開始
                        }
                    }]
                },
                maintainAspectRatio: false,
            }
        });
});

//繪製水果數量圖表
function setChart_food(){
        var ctx = $('#predic_Chart');
        var myChart = new Chart(ctx, {
            type: 'horizontalBar',        // 圖表類型
            data: {
                labels: labels, // data.labels
                datasets: [{
                    label: ["目前水果數量"],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderWidth: 1,
                    data: defaultData, // data.data
                },
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true   //y軸刻度從0開始
                        }
                    }]
                },
                maintainAspectRatio: false,
            }
        });

};

//獲取預測水果資料
function get_fruit_data(){
    $.ajax({
        method: 'GET',
        url: 'show_food',
        async : false,
        success: function(data){
            labels = data.labels
            defaultData = data.data
            defaultbackgroundColor = data.backgroundColor;
            setChart_food();
        },
        error: function(error_data){
            console.log('error');
        }
    });
    return defaultData
};

//點擊水果數量資料
$(function(){
    $("#s3_predic_update").click(function() {
    get_fruit_data();
    });
});

// 選擇年齡層並調整食用量 ========================================================================================

// 預設格線
$(function sss(){
    var defaultData=0
    var now_chartData =
    {
        type: 'bar',
        data: {
            labels: labels = ["熱量(kcal)", "鈣(mg)", "鎂(mg)", "鐵(mg)", "鋅(mg)", "磷(mg)", "維生素A(ug RE)", "維生素E(mg)", "維生素B1(mg)", "維生素B2(mg)", "維生素B6(mg)", "維生素C(mg)"],
            datasets: [{
                        label: ["建議營養素百分比%"],
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderWidth: 1,
                        data: defaultData, // data.data
                        stack: 'Stack 0',
                    },
                    {
                        label: ["青江白菜"],
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderWidth: 1,
                        data: 0,  //defaultData1[0],
                        stack: 'Stack 1',
                    },
                    {
                        label: ["蘆筍"],
                        backgroundColor: 'rgba(128, 0, 0, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[1]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["奇異果"],
                        backgroundColor: 'rgba(255, 127, 80, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[2]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["西瓜"],
                        backgroundColor: 'rgba(218, 165, 32, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[3]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["草菇"],
                        backgroundColor: 'rgba(173, 255, 47, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[4]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["香菇"],
                        backgroundColor: 'rgba(64, 224, 208, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[5]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["火龍果"],
                        backgroundColor: 'rgba(30, 144, 255, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[6]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["甘藍"],
                        backgroundColor: 'rgba(0, 0, 205, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[7]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["竹筍"],
                        backgroundColor: 'rgba(102, 51, 153, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[8]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["香蕉"],
                        backgroundColor: 'rgba(255, 20, 147, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[9]
                        stack: 'Stack 1',
                    },
                    ]
        },
        options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true   //y軸刻度從0開始
                            },
                            stacked: true          //堆疊圖
                        }]
                    },
                    legend:{                       //圖例
                        display: true,
                        position: 'right',
                        labels:{
                            boxWidth: 15,
                            padding: 20,
                        },
                    },
                    maintainAspectRatio: false,    //防止圖表超出指定框
                }
        }
    var ctx = $("#now_nutrients_chart");
    var now_nutrients_chart = new Chart(ctx,now_chartData);
})

// 讀取第一個年齡層資料
function get_age(){
    $.ajax({
        type: 'POST',
        url: 'get_data1',
        async : false,
        data:{
            "name":"7-9",
        },
        dataType: 'json',
        success: function(data){
            get_age_age = data.data
            //console.log("get_age_age:",get_age_age);
            defaultData1=get_age_age
        },
        error: function(error_data){
            console.log('error');
        }
    });
    return defaultData1
}

// 讀取第二個年齡層資料
function get_age1(){
    $.ajax({
        method: 'POST',
        url: 'get_data1',
        async : false,
        data:{
            "name":"19-30",
        },
        dataType: 'json',
        success: function(data){
            get_age1_age = data.data
            //console.log("get_age1_age:",get_age1_age);
            defaultData1=get_age1_age
        },
        error: function(error_data){
            console.log('error');
        }
    });
    return defaultData1
}

console.log('get_age():',get_age());
console.log('get_age1():',get_age1());

// 每日營養素標準資料
function std_nutrients_data(){
    $.ajax({
        method: 'GET',
        url: 'get_data',
        async : false,
        success: function(data){
            console.log("data:",data);
            labels = data.labels
            defaultData = data.data
        },
    });
    return defaultData
};

// 控制圖表變化
function sss(){
    var defaultData=std_nutrients_data()
    var now_chartData =
    {
        type: 'bar',
        data: {
            labels: labels = ["熱量(kcal)", "鈣(mg)", "鎂(mg)", "鐵(mg)", "鋅(mg)", "磷(mg)", "維生素A(ug RE)", "維生素E(mg)", "維生素B1(mg)", "維生素B2(mg)", "維生素B6(mg)", "維生素C(mg)"],
            datasets: [{
                        label: ["建議營養素百分比%"],
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderWidth: 1,
                        data: defaultData, // data.data
                        stack: 'Stack 0',
                    },
                    {
                        label: ["青江白菜"],
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderWidth: 1,
                        data: 0,  //defaultData1[0],
                        stack: 'Stack 1',
                    },
                    {
                        label: ["蘆筍"],
                        backgroundColor: 'rgba(128, 0, 0, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[1]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["奇異果"],
                        backgroundColor: 'rgba(255, 127, 80, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[2]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["西瓜"],
                        backgroundColor: 'rgba(218, 165, 32, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[3]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["草菇"],
                        backgroundColor: 'rgba(173, 255, 47, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[4]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["香菇"],
                        backgroundColor: 'rgba(64, 224, 208, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[5]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["火龍果"],
                        backgroundColor: 'rgba(30, 144, 255, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[6]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["甘藍"],
                        backgroundColor: 'rgba(0, 0, 205, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[7]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["竹筍"],
                        backgroundColor: 'rgba(102, 51, 153, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[8]
                        stack: 'Stack 1',
                    },
                    {
                        label: ["香蕉"],
                        backgroundColor: 'rgba(255, 20, 147, 0.5)',
                        borderWidth: 1,
                        data: 0, // defaultData1[9]
                        stack: 'Stack 1',
                    },
                    ]
        },
        options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true   //y軸刻度從0開始
                            },
                            stacked: true          //堆疊圖
                        }]
                    },
                    legend:{                       //圖例
                        display: true,
                        position: 'right',
                        labels:{
                            boxWidth: 15,
                            padding: 20,
                        },
                    },
                    maintainAspectRatio: false,    //防止圖表超出指定框
                }
        }

    var ctx = $("#now_nutrients_chart");
    var now_nutrients_chart = new Chart(ctx,now_chartData);

    // 增加數量按鈕=================================================================
    var i1=0
    for(a=0;a<12;a++){
        eval('var btn_p1'+a+'=defaultData1[0]['+a+']')
    }
    $("#p1").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[1].data['+a+']=btn_p1'+a+'+(btn_p1'+a+')*'+i1);
        }
        i1=i1+1;

        console.log('e1:',now_chartData.data.datasets[1].data[0]);
        now_nutrients_chart.update();
    });

    var i2=0
    for(a=0;a<12;a++){
        eval('var btn_p2'+a+'=defaultData1[1]['+a+']')
    }
    $("#p2").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[2].data['+a+']=btn_p2'+a+'+(btn_p2'+a+')*'+i2);
        }
        i2=i2+1;

        console.log('e2:',now_chartData.data.datasets[2].data[0]);
        now_nutrients_chart.update();
    });

    var i3=0
    for(a=0;a<12;a++){
        eval('var btn_p3'+a+'=defaultData1[2]['+a+']')
    }
    $("#p3").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[3].data['+a+']=btn_p3'+a+'+(btn_p3'+a+')*'+i3);
        }
        i3=i3+1;

        console.log('e3:',now_chartData.data.datasets[3].data[0]);
        now_nutrients_chart.update();
    });

    var i4=0
    for(a=0;a<12;a++){
        eval('var btn_p4'+a+'=defaultData1[3]['+a+']')
    }
    $("#p4").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[4].data['+a+']=btn_p4'+a+'+(btn_p4'+a+')*'+i4);
        }
        i4=i4+1;

        console.log('e4:',now_chartData.data.datasets[4].data[0]);
        now_nutrients_chart.update();
    });

    var i5=0
    for(a=0;a<12;a++){
        eval('var btn_p5'+a+'=defaultData1[4]['+a+']')
    }
    $("#p5").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[5].data['+a+']=btn_p5'+a+'+(btn_p5'+a+')*'+i5);
        }
        i5=i5+1;

        console.log('e5:',now_chartData.data.datasets[5].data[0]);
        now_nutrients_chart.update();
    });

    var i6=0
    for(a=0;a<12;a++){
        eval('var btn_p6'+a+'=defaultData1[5]['+a+']')
    }
    $("#p6").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[6].data['+a+']=btn_p6'+a+'+(btn_p6'+a+')*'+i6);
        }
        i6=i6+1;

        console.log('e6:',now_chartData.data.datasets[6].data[0]);
        now_nutrients_chart.update();
    });

    var i7=0
    for(a=0;a<12;a++){
        eval('var btn_p7'+a+'=defaultData1[6]['+a+']')
    }
    $("#p7").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[7].data['+a+']=btn_p7'+a+'+(btn_p7'+a+')*'+i7);
        }
        i7=i7+1;

        console.log('e7:',now_chartData.data.datasets[7].data[0]);
        now_nutrients_chart.update();
    });

    var i8=0
    for(a=0;a<12;a++){
        eval('var btn_p8'+a+'=defaultData1[7]['+a+']')
    }
    $("#p8").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[8].data['+a+']=btn_p8'+a+'+(btn_p8'+a+')*'+i8);
        }
        i8=i8+1;

        console.log('e1:',now_chartData.data.datasets[8].data[0]);
        now_nutrients_chart.update();
    });

    var i9=0
    for(a=0;a<12;a++){
        eval('var btn_p9'+a+'=defaultData1[8]['+a+']')
    }
    $("#p9").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[9].data['+a+']=btn_p9'+a+'+(btn_p9'+a+')*'+i9);
        }
        i9=i9+1;

        console.log('e9:',now_chartData.data.datasets[9].data[0]);
        now_nutrients_chart.update();
    });

    var i10=0
    for(a=0;a<12;a++){
        eval('var btn_p10'+a+'=defaultData1[9]['+a+']')
    }
    $("#p10").click(function(){
        for(var a=0;a<12;a++){
            eval('now_chartData.data.datasets[10].data['+a+']=btn_p10'+a+'+(btn_p10'+a+')*'+i10);
        }
        i10=i10+1;

        console.log('e10:',now_chartData.data.datasets[10].data[0]);
        now_nutrients_chart.update();
    });


    // 減少數量 =======================================================================

    for(a=0;a<12;a++){
        eval('var btn_m1'+a+'=defaultData1[0]['+a+']')
    }
    $("#m1").click(function(){
        if(i1>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[1].data['+a+']=(btn_m1'+a+')*'+i1+'-(btn_m1'+a+')');
            }
        i1=i1-1;
        }
        console.log("i1:",i1)
        console.log('f1:',now_chartData.data.datasets[1].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m2'+a+'=defaultData1[1]['+a+']')
    }
    $("#m2").click(function(){
        if(i2>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[2].data['+a+']=(btn_m2'+a+')*'+i2+'-(btn_m2'+a+')');
            }
        i2=i2-1;
        }
        console.log('f2:',now_chartData.data.datasets[2].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m3'+a+'=defaultData1[2]['+a+']')
    }
    $("#m3").click(function(){
        if(i3>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[3].data['+a+']=(btn_m3'+a+')*'+i3+'-(btn_m3'+a+')');
            }
        i3=i3-1;
        }
        console.log('f3:',now_chartData.data.datasets[3].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m4'+a+'=defaultData1[3]['+a+']')
    }
    $("#m4").click(function(){
        if(i4>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[4].data['+a+']=(btn_m4'+a+')*'+i4+'-(btn_m4'+a+')');
            }
        i4=i4-1;
        }
        console.log('f4:',now_chartData.data.datasets[4].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m5'+a+'=defaultData1[4]['+a+']')
    }
    $("#m5").click(function(){
        if(i5>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[5].data['+a+']=(btn_m5'+a+')*'+i5+'-(btn_m5'+a+')');
            }
        i5=i5-1;
        }
        console.log('f5:',now_chartData.data.datasets[5].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m6'+a+'=defaultData1[5]['+a+']')
    }
    $("#m6").click(function(){
        if(i6>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[6].data['+a+']=(btn_m6'+a+')*'+i6+'-(btn_m6'+a+')');
            }
        i6=i6-1;
        }
        console.log('f6:',now_chartData.data.datasets[6].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m7'+a+'=defaultData1[6]['+a+']')
    }
    $("#m7").click(function(){
        if(i7>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[7].data['+a+']=(btn_m7'+a+')*'+i7+'-(btn_m7'+a+')');
            }
        i7=i7-1;
        }
        console.log('f7:',now_chartData.data.datasets[7].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m8'+a+'=defaultData1[7]['+a+']')
    }
    $("#m8").click(function(){
        if(i8>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[8].data['+a+']=(btn_m8'+a+')*'+i8+'-(btn_m8'+a+')');
            }
        i8=i8-1;
        }
        console.log('f8:',now_chartData.data.datasets[8].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m9'+a+'=defaultData1[8]['+a+']')
    }
    $("#m9").click(function(){
        if(i9>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[9].data['+a+']=(btn_m9'+a+')*'+i9+'-(btn_m9'+a+')');
            }
        i9=i9-1;
        }
        console.log('f9:',now_chartData.data.datasets[9].data[6]);
        now_nutrients_chart.update();
    });

    for(a=0;a<12;a++){
        eval('var btn_m10'+a+'=defaultData1[9]['+a+']')
    }
    $("#m10").click(function(){
        if(i10>0){
            for(var a=0;a<12;a++){
                eval('now_chartData.data.datasets[10].data['+a+']=(btn_m10'+a+')*'+i10+'-(btn_m10'+a+')');
            }
        i10=i10-1;
        }
        console.log('f10:',now_chartData.data.datasets[10].data[6]);
        now_nutrients_chart.update();
    });
}

// 選擇第一個年齡層
$(function(){
    $('.btn1').on('click', function(){
        $("#show_age_img").html("");
        $("#show_age_img").attr("src","static/img/child.jpeg");
        $('#aa').slideDown('fast');

        get_age()
        console.log("get_age:",get_age()[1])
        sss()
    });
    $('.btn').not('.btn1').on('click', function(){
    $('#aa').slideUp('fast');
    });
});

// 選擇第二個年齡層
$(function(){
    $('.btn2').on('click', function(){
        $("#show_age_img").html("");
        $("#show_age_img").attr("src","static/img/adult.jpeg");
        $('#bb').slideDown('fast');
        get_age1()
        console.log("get_age1:",get_age1()[1])
        sss()
    });
    $('.btn').not('.btn2').on('click', function(){
    $('#bb').slideUp('fast');
    });
});



// 按鈕數量變化顯示 ==============================================================================================

function adder1(){
	var count=$("#num1").text();
	count=parseInt(count)+1;
	$("#num1").text(count);
}

function minuser1(){
	var count=$("#num1").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num1").text(count);
}

function adder2(){
	var count=$("#num2").text();
	count=parseInt(count)+1;
	$("#num2").text(count);
}
function minuser2(){
	var count=$("#num2").text();
    if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num2").text(count);
}

function adder3(){
	var count=$("#num3").text();
	count=parseInt(count)+1;
	$("#num3").text(count);
}
function minuser3(){
	var count=$("#num3").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num3").text(count);
}

function adder4(){
	var count=$("#num4").text();
	count=parseInt(count)+1;
	$("#num4").text(count);
}
function minuser4(){
	var count=$("#num4").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num4").text(count);
}

function adder5(){
	var count=$("#num5").text();
	count=parseInt(count)+1;
	$("#num5").text(count);
}
function minuser5(){
	var count=$("#num5").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num5").text(count);
}

function adder6(){
	var count=$("#num6").text();
	count=parseInt(count)+1;
	$("#num6").text(count);
}
function minuser6(){
	var count=$("#num6").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num6").text(count);
}

function adder7(){
	var count=$("#num7").text();
	count=parseInt(count)+1;
	$("#num7").text(count);
}
function minuser7(){
	var count=$("#num7").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num7").text(count);
}

function adder8(){
	var count=$("#num8").text();
	count=parseInt(count)+1;
	$("#num8").text(count);
}
function minuser8(){
	var count=$("#num8").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num8").text(count);
}

function adder9(){
	var count=$("#num9").text();
	count=parseInt(count)+1;
	$("#num9").text(count);
}
function minuser9(){
	var count=$("#num9").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num9").text(count);
}

function adder10(){
	var count=$("#num10").text();
	count=parseInt(count)+1;
	$("#num10").text(count);
}
function minuser10(){
	var count=$("#num10").text();
	if(count<=0){
		count=0;
	}else{
		count=parseInt(count)-1;
	}
	$("#num10").text(count);
}

// ================================================================================================

var defaultData=std_nutrients_data()

//繪製比較圖表格線
$(function setChart(){
 //   $("#s3_chart_update").click(function(){
        var ctx = $('#myChart');
        var defaultData=std_nutrients_data()
        var myChart = new Chart(ctx, {
            type: 'bar',        // 圖表類型
            data: {
                labels: labels, // data.labels
                datasets: [{
                    label: ["建議營養素百分比%"],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 0',
                },
                {
                    label: ["青江白菜"],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["蘆筍"],
                    backgroundColor: 'rgba(128, 0, 0, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["奇異果"],
                    backgroundColor: 'rgba(255, 127, 80, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["西瓜"],
                    backgroundColor: 'rgba(218, 165, 32, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["草菇"],
                    backgroundColor: 'rgba(173, 255, 47, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["香菇"],
                    backgroundColor: 'rgba(64, 224, 208, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["火龍果"],
                    backgroundColor: 'rgba(30, 144, 255, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["甘藍"],
                    backgroundColor: 'rgba(0, 0, 205, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["竹筍"],
                    backgroundColor: 'rgba(102, 51, 153, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["香蕉"],
                    backgroundColor: 'rgba(255, 20, 147, 0.5)',
                    borderWidth: 1,
                    data: 0, // data.data
                    stack: 'Stack 1',
                },
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true   //y軸刻度從0開始
                        },
                        stacked: true          //堆疊圖
                    }]
                },
                legend:{                       //圖例
                    display: true,
                    position: 'right',
                    labels:{
                        boxWidth: 15,
                        padding: 20,
                    },
                },
                maintainAspectRatio: false,    //防止圖表超出指定框
            }
        });
  //  });
});

//繪製比較圖表
function setChart(){
 //   $("#s3_chart_update").click(function(){
        var ctx = $('#myChart');
        var defaultData=std_nutrients_data()
        var myChart = new Chart(ctx, {
            type: 'bar',        // 圖表類型
            data: {
                labels: labels, // data.labels
                datasets: [{
                    label: ["建議營養素百分比%"],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderWidth: 1,
                    data: defaultData, // data.data
                    stack: 'Stack 0',
                },
                {
                    label: ["青江白菜"],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[0], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["蘆筍"],
                    backgroundColor: 'rgba(128, 0, 0, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[1], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["奇異果"],
                    backgroundColor: 'rgba(255, 127, 80, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[2], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["西瓜"],
                    backgroundColor: 'rgba(218, 165, 32, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[3], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["草菇"],
                    backgroundColor: 'rgba(173, 255, 47, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[4], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["香菇"],
                    backgroundColor: 'rgba(64, 224, 208, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[5], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["火龍果"],
                    backgroundColor: 'rgba(30, 144, 255, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[6], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["甘藍"],
                    backgroundColor: 'rgba(0, 0, 205, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[7], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["竹筍"],
                    backgroundColor: 'rgba(102, 51, 153, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[8], // data.data
                    stack: 'Stack 1',
                },
                {
                    label: ["香蕉"],
                    backgroundColor: 'rgba(255, 20, 147, 0.5)',
                    borderWidth: 1,
                    data: defaultData1[9], // data.data
                    stack: 'Stack 1',
                },
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true   //y軸刻度從0開始
                        },
                        stacked: true          //堆疊圖
                    }]
                },
                legend:{                       //圖例
                    display: true,
                    position: 'right',
                    labels:{
                        boxWidth: 15,
                        padding: 20,
                    },
                },
                maintainAspectRatio: false,    //防止圖表超出指定框
            }
        });
  //  });
};

$(function(){
    $("#s3_chart_update").click(function(){
    setChart()
    })
})




////取得標準營養素資料
//$(function(){
//    $.ajax({
//        method: 'GET',
//        url: 'get_data',
//        success: function(data){
//            labels = data.labels
//            defaultData = data.data
//            console.log("get_defaultData",defaultData)
//            defaultbackgroundColor = data.backgroundColor
//        },
//        error: function(error_data){
//            console.log('error');
//        }
//    });
//});


////取得目前營養素資料
//$(function(){
//    $.ajax({
//        method: 'GET',
//        url: 'get_data1',
//        success: function(data){
//            console.log("目前營養素資料:",data)
//            labels = data.labels
//            defaultData1 = data.data
//            console.log("get_defaultData1",defaultData1)
//            defaultbackgroundColor1 = data.backgroundColor
//            setChart()
//        },
//        error: function(error_data){
//            console.log('error');
//        }
//    });
//});


// ================================================================================================



//解析json
//$(function(){
//        $.getJSON("show_food",function(ret){
//            $.each(ret, function(i, item) {
//            console.log(item.name);
//            $("#s3_box1").append(item.name+"<br>");
//		});
//	});
//});

//$(function(){
//        $.getJSON("show_food_compare",function(ret){
//            $.each(ret, function(i, item) {
//            console.log(item.name);
//            $("#s3_box2").append(item.name+"<br>");
//		});
//	});
//});

//$(function(){
//        $.getJSON("show_food_compare",function(ret){
//            $.each(ret, function(i, item) {
//            console.log(item.name);
//            $("#s3_box2").append(item.name+"<br>");
//
//		});
//	});
//	    $.getJSON("show_food",function(ret){
//            $.each(ret, function(i, item) {
//            console.log(item.name);
//            $("#s3_box2").append(item.name+"<br>");
//		});
//	});
//});
