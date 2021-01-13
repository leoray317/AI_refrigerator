////擷取影像用
//$(function(){
//    $("#s2_show_img_id").click(function(){
//        $.getJSON("web_video_url",function(ret){       //getJSON傳回一個物件，不需再用JSON.parse轉物件
//            var today=new Date().format("Y-m-d H:i:s");
//            console.log(ret.url);
//            $("#json_img_box").html("");
//            $("#json_img_box").attr("src", ret.url);
//            $("#img_log").append("擷取影像" + today+'<br>');
//		});
//    });
//});


//測試圖片 from api
$(function(){
    $("#s2_show_img_id").click(function(){
        $.getJSON("photo",function(ret){
            var today=new Date().format("Y-m-d H:i:s");
            console.log("json圖片:",typeof(ret));
            console.log("json:",ret);
            console.log("json-1:",ret.url);
            if (typeof(ret.url)=='undefined'){
                $("#predic_result").append("沒有圖片" );
            }
            else{
                $("#json_img_box").html("");
                $("#json_img_box").attr("src", ret.url);
                $("#predic_result").html("");  // 覆蓋當前物件
                $("#predic_result").append("結果為:" + ret.name);  //追加當前物件
                $("#img_log").append("擷取圖片" + today+'<br>');
            }
		});
    });
});

//測試圖片 from api
$(function(){
    $("#s2_show_predic_id").click(function(){
        $.getJSON("photo_post",function(ret){
            var today=new Date().format("Y-m-d H:i:s");
            if (typeof(ret.url)=='undefined'){
                $("#predic_result").append("沒有圖片" );
            }
            else{
                $("#json_img_predic_box").html("");
                $("#json_img_predic_box").attr("src", ret.url);
                $("#predic_result").html("");
                $("#predic_result").append("結果為:" + ret.result);
                $("#img_log").append("預測圖片" + today+'<br>');
            }
		});
    });
});




////預測結果 from other predict api
//$(function(){
//    $("#s2_show_predic_id").click(function(){
//        $.getJSON("web_img_url",function(rec){
//            var today=new Date().format("Y-m-d H:i:s");
//            $.each(rec.results, function(i, item) {
//                console.log(item.name);
//                console.log(item.nickname);
//                $("#predic_result").append("名稱:" + item.name +'<br>'+ "暱稱:" + item.nickname +'<br>' +"備註:" + item.nationality);
//                $("#json_img_box").attr("src",item.img_url);
//                $("#json_img_predic_box").attr("src",item.url);
//            });
//		});
//    });
//});

////預測結果 from my flask api
//$(function(){
//    $("#s2_show_predic_id").click(function(){
//        $.getJSON("web_img_url",function(rec){
//            var today=new Date().format("Y-m-d H:i:s");
//            $.each(rec, function(i, item) {
//            console.log(item);
//            console.log(item.name);
//            console.log(item.nickname);
//            $("#predic_result").append("名稱:" + item.name +'<br>'+ "暱稱:" + item.nickname +'<br>' +"備註:" + item.nationality);
//            });
//		});
//    });
//});

