$(document).ready(function(){
  $(function(){
    $('.block').filter(':not(".now")').hide(); //初始化 隐藏部分页数
    $('.winw').height($(window).height());
    $('.winh').width($(window).width());    //图片大小设置为设备大小
    for(var i=0;i<$('.block').length;i++){  //添加切换下圆圈图标
      if(i==0){
        $('.point').append('<div class="now"></div>');
      }else{
        $('.point').append('<div></div>');
      }
    }
    $('.point div').on('click',function(){  //点击小圆圈 跳转的相应页数
      go_to_index($(this).index());
    })
  });
  //------------------bg2--------------------------------//
  function mySetTimeoutPic1(index,text,time){
    var timer=setTimeout(function(){
      $('.b_4').hide();
      $('.b_4').removeClass('b_4_show');
      $('.b_4').addClass('b_4_hide');
      $('.pic2 p').text('');
      $('.pic2 p').removeClass('text2_show');
      $('.pic2 p').addClass('text2_hide');
      $('.b_1').css({display:'none'});
      $('.b_1:eq('+ index +')').css({display:'block'});
      $('.b_2').show();
      $('.b_2').removeClass('b_2_hide');
      $('.b_2').addClass('b_2_show');
      $('.pic1 p').text(text);
      $('.pic1 p').removeClass('text1_hide');
      $('.pic1 p').addClass('text1_show');
    },time);
    return timer;
  }
  function mySetTimeoutPic2(index,text,time){
   var timer=setTimeout(function(){
      $('.b_2').hide();
      $('.b_2').removeClass('b_2_show');
      $('.b_2').addClass('b_2_hide');
      $('.pic1 p').text('');
      $('.pic1 p').removeClass('text1_show');
      $('.pic1 p').addClass('text1_hide');
      $('.b_3').css({display:'none'});
      $('.b_3:eq('+ index +')').css({display:'block'});
      $('.b_4').show();
      $('.b_4').removeClass('b_4_hide');
      $('.b_4').addClass('b_4_show');
      $('.pic2 p').text(text);
      $('.pic2 p').removeClass('text2_hide');
      $('.pic2 p').addClass('text2_show');
    },time);
   return timer;
  }
  function displayElement(clsName,index,time){
    var timer=setTimeout(function(){
      $('.'+clsName+'').hide();
      $('.'+clsName+'').removeClass(''+clsName+'_show');
      $('.'+clsName+'').addClass(''+clsName+'_hide');
      $('.'+clsName+'').siblings('p').text('');
      $('.'+clsName+'').siblings('p').removeClass('text'+index+'_show');
      $('.'+clsName+'').siblings('p').addClass('text'+index+'_hide');
    },time)
    return timer;
  }
  function action(){
    timer1=mySetTimeoutPic2(0,'大熊,你怎么呢？',100);
    timer2=mySetTimeoutPic1(0,'多啦a梦！我的手机又丢了,大家的电话号码都没了,怎么办啊！',2000);
    timer3=mySetTimeoutPic2(0,'再给大家发短信,让大家把电话号码发给你啊~',4000);
    timer4=mySetTimeoutPic1(0,'已经好多次这样做了,既麻烦自己,又麻烦大家,还有其他办法吗？',6000);
    timer5=mySetTimeoutPic2(1,'这简单,登录www.haomyun.com,看大家号码都在上面呢！',8000);
    timer6=displayElement('b_4','2',10000);
    timer7=setTimeout(function(){
      $('.b_5').css({display:'block'});
    },11000);
    timer8=mySetTimeoutPic1(1,'哇,太棒了！我这就去新添我的电话号码让大家都看到！',12000);
    timer9=mySetTimeoutPic1(1,'看',14000);
    timer10=displayElement('b_2','1',16000);
    timer11=setTimeout(function(){
      $('.b_5').css({display:'none'});
      $('.b_6').css({display:'block'});
    },16000);
    timer12=setTimeout(function(){
      $('.b_6').css({display:'none'});
    },18000)
  }
  //------------------------------------------------------//

  //------------------bg3--------------------------------//
  $('.picShow').filter(':not(".current")').hide();
  setInterval(function(){
    var current_pic=$('.picShow.current').index();
    if(current_pic==3){
      go_to_pic(0,current_pic);
    }else{
      go_to_pic(current_pic+1,current_pic);
    }
  },3500);

  function go_to_pic(index,current_pic){
    $('.picShow.current').removeClass('current');
    $('.picShow:eq('+current_pic+') img').removeClass('pic_show');
    $('.picShow:eq('+current_pic+') p').removeClass('p_show');
    $('.picShow:eq('+current_pic+')').animate({opacity:0},750,function(){
      $(this).hide();
    })
    $('.picShow:eq('+index+')').addClass('current');
    $('.picShow:eq('+index+') img').addClass('pic_show');
    $('.picShow:eq('+index+') p').addClass('p_show');
    $('.picShow:eq('+index+')').animate({opacity:1},750,function(){
      $(this).show();
    })
  }
  //-----------------------------------------------------//

  //鼠标滚动
  $('body').on('mousewheel',function(event){
    var current_index=$('.block.now').index();
    var index=$('.block').length;
    if(event.originalEvent.deltaY>0){ //event.originalEvent.deltaY=100,向下滚动
      if(current_index==index-1){  //最后一页不能向下
        return false;
      }
      go_to_index(current_index+1);
    }else{                            //event.originalEvent.deltaY=-100,向上滚动
      if(current_index==0){
        return false;
      }
      go_to_index(current_index-1);
    }
  });

  function go_to_index(index){
    if(index==$('.block.now').index()){ //当前页面
      return false;
    }
    $('.block.now').removeClass('now'); //删除当前页面的now
    $('.block').animate({opacity:0},750,function(){  //
      $('.block').filter(':not(".now")').hide();
    });
    $('.block:eq('+ index +')').addClass('now');  //为要跳转的页面添加now
    $('.block:eq('+ index +')').stop();
    $('.block:eq('+ index +')').show();
    $('.block:eq('+ index +')').animate({opacity:1},750);
    $('.point div').filter('.now').removeClass('now');
    $('.point div:eq('+ index +')').addClass('now');

    if (index==1) {
      action();
    }else{
      clearTimeout(timer1);
      clearTimeout(timer2);
      clearTimeout(timer3);
      clearTimeout(timer4);
      clearTimeout(timer5);
      clearTimeout(timer6);
      clearTimeout(timer7);
      clearTimeout(timer8);
      clearTimeout(timer9);
      clearTimeout(timer10);
      clearTimeout(timer11);
      clearTimeout(timer12);
    }
    // if(index==2){
    //   clearInterval(picTimer);
    // }
  }
});