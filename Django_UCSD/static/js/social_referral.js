$(document).ready(
  function() {
    $('#sidebarText').load("sidebar.html");
    $('#Topright').load("index_top_right.html");
    $('#keywordsearch').load("one_filter_search_bar_referral.html");
    $('#referrals').load("referral_content.html");
    $('#oldfriend').load("old_friends.html");
    $('#newfriend').load("new_friends.html");

    //  alert("YES");
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
  });

function toggleIcon(e) {
  $(e.target)
    .prev('.panel-heading')
    .find(".more-less")
    .toggleClass('glyphicon-plus glyphicon-minus');
}
$('.panel-group').on('hidden.bs.collapse', toggleIcon);
$('.panel-group').on('shown.bs.collapse', toggleIcon);
