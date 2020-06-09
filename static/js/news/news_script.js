window.onload = function () {
    let forumMenuSvg = document.querySelector(".forum_menu_svg_320px");
    let popUpWindowForum = document.querySelector(".pop_up_window_forum_320px");
    let menuLogotypeQuitForum = document.querySelector(".menu_logotype_quit_forum");
    let contentForum = document.querySelector(".content_forum");

    forumMenuSvg.addEventListener("click", function (e) {
        popUpWindowForum.style.display = "flex";
        contentForum.style.display = "none";
    })

    menuLogotypeQuitForum.addEventListener("click", function (t) {
        popUpWindowForum.style.display = "none";
        contentForum.style.display = "flex";
    })
}