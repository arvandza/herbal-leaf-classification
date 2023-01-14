function fileValidation(){
    var fileInput = document.getElementById('image');
    var filePath = fileInput.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Wrong Extension!');
        fileInput.value = '';
        return false;
    }
}