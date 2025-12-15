const userJoin = document.querySelector('.userJoin');

userJoin.addEventListener('click', function(){
    const id = document.querySelector('.userId').value;
    const pw = document.querySelector('.userPw').value;
    const pw2 = document.querySelector('.userPw2').value;
    const name = document.querySelector('.userName').value;
    const phone = document.querySelector('.userPhone').value;
    const gender = document.querySelector('.gender').value;
    const mail = document.querySelector('.userEmail').value;
    const letter = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*?_]).{8,30}$/;
    const message = document.querySelector('.checkMessage')
    const userJoinForm = document.querySelector('.userJoinForm')
    if(!userJoinForm.checkValidity()){
        return;
    }    

    if(letter.test(pw)){
        if (pw == pw2){
            alert("회원가입이 완료 되었습니다.\n"+
                "아이디: " + id + "\n" +
                "비밀번호: "+ pw + "\n" +
                "이름: " + name + "\n" +
                "전화번호: " + phone + "\n" +
                "성별: " + gender +"\n" +
                "이메일: " + mail);
            window.location.replace('adminPage.html');
        }else{
            message.innerHTML = "비밀번호가 유효하지만 일치하지 않습니다."
        }
    }else{
        message.innerHTML = "비밀번호가 유효하지 않습니다."
    }
});

const darkButton = document.querySelector('.darkButton');
const topDiv = document.querySelector('.topDiv');
const body = document.body;
darkButton.addEventListener('click', function(){
    if(!document.body.classList.contains('dark')){
        darkButton.value = "화이트모드"
        body.classList.add('dark');
        topDiv.classList.add('dark');
    }else{
        darkButton.value = "다크모드"
        body.classList.remove('dark');
        topDiv.classList.remove('dark');
    }
});