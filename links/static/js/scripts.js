function askToConfirm(){
var a = confirm("Вы действительно хотите удалить линк?");
if (a == true) {
    document.write("deleted");
    window.location.replace("http://stackoverflow.com");

}
else document.write("nope");
return;
}