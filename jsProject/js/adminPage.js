function updateTime(){
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    const formattedTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    document.querySelector('.nowTime').innerHTML = formattedTime;
}
setInterval(updateTime,1000);
updateTime();

const darkPageButton = document.querySelector('.darkPage');
const body = document.body;
const html = document.html;
darkPageButton.addEventListener('click', function(){
    if(document.body.classList.contains('dark')){
        darkPageButton.value = "다크모드";
        body.classList.remove('dark');
        document.documentElement.classList.remove('dark');
    } else {
        darkPageButton.value = "화이트모드";
        body.classList.add('dark');
        document.documentElement.classList.toggle('dark');   
    }
});