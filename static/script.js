// loginbtn=document.querySelector('#login-btn')
// loginform=document.querySelector('#loginform')
// container=document.querySelector('.container')
// loginbtn.addEventListener("click",function(){
//     container.style.opacity=.3
//     loginform.style.display="block"
// })
// container.addEventListener("click",function(){
//     container.style.opacity=1
//     loginform.style.display="none"
// })

function fileValidation() {
    var fileInput = 
        document.getElementById('formFile');
     
    var FilePath = fileInput.value;
 
    if (FilePath == '') {
        alert("Please upload an image");

    } else {
        var Extension = FilePath.substring(
                FilePath.lastIndexOf('.') + 1).toLowerCase();
     

if (Extension == "gif" || Extension == "png" || Extension == "bmp"
            || Extension == "jpeg" || Extension == "jpg"){
                return true
            }
else{
    alert("Enter a image file")
    return false
} 
    
}
}

