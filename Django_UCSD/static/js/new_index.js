
$(document).ready(function() {
    // Load SignUp PopUp
    //alert('hello');
      //console.log('hello');
    //$('#signin-popup').load('/templates/login.html');
    $('#signin-popup').load('/templates/signin_integrated.html');
    $('#logout-successful-div').load('/templates/logout_successful.html');

    //initial condition
    var c = $('input[type=checkbox]').prop('checked');
    console.log(c);
    if (c==false){
        $('#buttons').hide();
    }
    else{
        $('#buttons').show();
    }
    // onclick condition
    $('#rightcorner').on('click', function(){
        var c = $('input[type=checkbox]').prop('checked');
        console.log(c);
        if (c==false){
            $('#buttons').hide(200);
        }
        else{
            $('#buttons').show(300);
        }
    });
  });
