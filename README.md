#food service
Task: to develop a simple questionnaire system

The user should be able to have a simple dialog with the system and to go through predefined questions and answers.

Dialog example:
`
Are you hungry? (Yes/No)
   Yes:
       What would you like to eat? (Hamburger/Pizza/Pop Corn/Chicken)
           Hamburger:
               Nice, I will order a hamburger for you!
           Pizza:
               Would you like pizza with mushrooms? (Yes/No)
                   Yes:
                       Ok, I will order the best pizza in town for you
                   No:
                      No? Well... stay hungry then
   No:
       Ok. Call me when you're hungry.
       `

The system consists of two parts: user app (frontend) and backend.

Frontend functionality:
1. Show questionnaires list in responsive and styled format (user can select what questionnaire he/she will pass)
2. Go through Q&A (show question and possible answers to the user)
3. Requests must be AJAX
4. Spinner must be implemented and every action must be disabled on start of AJAX request and re-enabled after comletion or error
5. error handling must be done and displayer errors in proper design and format

Backend functionality:
1. Load questionnaires structure from JSON file
2. REST API for user app (questionnaires list)
3. When the conversation finished (last question answered) the backend should log the conversation history into the console. The log should contain the first question and all subsequent user answers. Example: `Are you hungry?: Yes -> Pizza -> Yes`

Limitations:
1. The server shouldn't return the whole dialog tree via one response. The system should be interactive (should load next question and answer variants only)
2. The backend should be developed with django
3. The frontend must be in jQuery (allowed to use jquery plugins) and no modern framework shall be used (vue, react, angular and ...)

