window.onload = function () {
    btnBackStep2 = document.querySelector('.btn-back-step2');
    btnBackStep3 = document.querySelector('.btn-back-step3');

    btnBackStep2.addEventListener('click', function (ev) {
        formStep1 = document.querySelector('.form-step_1');
        formStep2 = document.querySelector('.form-step_2');
        formStep3 = document.querySelector('.form-step_3');
        formStep1.style.display = "flex";
        formStep2.style.display = "None";
        formStep3.style.display = "None";
    });

    btnBackStep3.addEventListener('click', function (ev) {
            formStep1 = document.querySelector('.form-step_1');
            formStep2 = document.querySelector('.form-step_2');
            formStep3 = document.querySelector('.form-step_3');
            formStep1.style.display = "None";
            formStep2.style.display = "flex";
            formStep3.style.display = "None";
    });
    btnStep1 = document.querySelector('.btn-step-1');
    btnStep1.addEventListener('click', function (ev) {
        formStep2 = document.querySelector('.form-step_2');
        formStep1 = document.querySelector('.form-step_1');
        formStep3 = document.querySelector('.form-step_3');
        formStep1.style.display = "None";
        formStep2.style.display = "flex";
        formStep3.style.display = "None";
    });
    btnStep2 = document.querySelector('.btn-step-2');
    btnStep2.addEventListener('click', function (ev) {
        formStep1 = document.querySelector('.form-step_1');
        formStep2 = document.querySelector('.form-step_2');
        formStep3 = document.querySelector('.form-step_3');
        formStep1.style.display = "None";
        formStep2.style.display = "None";
        formStep3.style.display = "flex";
    });
};
function showFileName() {
    let fileName = document.getElementById('id_avatar');
    usersAvatar = document.querySelector('.users-avatar');
        if(fileName.files && fileName.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                usersAvatar.src= e.target.result;
            }
            reader.readAsDataURL(fileName.files[0]);
        }
}
