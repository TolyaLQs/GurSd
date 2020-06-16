window.onload = function () {
    let forumMenuSvg = document.querySelector(".forum_menu_svg_320px");
    let popUpWindowForum = document.querySelector(".pop_up_window_forum_320px");
    let menuLogotypeQuitForum = document.querySelector(".menu_logotype_quit_forum");
    let contentNews = document.querySelector(".content_news");

    forumMenuSvg.addEventListener("click", function (e) {
        popUpWindowForum.style.display = "flex";
        contentNews.style.display = "none";
    })

    menuLogotypeQuitForum.addEventListener("click", function (t) {
        popUpWindowForum.style.display = "none";
        contentNews.style.display = "flex";
    })
}