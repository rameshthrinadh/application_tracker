var sname,sid,semail,ssubject,smessage;
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var name = $('.validate-input input[name="name"]');
    var id=$('.validate-input input[name="id"]');
    var email = $('.validate-input input[name="email"]');
    var subject = $('.validate-input input[name="subject"]');
    var message = $('.validate-input textarea[name="message"]');
    sname=name;
    sid=id;
    semail=email;
    smessage=message;
    ssubject=subject;


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(name).val().trim() == ''){
            showValidate(name);
            check=false;
        }
        if($(id).val().trim() == ''){
            showValidate(id);
            check=false;
        }

        if($(subject).val().trim() == ''){
            showValidate(subject);
            check=false;
        }


        if($(email).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
            showValidate(email);
            check=false;
        }

        if($(message).val().trim() == ''){
            showValidate(message);
            check=false;
        }

             
   

        return check;
    });

    


    $('.validate-form .input1').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);


function geetdata(){
    
    applications[applications.length].application_no=applications[applications.length-1].application_no+1;
    applications[applications.length].application_id=sid;
    applications[applications.length].subject=ssubject;
    applications[applications.length].message=smessage;
    
}



applications =[
    {
        "application_no": 1,
        "applicant_id":"S160931",
        "subject":"Application for PUC Consolidate grade sheet",
        "message":"gjagacjgjas",
        "step" :3,
        "type":"ms"
        
    },
    {
        "application_no": 2,
        "applicant_id":"S160404",
        "subject":"Application for PUC Consolidate grade sheet",
        "message":"gjagacjgjas",
        "step" :2,
        "type":"ms",
        
    },
    {
        "application_no": 3,
        "applicant_id":"S160884",
        "subject":"Application for PUC Consolidate grade sheet",
        "message":"gjagacjgjas",
        "step" :1,
        "type": "ms"
        
    },
]

$(".ap-status").click(function(){
    console.log("clicked");
    var a =document.getElementById("status");
    a.setAttribute("class","row my-5 visible w3-animate-opacity")
});
var ops=document.createTextNode(applications[0].applicant_id);
