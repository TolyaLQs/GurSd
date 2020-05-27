window.onload = function () {
    let likeSvg = document.querySelector('.like_svg');
    let like = document.querySelector('.like');

    /*likeSvg.addEventListener('click', function (t) {
        like = document.querySelector('.like');
        like.style.fill = "red";
    });*/

    /*likeSvg.addEventListener('click', function (t) {
        like = document.querySelector('.like');
        like.style.fill = "black";
    });*/
    trek1 = document.querySelector('.trek1');
    trek2 = document.querySelector('.trek2');
    trek3 = document.querySelector('.trek3');
    btnBackStep1 = document.querySelector('.btn-back-step1');
    btnBackStep2 = document.querySelector('.btn-back-step2');
    btnBackStep1.addEventListener('click', function (ev) {
        formStep2 = document.querySelector('.form-step_2');
        formStep1 = document.querySelector('.form-step_1');
        formStep3 = document.querySelector('.form-step_3');
        formStep3.style.display = "None";
        formStep2.style.display = "None";
        formStep1.style.display = "flex";
        activeStep = document.querySelector('.activestep');
        activeStep.classList.remove('activestep');
        trek1.classList.add('activestep');
    });
    btnStep1 = document.querySelector('.btn-step-1');
    btnStep1.addEventListener('click', function (ev) {
        formStep2 = document.querySelector('.form-step_2');
        formStep1 = document.querySelector('.form-step_1');
        formStep3 = document.querySelector('.form-step_3');
        formStep3.style.display = "None";
        formStep1.style.display = "None";
        formStep2.style.display = "flex";
        activeStep = document.querySelector('.activestep');
        activeStep.classList.remove('activestep');
        trek2.classList.add('activestep');
    });
    btnStep2 = document.querySelector('.btn-step-2');
    btnStep2.addEventListener('click', function (ev) {
        formStep1 = document.querySelector('.form-step_1');
        formStep2 = document.querySelector('.form-step_2');
        formStep3 = document.querySelector('.form-step_3');
        formStep1.style.display = "None";
        formStep2.style.display = "None";
        formStep3.style.display = "flex";
        activeStep = document.querySelector('.activestep');
        activeStep.classList.remove('activestep');
        trek3.classList.add('activestep');
        btnBackStep2.addEventListener('click', function (ev) {
            formStep2 = document.querySelector('.form-step_2');
            formStep1 = document.querySelector('.form-step_1');
            formStep3 = document.querySelector('.form-step_3');
            formStep3.style.display = "None";
            formStep2.style.display = "flex";
            formStep1.style.display = "None";
            activeStep = document.querySelector('.activestep');
            activeStep.classList.remove('activestep');
            trek2.classList.add('activestep');
        });
    });

};

function registration() {


}


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
