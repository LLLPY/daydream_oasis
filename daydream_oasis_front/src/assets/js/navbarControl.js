

export default {

    created() {
        changeStatus()
    }


}
let has_logined = true

function changeStatus() {


    const spansWithAAA = document.querySelector('span');

    spansWithAAA.forEach(function (span) {
        if (span.textContent === '登录/注册🚪') {
            // 处理内容为 "aaa" 的 <span> 元素
            console.log(span);
        }else{
            console.log(11111);
        }
    });



}



window.onload = function () {
    changeStatus()
}