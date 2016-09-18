$(document).ready(function(){
	function draw(i){
		var canvas=document.getElementById("myCanvas"+i);;
		if(canvas.getContext){
			var ctx=canvas.getContext('2d')
			return ctx;
		}
	}
	function draw_pic(){  //(i,x1,y1,x2,y2,x3,y3,...,strokeStyle_color,fillStyle_color)
		var len=arguments.length;
		var ctx=draw(arguments[0]);
		ctx.beginPath();
		ctx.strokeStyle=arguments[len-2];
		ctx.fillStyle=arguments[len-1];
		ctx.moveTo(arguments[1],arguments[2]);
		for(var i=3,len_xy=len-3;i<len_xy;i+=2){
			ctx.lineTo(arguments[i],arguments[i+1])
		}
		ctx.closePath();
		ctx.stroke();
		ctx.fill();
	}
	function draw_text(){  //(i,x1,y1,text1,x2,y2,text2,x3,y3,text3...,)
		var ctx=draw(arguments[0]);
		ctx.strokeStyle='white';
		ctx.fillStyle='white';
		ctx.font="30px Arial";
		for(var i=1,len=arguments.length;i<len;i+=3){
			ctx.fillText(arguments[i+2],arguments[i],arguments[i+1]);
		}
	}
	draw_pic(1,20,50,45,20,370,20,370,80,45,80,'#00a0e9','#00a0e9');
	draw_pic(1,370,80,350,100,350,80,'#00a0e9','#0075a9');
	draw_text(1,70,60,'基本信息');
	draw_pic(2,20,50,45,20,370,20,370,80,45,80,'#00a0e9','#00a0e9');
	draw_pic(2,370,80,350,100,350,80,'#00a0e9','#0075a9');
	draw_text(2,70,60,'联系方式');
	draw_pic(3,20,50,45,20,370,20,370,80,45,80,'#00a0e9','#00a0e9');
	draw_pic(3,370,80,350,100,350,80,'#00a0e9','#0075a9');
	draw_text(3,70,60,'掌握技能');
	draw_pic(4,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(4,20,0,100,0,100,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(5,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(5,20,0,90,0,90,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(6,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(6,20,0,90,0,90,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(7,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(7,20,0,100,0,100,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(8,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(8,20,0,110,0,110,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(9,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(9,20,0,130,0,130,10,20,10,'#00a0e9','#00a0e9');
	draw_pic(10,20,0,160,0,160,10,20,10,'#b5b5b6','#b5b5b6');
	draw_pic(10,20,0,96,0,96,10,20,10,'#00a0e9','#00a0e9');

	$('button').on('click',function(){
	    $('textarea').val('');
	})

	Date.prototype.Format = function (fmt) {  
	    var o = {
	        "M+": this.getMonth() + 1, //月份 
	        "d+": this.getDate(), //日 
	        "h+": this.getHours(), //小时 
	        "m+": this.getMinutes(), //分 
	        "s+": this.getSeconds(), //秒 
	        "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
	        "S": this.getMilliseconds() //毫秒 
	    };
	    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
	    for (var k in o)
	    if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
	    return fmt;
	}

	$.ajaxSetup({
	    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
	});
	var csrfValue=$('input[name="csrfmiddlewaretoken"]').val();
	$('#formSuggest').submit(function(e){
	    e.preventDefault();
	    var data = $(this).serialize()+'&submitName=put';
	    var suggest=$('textarea').val();
	    $.ajax({
	        url:'/jianli/',
	        type:'POST',
	        traditional:true,
	        cache:false,
	        // data:{name:name,phones:phoneArr},
	        data:data,
	        success:function(arg){
	            if (arg=='感谢您的建议！') {
	                var time=new Date().Format("yyyy-MM-dd hh:mm:ss");
	                $('textarea').val(' ');
	                $('.suggest').after('<form method="POST" name="formCancel" class="hiddenSuggest"><input type="hidden" name="csrfmiddlewaretoken" value="'+csrfValue+'" /><div class="showSuggest floatfix"><div class="suggestContent">'+suggest+'</div><div class="timeRight"><div class="time left">'+time+'</div><div class="remove left"><input type="submit" name="cancel" value="删除"></input></div> </div></div></form>');
	                alert(arg); 
	            }else{
	                alert(arg);
	            }
	        }
	    });
	});

	$('form[name="formCancel"]').submit(function(e){
	    e.preventDefault();
	    var suggest=$(this).children('.showSuggest').children('.suggestContent').text()
	    var data=$(this).serialize()+'&suggest='+suggest+'&submitName=cancel';
	    var form=$(this);
	    $.ajax({
	        url:'/jianli/',
	        type:'POST',
	        traditional:true,
	        cache:false,
	        data:data,
	        success:function(arg){
	            $(form).remove();
	            alert(arg);
	        }
	    });
	});
})