# ReadME - Project Instruction
Portfolio Project 3 – User SureDeveloping – Code Institute

## Rock-Paper-Scissors Extended project overview
### Introduction to the project
The create programme in this project is a Rock Paper Scissors online game. In this created version the items Lizard and Spock have been added to have more variety in the game. This variant is known from the series the big band theory. The game is based on chance and luck. It can be played against the computer.

### Contents
[Introduction to the project](#introduction-to-the-project) \
[Contents](#contents) \
[Game play](#gameplay) \
[User experience (UX)](#user-experience)\
[Target audience](#target-audience)\
[User story](#user-story)\
[Flow Chart](#flow-chart) \
[Features](#features) \
[Technologies used](#technologies-used) \
[Software and frameworks used](#software-and-frameworks-used) \
[Languages used](#languages-used) \
[Deployment](#deployment) \
[Testing](#testing) \
[Manual testing](#manual-testing) \
[Slack peer group rewiew](#slack-peer-group-rewiew) \
[Validator tests](#validator-tests) \
[Solved bugs](#solved-bugs) \
[Known unsolved bugs](#known-unsolved-bugs) \
[Credits](#credits) \
[Code used](#code-used) \
[Content on the website](#content-on-the-website) \
[Learning materials](#learning-materials) \
[Acknowledgments](#acknowledgments)

### Gameplay
First, the player is asked for his name. This allows the computer to address them directly later. When a game has been started, the player chooses by entering a number. Rock, Paper, Scissors, Lizard or Spock. At the same time, the computer also selects its object using a random function. The computer then chooses who has won and displays this. 
Here are the criteria according to which the computer chooses:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporises Rock
Rock crushes Scissors

The player can play as often as he likes. It is possible to cancel after each round.

## User experience (UX)
### Target audience of the website
- People who like Browsergamers.
- People who want to pass some free time.
- People who want to play the game Rock-Paper-Scissors- Lizard- Lizard against the computer.

### User story
As a first time user of the game, you want to:
- Play a bug-free game.
- Play a self-explanatory game.
- Be able to navigate easily over the terminal window
- Know the rules of the game.
find a Highscoure display on the site.???????????


As a frequent user of the website, you want to:
- Repeat the game experience.
- Improve the last game result.


Objectives of the website operator is to:
- Provide an easy to navigate and to play game.
- Provide a feedback of all user inputs.
- Provide an error free game.
- Provide an entertaining diversion to pass the time.


How this requirements are met:
- The game will be free to play.
- There will be a welcome page from which the player can navigate.
- All important elements will be shown in the terminal.
- A response is given to every user input, especially if the input is not expected by the computer.
- The player can display the rules.
- There is always the possibility to cancel the game.

### Flow Chart
Here are the Flowsharts created with draw.io:

![Flow Chart](images/flowchart-rpsls.png "Flow Chart")

### Features
Start Screen:
From the start screen, the user can start the game or view the rules. By pressing P starts the game and pressing R takes you to the rules.
An incorrect letter or number has been entered.
In this case, a message is displayed to the user that only R or P are permitted in upper or lower case.

Screenshots ???

Rules Screen:
Once R has been selected on the start screen, the rules are displayed. At the end of the text, the player can start the game or return to the main menu.
An incorrect letter or number has been entered.
In this case, a message is displayed to the user that only R or P are permitted in upper or lower case.
Screenshots ???

Play the Game Screen:
First, the player is asked to enter a name. 
Potential errors:
the name field cannot remain empty:
checking if the string length is zero

Screenshots ???

Future Implementations:
Sound Effects : 
 - As a further improvement, the game sound effects could be added. This would give your player an even better experience and also appeal to the sense of hearing.
Login function:
- A login function allows the player to beat and overwrite his old highscore list. This prevents a player from appearing more than once in the highscore list with the same name.

## Technologies used
### Languages used
Python is used for the project. For the landingpage HTML, CSS  were used to customised it.
### Software used
Draw.io - To create a Flow Chart. <br>
Gitpod - To code the project. <br>
Git - For version control. <br>
Github - To store to project. <br>
Heroku – to deploy the project. <br>
Ci Python Linter – To validate the python code. <br>
Deepl - For translating text. <br>
Birme - To change the image to webp format and reducing the size of the images. <br>  ?????

### Data Moduel
-	Which data module is used     ??????????
- Structure of the Modul ??????????
- How is data stored organized and manipulated????????????

### Libraries
These libraries were used for this project:
- Random: To make a random selection of the items of the computer.
- OS: To clear the terminal so that not too much irrelevant text is displayed
- Colorama: To add colour to the text
- Art: To be able to use an ASCII font for the start screen.

## Deployment
Forking???
Playing on a Local machine or via Gitpod Terminal:     CHECKEN CHECKen!!!!!
????
The project was coded with gitpod, stored on github and then deployed on Heroku. That is how the deployment was done:
1.	Log in to Heroku or create an account if required.
2.	Click on the New Button on the dashboard in the top right corner.
3.	Click on "Create new app".
4.	Select the relevant region. In my case, I chose Europe.
5.	Click on the "Create app" button.
6.	Navigate to the settings tab and scroll down to the "Config Vars" section.
7.	Click "Reveal Config Vars" and enter the "key" as port, the "value" as 8000 and click the "add" button.
8.	Scroll to the buildpacks and click on " add buildpack," select "Python," and click "Save Changes".
9.	Repeat step 8 but this time add "node.js" instead of python. 
o	IMPORTANT First the python buildpack must be displayed, then the pack from node.js. It can be moved via drag and drop. 
10.	Scroll to settings page, and click on Deploy tab.
11.	Click on Github as the deployment method.
12.	Confirm the connection to GitHub.
13.	Search for the repository name and click on conncet.
14.	Select one of the deployment types: 
o	Automatic deployment "Enable Automatic Deploys" or
o	Manual deployment "Deploy Branch”.

## Testing
The page was tested on different ways and different errors came to light.
### Manual testing
I tested all the buttons by clicking on them and playing the game several times. This was done during the hole prozess while creating this project and especially at the end. A detailed description of the bugs can be found in solved and unsolved bugs.

### Slack peer groupe rewiew
James Evans has tested my game and noticed that everything is running well. He also discovered a spelling mistake which I have corrected. 
### Validator tests
PEP8 Linter:
https://pep8ci.herokuapp.com/

SCREENSHOT!!!


### Solved bugs
I tried to check several conditions at the same time with a while loop. So: "while not player_choice == "1" or not "2" or not" . This was the wrong approach. The player_choice function was modified with a try and expect block.

At first I had not made the variables won_games, lost_games, played_games and drawn_games global. This way they could not be accessed outside the find-winner function.

In addition, I had formatted an f string incorrectly so that the variables were not displayed correctly in the terminal at first. Improving the formatting could fix this.

The ASCII font of the start screen was initially too large for the terminal. This was detected after deployment. By trying several fonts, another suitable combination could be found.

I had forgotten to add a while loop to the main_menu and the end_game function. Therefore several wrong user inputs were not handled correctly and the programme stopped. Because of the while loops the user is asked again until the answer is valid.

### Known unsolved bugs
- There are no known unsolved problems.
## Credits
### Code used
- I love sandwhiches PP3 - code institute ????
- ????
- I have informed and inspired myself about some functions in Youtube tutorials. The videos I watched are listed under Learning materials.
### Content for the project
The content of this project was written by Stephan Sure.
### Learning materials
- All content from Online Course in Full Stack Software Developmen especially videos about Portfolio Project 3 and ReadME from Code Instituet
- https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/ - to get a basic idear
- https://www.youtube.com/watch?v=I9h1c-121Uk&t=37s – Learn about the input function
- https://www.w3schools.com/python/ref_string_isalpha.asp - Learn about isalpha method
- https://www.w3schools.com/python/ref_string_strip.asp#gsc.tab=0 - learn about the string method
- https://www.python-lernen.de/python-modul-os.htm - learn about the os module
- https://www.geeksforgeeks.org/clear-screen-python/ - learn about the os module
- https://www.youtube.com/watch?v=HcqgHbvN0EQ - learn about the random module
- https://www.youtube.com/watch?v=46yolPy-2VQ - basic information on python
- https://stackoverflow.com/
- geekforgeeks
- W3Schools

### Acknowledgments
I like to thank the follow persons for the help during the project:
- My Code Institute mentor Spencer Barriball.
- The Tutor Support team at Code Institute.
- Slack pear groupe.
- To all people who make their knowledge available for free in the internet, especially on youtube.

**This project is for educational use only and was created for the Code Institute course Full stack software development by Stephan Sure.**