function openModal(modal){
    document.getElementById(modal).style.display="flex";
    var file_name = document.getElementById("myfile").files.item(0).name;
    document.getElementById("file_name").innerHTML = file_name;
    
    if (!file_name.endsWith(".zip")){
        document.getElementById("compilebtn").setAttribute("disabled",true);
        document.getElementById("error_msg").style.display="flex";
    }
}
function closeModal(modal){
    document.getElementById(modal).style.display="none";
    document.getElementById("error_msg").style.display="none";
    document.getElementById("myfile").value = null; //reset the file selection
    document.getElementById("compilebtn").removeAttribute("disabled");

}

function submit(){
    alert(document.getElementById("myfile").value);
    document.getElementById("upload").submit();
}
