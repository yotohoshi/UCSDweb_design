$(document).ready(function() {
  $('#new-friends-content1').load('m1.html');
  $('#new-friends-content2').load('m2.html');
  $('#new-friends-content3').load('m3.html');

  $('#new-friends-content4').load('m4.html');
  $('#new-friends-content5').load('m5.html');
  $('#new-friends-content6').load('m6.html');
  // $('#new-friends-content7').load('network_content_Vfinal.html');
  // $('#new-friends-content').load('network_content_Vfinal.html');
  $('#sidebarText').load("sidebar.html");
  $('#Topright').load("index_top_right.html");
  $('#keywordsearch').load("simple_keyword_search.html");
  $('#reff').load("referrals.html");

  // $('#referr').load("network_content_Vfinal.html");

  // $('#friend_request').load("friend_request.html");
  //  alert("YES");
  $('.scroll').css('height', $(window).height()*0.6);
  $('.tab-content').css('height', $(window).height()*0.9);
  $('#paddingrow').css('height', $(window).height()*0.1);
  $('.card').addClass('bg-white shadow');
  $('#racommanding').css('height', $(window).height()*0.15);

  $('.leftmenutrigger').on('click', function(e) {
    $('.side-nav').toggleClass("open");
    e.preventDefault();
  });

  function toggleIcon(e) {
    $(e.target)
      .prev('.panel-heading')
      .find(".more-less")
      .toggleClass('glyphicon-plus glyphicon-minus');
  }

  $('.panel-group').on('hidden.bs.collapse', toggleIcon);
  $('.panel-group').on('shown.bs.collapse', toggleIcon);


  $("#request").click(function(){
      var color = clicked ? 'red' : 'black';
      $(this).css('background-color', color);
      clicked = !clicked;
  });

  // $('#referralbtn').on('click', function{
  //   $('body').css('background-color', #000);
  // });

});
