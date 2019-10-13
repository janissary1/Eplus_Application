function openModal(modal){
    document.getElementById(modal).style.display="block";
    document.getElementById("file_name").innerHTML = document.getElementById("myfile").files.item(0).name;
}
function closeModal(modal){
    document.getElementById(modal).style.display="none";
    document.getElementById("myfile").value = null;

}