window.onload = function(e){
    let step_1 = document.querySelector('.step1');
    let step_2 = document.querySelector('.step2');
    let end_step = document.querySelector('.end_step');

    let btn_success_1 = document.querySelector('.btn-success1');
    let btn_success_2 = document.querySelector('.btn-success2');

    btn_success_1.addEventListener('click', function(t){
        step_1.style.display = 'none';
        step_2.style.display = 'flex';
        end_step.style.display = 'none';
    });

    btn_success_2.addEventListener('click', function(t){
        step_1.style.display = 'none';
        step_2.style.display = 'none';
        end_step.style.display = 'flex';
    });
};


function showFileName() {
    let down_file = document.getElementById('id_avatar');
    let image = document.querySelector('.users-avatar');
    if (down_file.files && down_file.files[0]){
        let read_file = new FileReader();
        read_file.onload = function (r) {
            image.src = r.target.result;
        }
        read_file.readAsDataURL(down_file.files[0]);
    }
}
