<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <title>ArmQuiz</title>
  <link rel="shortcut icon" href="https://previews.123rf.com/images/jovanas/jovanas1810/jovanas181000353/109413496-quiz-icon.jpg" type="image/x-icon">

	<style>
		.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}
#que1{
	  background-size: 100% 100%;

	text-align: center;

		height:364px; 
	display: flex;
  align-items: flex-end;  
}
#que{
	font-size: 60px;
	margin:0;
	 color: yellow;
  text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
}
#an{
	text-align: center;
}
#answe{
	text-align: center;
	display: inline-block;
	
 
}
#an1{
	text-align: center;
}
.button2{
	height: 100px;
    width: 100px;
     position: sticky;
    font-size: 50px;
}
#und1, #red1{
	display: inline-block;
}
#enter{
    display: flex;
    justify-content: center;
    margin: auto;
}
.button1:hover {
  background-color: #4CAF50;
  color: white;
}
.text1{
	  border-style: solid;
  border-color: red;
}
.a{
	border:0;
}
.st{
	
	font-size: 30px;
}
.modal-footer{
	display: flex;
  justify-content: space-between;
}
.aa{
	margin-top: 90px;
	
}
.as{
	background-color: transparent;
	border-radius: 5px;
}
.ar{
	border:0;
	

}
.at{
	text-align: center;


}
.al{
	color: #DE0101;
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	font-size:45px;
	 font-family:"Courier New", Courier, monospace;
	

}
.endr{
	 margin:auto;
}
.gif{
	text-align: center;	
}
.wo{
	color:rgb(0 43 255);
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	font-size: 40px;
}
.rat{
	color: rgb(255 25 25);
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	font-size: 50px;
}
.off{
	margin:auto;
}
</style>
</head>
<body>
  <div class="modal fade" id="basicExampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>











  
	<div id="que1"><p id="que", class=""></p></div>
	<div id="an" >
		<div id="und1"></div>
		<div id="answe"></div>
		<div id="red1"></div>
	</div>
 <div id="an1">    <div id="r"></div></div>
 <button id="enter" class="btn btn-warning st"></button>













<!-- Modal -->
<div id="myModal" class="modal fade aa" role="dialog">
  <div class="modal-dialog as">

    <!-- Modal content-->
    <div class="modal-content as">
      <div class="modal-body at">
        <p class="al" id="al1"></p>
      </div>
      
      <div class="modal-footer ar" id="fsyo">
      	<button type="button" class="btn btn-success  " id="but1"  data-dismiss="modal">Նախորդը</button>
      	<button type="button" class="btn btn-warning "  id="but2" data-dismiss="modal">Կրկին փորձել</button>
        <button type="button" class="btn btn-danger"  id="but3" data-dismiss="modal">Հաջորդը</button>
      </div>
    </div>

  </div>
</div>


<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    
    <div class="modal-content as">
      <div class="modal-body at">
        <p class="wo" id="wo1"></p>
        <p class="rat" id="rat1"> </p>
      </div>

      <div class="modal-body gif">
         <img  id="im1" , style="width:450px;" >
         
      </div>
      	
        
           
   
  </div>
</div>





</div>
<audio id="idAudio"> 
  <source src= 
"https://www.fesliyanstudios.com/play-mp3/640"
      type="audio/ogg"> 
  
Your browser does not support the audio element. 
</audio> 
<audio id="idAudio1"> 
  <source src= 
"https://www.fesliyanstudios.com/play-mp3/7"
      type="audio/ogg"> 
  
Your browser does not support the audio element. 
</audio> 
<audio id="idAudio2"> 
  <source src= 
"https://www.fesliyanstudios.com/play-mp3/2897"
      type="audio/ogg"> 
  
Your browser does not support the audio element. 
</audio>

	<script>

    
let ques=["Ո՞րն է Ավստրալիայի մայրաքաղաքը",'Ո՞ր երկրի դրոշն է պատկերված նկարում','Ո՞վ է գրել «Աստվածային կատակերգությունը»․',"Եթե խառնենք կապույտն ու դեղինը, ի՞նչ գույն կստանանք․",'Արեգակից թվով 4-րդ մոլորակը',"Քիմիական տարրերի պարբերական համակարգում ո՞ր տարրն է նշանակվում Cu-ով․","Աշխարհի ամենամեծ անապատը․","Ատոմի կազմի մեջ մտնող դրական լիցքավորված մասնիկը կոչվում է",'Շրջանագծի երկու կետերը միացնող և դրա կենտրոնով չանցնող հատվածը կոչվում է․․․','Ո՞րն է ԱՄՆ-ի մայրաքաղաքը'];
let answ=["ԿԱՆԲԵՐԱ",'ԻՐԱՆ','ԴԱՆԹԵ',"ԿԱՆԱՉ",'ՄԱՐՍ',"ՊՂԻՆՁ",'ՍԱՀԱՐԱ','ՊՐՈՏՈՆ',"ԼԱՐ","ՎԱՇԻՆԳԹՈՆ"]
let img=["https://3er1viui9wo30pkxh1v2nh4w-wpengine.netdna-ssl.com/wp-content/uploads/2017/08/canberra.jpg",  "https://mediamag.am/wp-content/uploads/2020/07/iran-162321_960_720.png","https://www.vnews.am/wp-content/uploads/2019/11/%D6%86%D6%86%D6%86%D6%86%D6%86%D6%86%D6%86%D6%86%D6%86-1.jpg","https://media.swncdn.com/via/5793-istockgetty-images-pluspattadis-walarput.jpg",'https://ak.picdn.net/shutterstock/videos/26205473/thumb/1.jpg',"https://wallpaperplay.com/walls/full/f/c/9/207912.jpg","https://lh4.googleusercontent.com/-SDwKa_xTC94/UVLhhfscRXI/AAAAAAAAAnQ/IwKMuVOGvxE/s2000/sahara.jpg","https://i.pinimg.com/originals/7e/d6/1a/7ed61a337b0cccb1598fe5fd1b9724bf.jpg","https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b0e08472-4f08-4bb4-a7cd-0498560143f7/d4z8omn-e14d4bd7-3a7d-414e-b904-835977d75937.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYjBlMDg0NzItNGYwOC00YmI0LWE3Y2QtMDQ5ODU2MDE0M2Y3XC9kNHo4b21uLWUxNGQ0YmQ3LTNhN2QtNDE0ZS1iOTA0LTgzNTk3N2Q3NTkzNy5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ._k4a3IArwrYoDoE2N2Qt4GsnMpGovNfWCtZL5sWlsTc", "https://wallpaperaccess.com/full/459022.jpg"]

	
let obj =["Ա", "Բ","Գ","Դ","Ե", "Զ","Է","Ը","Թ", "Ժ", "Ի","Լ","Խ","Ծ", "Կ","Հ","Ձ", "Ղ", "Ճ","Մ","Յ","Ն", "Շ", "Ո","Չ" , "Պ","Ջ","Ռ","Ս", "Վ", "Տ","Ր" ,"Ց", "ՈՒ", "Փ","Ք" , "և", "Օ","Ֆ"]
let z=0; 
let t=-1;
let l="";
let b=0
window.onload = function () {
	document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
}
document.getElementById("but1").onclick=function(){
	t=-1;
     l="";
  for (var p = 0; p <= (answ[z].length-1); p++) {
          	document.getElementById('self'+p).remove();
          }
        z-=1
        
    for(var d=0;d<=(answ[z].length-1); d++){
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
    ans1.onclick=function(){
        this.innerHTML=" "
        t-=1
        l=l.slice(0, -1)
         }
    }
        document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
        que.textContent=ques[z];
}
document.getElementById("but2").onclick=function(){
  l="";
  t=-1
  for (var p = 0; p <= (answ[z].length-1); p++) {
          	document.getElementById('self'+p).remove();
          }
        
        
    for(var d=0;d<=(answ[z].length-1); d++){
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
    ans1.onclick=function(){
        this.innerHTML=" "
        t-=1
        l=l.slice(0, -1)
         }
    }
  
  
}
document.getElementById("but3").onclick=function(){
	t=-1;
    l="";
    console.log(l)
  for (var p = 0; p <= (answ[z].length-1); p++) {
          	document.getElementById('self'+p).remove();
          }
    z+=1   
    for(var d=0;d<=(answ[z].length-1); d++){
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
    ans1.onclick=function(){
        this.innerHTML=""
        t-=1
        l=l.slice(0, -1)
        
         }
    }
    document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
     que.textContent=ques[z]; 
        que.textContent=ques[z];
        document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
       
}


var que=document.getElementById('que');
que.textContent=ques[z];
let undo = document.createElement("img");
    document.getElementById("und1").appendChild(undo);
    undo.setAttribute("src", 'https://www.shareicon.net/data/128x128/2016/11/09/851210_arrows_512x512.png')
    undo.style.width = '62px'

    undo.onclick=function(){
        for (var p = 0; p <= (answ[z].length-1); p++) {
          	document.getElementById('self'+p).remove();
          }
        z-=1
        l="";
  t=-1
        
    for(var d=0;d<=(answ[z].length-1); d++){
      
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
    ans1.onclick=function(){
        this.innerHTML=" "
        t-=1
        l=l.slice(0, -1)
         }
    }
        document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
        que.textContent=ques[z];
        
    }

let ans1=0;
for(var d=0;d<=(answ[z].length-1); d++){
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
  
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
   
    ans1.onclick=function(){
        this.innerHTML=" "
        t-=1
        l=l.slice(0, -1)
        var GFG = document.getElementById("idAudio1"); 
            GFG.play();
       
         }


}

let redo = document.createElement("img");
    document.getElementById("red1").appendChild(redo);
    redo.setAttribute("src", 'https://www.shareicon.net/data/128x128/2016/11/09/851191_arrows_512x512.png')
    redo.style.width = '62px'
    redo.onclick=function(){
        if (z==9) {

        }
        else{ 
        	for (var p = 0; p <= (answ[z].length-1); p++) {
          	document.getElementById('self'+p).remove();
          }
        z+=1
        l="";
         t=-1


        
    for(var d=0;d<=(answ[z].length-1); d++){
      
    ans1 = document.createElement("button");
    document.getElementById("answe").appendChild(ans1);    
    ans1.setAttribute("id", "self"+d);
    ans1.setAttribute('class',"btn btn-dark button2 btn-outline-success ol")
    ans1.onclick=function(){
        this.innerHTML=" "
        t-=1
        l=l.slice(0, -1)
         }
    }
    document.getElementById("que1").style.backgroundImage = "url("+img[z]+")";
     que.textContent=ques[z];      
     }   
    }

let u=0
let end=0
for(var i=0 in obj){
    let lett = document.createElement("button");
    document.getElementById("r").appendChild(lett);
    lett.classList.add("button1");
    lett.textContent = obj[i];
    lett.style.display = 'inline-block'
    lett.style.fontSize = '40px'
    lett.setAttribute('class',"btn btn-outline-danger a") 

    lett.onclick=function(){
          t+=1;
          var GFG = document.getElementById("idAudio"); 
            GFG.play(); 
            document.getElementById('self'+t).innerHTML=lett.textContent;
            l+=document.getElementById('self'+t).innerHTML
            
        }
}

let ent=document.getElementById("enter")
document.body.appendChild(ent)
ent.textContent="Ստուգել Պատասխանը";
ent.setAttribute('data-toggle', "modal")
ent.setAttribute('data-target', "#myModal")
ent.onclick=function(){
  var GFG = document.getElementById("idAudio2"); 
            GFG.play();



            
            if (z==9) {let end1 = document.createElement("button");
                document.getElementById("fsyo").appendChild(end1); 
                end1.textContent="Ավարտել"
                end1.setAttribute('class',"btn btn-danger endr")
                end1.setAttribute('data-dismiss',"modal")
                end1.setAttribute('data-toggle', "modal")
                end1.setAttribute('data-target', "#exampleModal")
                end1.onclick=function(){
                	if(end<=5){
                       document.getElementById("wo1").innerHTML="«ՍՈՎՈՐԵԼ, ՍՈՎՈՐԵԼ, ՍՈՎՈՐԵԼ»"
                       document.getElementById("rat1").innerHTML=end+"/10"
                       document.getElementById("im1").setAttribute("src", "https://media1.giphy.com/media/61lMnpz0sKkpi/200.gif")
                	}
                	else if (end>=6 && end<=8) {
                		document.getElementById("wo1").innerHTML="Դու կարող ես ավելին"
                       document.getElementById("rat1").innerHTML=end+"/10"
                       document.getElementById("im1").setAttribute("src", "https://media0.giphy.com/media/xT4ApmfvO9u0fg0aA0/giphy.gif")
                	}
                	else{
                		document.getElementById("wo1").innerHTML="Հրաշալի է!!!"
                       document.getElementById("rat1").innerHTML=end+"/10"
                       document.getElementById("im1").setAttribute("src", "https://media1.tenor.com/images/aefe2183126bc29cfe549f6b7ef33b70/tenor.gif?itemid=5576708")

                	}
                }
            	document.getElementById("but1").remove();
            	document.getElementById("but3").remove();
            	document.getElementById("but2").remove();	
            }
             if (l==answ[z]){
                end+=1
             
               	document.getElementById("al1").innerHTML="Ճիշտ է!!!"
               	
               }
               else if (l.length<answ[z].length) {
                     document.getElementById("al1").innerHTML="Նշեք բոլոր տառերը"
               }
               else{
               	document.getElementById("al1").innerHTML="Սխալ է!!!"
               }
     
	
}


            console.log(z);
console.log(end)

 

            


  </script>
  
  <h3>Customer Form</h3>
  <hr>
  
  <form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit", value="Save">
  
  </form> 







<div class="table-responsive d-none d-sm-block">
  <!--Table-->
  <table class="table table-striped">

    <!--Table head-->
    <thead>
      <tr>
        <th>#</th>
        <th>Name</th>
        <th>Surname</th>
        <th>Age</th>
        <th>Points</th>
        
        
      </tr>
    </thead>
    <!--Table head-->

    <!--Table body-->
    <tbody>
      {% for der in user %}
      <tr>
        <th scope="row">{{der.id}}</th>
        <td>{{der.name}}</td>
        <td>{{der.username}}</td>
        <td>{{der.age}} </td>
        <td>{{der.points}}</td>
      </tr>
      {% endfor %}
    </tbody>
    <!--Table body-->
  </table>
  <!--Table-->
</div>







</script>




 <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
