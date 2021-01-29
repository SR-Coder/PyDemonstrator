

document.addEventListener('DOMContentLoaded', function(event){
    document.getElementById('open').addEventListener('click', function(event){
        document.getElementById('leftMenu').style.width="200px";
    })
    document.getElementById('close').addEventListener('click', function(event){
        document.getElementById('leftMenu').style.width="0px"
    })
})

