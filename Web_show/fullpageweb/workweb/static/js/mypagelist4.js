function get_price(fruit_type){
    $.ajax({
        type: 'POST',
        url: 'price_pre',
        async : false,
        data:{
            "name":fruit_type,
        },
        dataType: 'json',
        success: function(data){
            $("#sec4_box4").html("");
            $("#sec4_box4").attr("src", data.pre_img_url_y);
            $("#sec4_box5").attr("src", data.pre_img_url_t);
            $("#sec4_pre1").html("");  
            $("#sec4_pre1").append("預測值為:" + data.price1);
            $("#sec4_pre2").html("");  
            $("#sec4_pre2").append("昨天價格為:" + data.price2);
            $("#sec4_pre3").html("");  
            $("#sec4_pre3").append("今天價格為:" + data.price3);
        },
        error: function(error_data){
            console.log('error');
        }
    });
    return 
}

$(function s4_btn1_id(){
    $('#s4_btn1_id').click(function() {
        fruit_type="a"
        get_price(fruit_type)
    });
});

$(function s4_btn2_id(){
    $('#s4_btn2_id').click(function() {
        fruit_type="b"
        get_price(fruit_type)
    });
});

$(function s4_btn3_id(){
    $('#s4_btn3_id').click(function() {
        fruit_type="c"
        get_price(fruit_type)
    });
});

$(function s4_btn4_id(){
    $('#s4_btn4_id').click(function() {
        fruit_type="d"
        get_price(fruit_type)
    });
});

$(function s4_btn5_id(){
    $('#s4_btn5_id').click(function() {
        fruit_type="e"
        get_price(fruit_type)
    });
});

$(function s4_btn6_id(){
    $('#s4_btn6_id').click(function() {
        fruit_type="f"
        get_price(fruit_type)
    });
});

$(function s4_btn7_id(){
    $('#s4_btn7_id').click(function() {
        fruit_type="g"
        get_price(fruit_type)
    });
});

$(function s4_btn8_id(){
    $('#s4_btn8_id').click(function() {
        fruit_type="h"
        get_price(fruit_type)
    });
});

$(function s4_btn9_id(){
    $('#s4_btn9_id').click(function() {
        fruit_type="i"
        get_price(fruit_type)
    });
});

$(function s4_btn10_id(){
    $('#s4_btn10_id').click(function() {
        fruit_type="j"
        get_price(fruit_type)
    });
});