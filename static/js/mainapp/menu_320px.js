window.onload = function () {
    let menuTransition = document.querySelector(".menu_svg_320px");
    let popUpWindow = document.querySelector(".pop_up_window_320px");
    let content = document.querySelector(".content");
    let quit = document.querySelector(".menu_logotype_quit");

    menuTransition.addEventListener("click", function (e) {
        popUpWindow.style.display = "flex";
        content.style.display = "none";
    })

    quit.addEventListener("click", function (t) {
        popUpWindow.style.display = "none";
        content.style.display = "flex";
    })
}