const cursor = document.querySelector('#cursor')
const devs = document.querySelector('#title')

function addEffect(e) {
    cursor.style.left = (e.x - 275) + 'px';
    cursor.style.top = (e.y - 275) + 'px';
}

function removeEffect() {
    window.removeEventListener("mousemove", addEffect)
    cursor.style = '';
    devs.style.color = "black";
}

window.addEventListener('mousemove', addEffect)
devs.addEventListener("click", removeEffect)