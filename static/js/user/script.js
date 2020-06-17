window.onload = function(el){
    let gameUser = document.querySelector('.game_user');
    let friendsUser = document.querySelector('.friends_user');
    let subscribe = document.querySelector('.subscribe');

    let userAllGame = document.querySelector('.user_all_game');
    let userFriends = document.querySelector('.user_friends');
    let markChecked = document.querySelector('.mark_checked');

    gameUser.addEventListener('click', function(t){
        userAllGame.style.display = 'flex';
        userFriends.style.display = 'none';
    });

    friendsUser.addEventListener('click', function(t){
        userAllGame.style.display = 'none';
        userFriends.style.display = 'flex';
    });
    if (subscribe){
        subscribe.addEventListener('click', function(t){
            markChecked.style.display = 'flex';
        });
    };


    let userPhoto = document.querySelector('.user_photo');
    let userPhotoSettings = document.querySelector('.user_photo_settings')
    userPhoto.addEventListener('mouseover', function (q) {
        userPhotoSettings.style.display = 'flex';
    });
    userPhoto.addEventListener('mouseout', function (q) {
        userPhotoSettings.style.display = 'none';
    });
}