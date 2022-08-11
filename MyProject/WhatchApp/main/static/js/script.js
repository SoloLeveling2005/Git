
function open_chat(id){

  // console.log(document.getElementsByClassName('chat')[i].style )
  // document.getElementsByClassName('chat')[i].style = "display:flex;"
  var chats = document.getElementsByClassName("chat");
  for (var i = 0; i < chats.length; i++) {
     // Distribute(chats.item(i));
     console.log(chats.item(i))
     console.log(i)
     document.getElementsByClassName('chat')[i].style = "display:none;"
  }
  // alert(id);
  var id = "id_" + id 
  
  document.getElementById(id).style = "display:block;"
}


function open_block_new_chat(){
  document.getElementById('new_chat').style = "left:0px;"

}

function close_block_new_chat(){
  document.getElementById('new_chat').style = "left:-1000px;"

}



