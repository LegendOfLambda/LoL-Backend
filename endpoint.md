REGISTRATION:

(POST) /API/REGISTRATION - creates user login

{
"username": "",
"email": "",
"password1": "",
"password2": ""
}

responds with user token

GAME FUNCTIONS:

(GET) /API/INIT - initializes player based on token
(POST) /API/MOVE - moves player based on direction input {"direction": "n/e/s/w"}
(GET) /API/ROOMS - retrieves all the rooms
