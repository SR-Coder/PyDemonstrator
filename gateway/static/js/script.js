// Displays the login and registration
const hideDiv = (data) => {
    var eleID = document.getElementById(data).parentElement.id;
    var ele = document.getElementById(data).parentElement
    const register = document.getElementById("register")
    const login = document.getElementById("login")
    console.log(data,eleID, ele)
    if(eleID === "register"){
        if(ele.classList.contains("hidden")){
            ele.classList.remove("hidden")
            ele.classList.add("visible")
        } else {
            ele.classList.remove('visible')
            ele.classList.add('hidden')
            login.classList.remove('hidden')
            login.classList.add('visible')
        }
    } else if(eleID ==="login"){
        if(ele.classList.contains('hidden')){
            ele.classList.remove('hidden')
            ele.classList.add('visible')
        } else {
            ele.classList.remove('visible')
            ele.classList.add('hidden')
            register.classList.remove('hidden')
            register.classList.add('visible')
        }
    }
    
}
// ---------------------------------------------------------------------
// Custom Frontend Validations for register
var errors = []

// email regex validator front end
function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function onChangeHandler(data){
    var elementID = data.id + "Err"
    var tgtDiv = document.getElementById(elementID)
    console.log(data.id)
    if(data.id == "fName" || data.id == "lName"){
        if(data.value.length < 3){
            tgtDiv.innerHTML = "Must be greater than two characters!"
            errors.push(data.id)
        } else if(data.value.length >2){
            tgtDiv.innerHTML = ""
            errors.pop()
        }
    }
    if(data.id == 'eMailr'){
        console.log(validateEmail(data.value))
        if(data.value.length<2 || !validateEmail(data.value)){
            tgtDiv.innerHTML = "Invalid email address"
        } else {
            tgtDiv.innerHTML = ""
        }
    }
}
const toBinary = (dec) => {
    return (dec >>> 0).toString(2)
}

function updateClock() {
    var now = new Date(), // current date
        months = ['January', 'February', 'March','April', 'May', 
                'June', 'July', 'August', 'September', 'October', 
                'November', 'December'];
        if(now.getSeconds()<10){
            var seconds = '0'+now.getSeconds();
        } else {
            var seconds = now.getSeconds();
        }
        // convert to binary
        seconds = toBinary(seconds)
        hours = toBinary(now.getHours())
        minutes = toBinary(now.getMinutes())
        time = hours + ':' + minutes + ":" + seconds
        
        date = [now.getDate(), 
            months[now.getMonth()],
            now.getFullYear()].join(' ');
        
        var timeFromEpoch = Date.now()

    // document.getElementById('time').innerHTML = [date, time].join(' / ');
    document.getElementById('time').innerHTML =  ['EOT:' , toBinary(timeFromEpoch)].join(' ');
    // console.log(seconds)
    setTimeout(updateClock, 1);
}

document.addEventListener('DOMContentLoaded', function(event){
    document.getElementById('registerBtn').addEventListener('click', function(event){
        fname = document.getElementById('fName')
        lname = document.getElementById('lName')
        email = document.getElementById('eMailr')
        pw = document.getElementById('pWordr')
        cpw = document.getElementById('chkPword')
        console.log(validateEmail(email.value))
        if(fname.value<2 || lname.value<2 || pw.value<8 || pw.value!=cpw.value || !validateEmail(email.value) ){
            event.preventDefault()
        }
    })
    document.getElementById('open').addEventListener('click', function(event){
        document.getElementById('leftMenu').style.width="200px";
    })
    document.getElementById('close').addEventListener('click', function(event){
        document.getElementById('leftMenu').style.width="0px"
    })
    updateClock()
})
