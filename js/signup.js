var user=document.querySelector('#us');
user.addEventListener('keyup',function(){ 
       var span=document.querySelector('#sp3');  
       if(user.value.length==0 || user.value.length<8){
           user.style.border='1px solid red';
           span.style.display='block';
       }
       else{
        user.style.border='1px solid green';
        span.style.display='none';
       }
})

var password=document.querySelector('#pass');
password.addEventListener('keyup',function(){ 
       var span=document.querySelector('#sp4');
       var input=document.querySelector("#submit");
       if(password.value.length==0 || password.value.length<8){
        password.style.border='1px solid red';
           span.style.display='block';
           input.disabled=false;
       }
       else{
        password.style.border='1px solid green';
        span.style.display='none';
        input.disabled=true;
       }
})

var cpassword=document.querySelector('#cpass');
cpassword.addEventListener('keyup',function(){
     var password=document.querySelector('#pass');
       var span=document.querySelector('#sp5'); 
       var span2=document.querySelector('#sp6');
       var input=document.querySelector("#submit"); 
       if(cpassword.value==password.value){
            cpassword.style.border='1px solid green';
            span.style.display='none';
            span2.style.display='block';
            span2.style.color='green';
            input.disabled=false;
       }
       else{
        cpassword.style.border='1px solid red';
        span.style.display='block'; 
        span2.style.display='none';
        input.disabled=true; 
       }
})
