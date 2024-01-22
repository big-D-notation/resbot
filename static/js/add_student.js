'use strict';

window.onload = () => {
    const studentNameField    = document.getElementById('student_name'),
            studentGroupField = document.getElementById('student_group'),
            studentTgField    = document.getElementById('student_tg'),
            submitButton      = document.getElementById('add_student_button');
            

    submitButton.addEventListener('mouseover', function() {
        if (!fieldsAreEmpty()) {
            submitButton.classList.add('button_green');
            submitButton.classList.remove('button_red');
            
            return;
        }

        submitButton.classList.add('button_red');
        submitButton.classList.remove('button_green');
    });

    function fieldsAreEmpty() {
        return studentGroupField.value === '' 
        || studentNameField.value === ''
        || studentTgField.value === ''; 
    }
}
