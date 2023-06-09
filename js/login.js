
var email=document.querySelector('#email');
var password=document.querySelector('#passwords');
email.addEventListener('keyup',function(){
       var u_times = document.querySelector('.u_times');
       var u_check = document.querySelector('.u_check'); 
       var span=document.querySelector('#sp1');
       var input=document.querySelector("#signin");
       if(email.value.length==0 || email.value.length<8){
           email.style.border='1px solid red';
           u_times.style.display='block';
           u_check.style.display='none';
           span.style.display='block';
           input.disabled=true;
       }
       else{
        email.style.border='1px solid green';
        u_times.style.display='none';
        u_check.style.display='block';
        span.style.display='none';
        input.disabled=false;
       }
})
password.addEventListener('keyup',function(){
       var u_times = document.querySelector('.c_times');
       var u_check = document.querySelector('.c_check'); 
       var span=document.querySelector('#sp2');
       var input=document.querySelector("#signin");
       if(password.value.length==0 || password.value.length<6){
        password.style.border='1px solid red';
           u_times.style.display='block';
           u_check.style.display='none';
           span.style.display='block';
           input.disabled=true;
       }
       else{
        password.style.border='1px solid green';
        u_times.style.display='none';
        u_check.style.display='block';
        span.style.display='none';
        input.disabled=false;
       }
})

