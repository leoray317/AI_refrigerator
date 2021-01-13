$(document).ready(function(){
	$("button").click(function(){
		$("#div1").load("/static/img/text.txt");
	});
});


$(function(){
    $("#sum").click(function(){
        var a = $("#a").val();
        var b = $("#b").val();
        $.get("add",{'a':a,'b':b}, function(ret){
        $('#result').html(ret)
        })
    });
});

$(function(){
    $("#textid").click(function(){
        $.get("text",function(ret){
        $('#resul').html(ret)
        })
    });
});