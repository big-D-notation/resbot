'use strict'

window.onload = () => {
    const questionsContainer = document.getElementById('questions_container'),
          addQuestionButton  = document.getElementById('add_question_button'),
          submitButton       = document.getElementById('add_test_button');

    let currentQuestionNumber = 1;

    const questionTemplate = `
        <section class="question" id="question_{{current_number}}">
            <div class="question__title">
                Question {{current_number}}
            </div>

            <div class="question__text">
                <input class="form__input form__text_field" type="text" name="questions[{{current_number}}][text]">
            </div>

            <div class="options">
                <div class="option">
                    <input class="option__radiobutton" type="radio" name="questions[{{current_number}}][answer]" value="0">
                    <input class="option__textfield" type="text"    name="questions[{{current_number}}][options][0]">
                </div>

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="questions[{{current_number}}][answer]" value="1">
                    <input class="option__textfield" type="text"    name="questions[{{current_number}}][options][1]">
                </div>  

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="questions[{{current_number}}][answer]" value="2">
                    <input class="option__textfield" type="text"    name="questions[{{current_number}}][options][2]">
                </div>  

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="questions[{{current_number}}][answer]" value="3">
                    <input class="option__textfield" type="text"    name="questions[{{current_number}}][options][3]">
                </div>  
            </div>
        </section>
    `;


    function addQuestion() {
        let newQuestion = document.createElement('div');
        newQuestion.innerHTML = questionTemplate.replaceAll('{{current_number}}', currentQuestionNumber);
        questionsContainer.appendChild(newQuestion);
        currentQuestionNumber++;
    };

    addQuestionButton.addEventListener('mousedown', addQuestion);

    submitButton.addEventListener('mousedown', () => {
        let questions = Array.from(document.getElementsByClassName('question'));
        let questionsToSend = {};

        for (const question of questions) {
            questionsToSend[question.id] = {};
            questionsToSend[question.id]['title'] = question.getElementsByClassName('form__text_field')[0].value;

            let options = Array.from(question.getElementsByClassName('option'));

            questionsToSend[question.id]['options'] = [];

            for (const option of options) {
                let optionToSend = {};

                optionToSend['text']    = option.getElementsByClassName('option__textfield'  )[0].value;
                optionToSend['isRight'] = option.getElementsByClassName('option__radiobutton')[0].checked;

                questionsToSend[question.id]['options'].push(optionToSend);
            };
        };

        let jsonToSend = JSON.stringify(questionsToSend);
        const form = document.getElementById('form-add-test');

        let jsonContainer = document.createElement('textarea');
        jsonContainer.setAttribute('name', 'questions_json');

        jsonContainer.value = jsonToSend;
    
        form.appendChild(jsonContainer);
        form.submit();
    });
}
