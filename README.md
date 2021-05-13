# Fundamental_project - Warhammer Armies

## Contents 
* [Introduction](#Introduction)
    * [Requirements](#Requirements)
    * [My Idea](#My-Idea)
    * [User Stories](#User-Stories)
    * [My Plan](#My-Plan)
* [Architecture](#Architecture)
    * [Database Structure](#Database-Structure)
    * [CI Pipeline](#CI-Pipline)
* [Project Tracking](#Project-Tracking)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
    * [Unit Testing](#Unit-Testing)
    * [Integration Testing](#Integration-Testing)
* [Front End Design](#Front-End-Design)
* [Future Improvements](#Future-Improvements)
    * [Project Tracking](#Project-Tracking-Improvement)
    * [Web Design](#Web-Design-Improvement)
    * [Code](#Code-Improvement)
    * [Testing](#Testing-Improvement)
* [Author](#Author)

## Introduction
The object of the project was “To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training”.

This means I had to make a website with create, read, update and delete functions and perform tests to make sure the site was working to the specifications.

### Requirements
* A Trello board
* A database with at least 2 tables, with at least a one-to-many relationship.
* A detailed risk assessment. 
* A functioning CRUD application using python.
* Automated test units 
* A working front-end website using Flask
* Integration into a Version Control System (Github) 

### My Idea
My idea for this project was to create a website where people could add Warhammer figures and armies so they could organise what they own and set up the armies they use. 

### User Stories
The first step was to create user stories to plan what needed to be done and why. As well as getting a better perspective on the project.

* As a customer, I want to add a new set of figures, so I can update my collection. (*)
* As a customer, I want to view my figures, so I know what I own. (*)
* As a customer, I want to change the number of the figures I own, so I can keep up do date with what I own. (*)
* As a customer, I want to remove figures, as I have sold or don’t own anymore. (*)
* As a customer, I want to add a new army, so I can organise the armies I will use. (*)
* As a customer, I want to view my armies, to see what armies I have. (*)
* As a customer, I want to change my armies, so I keep my armies up to date. (*)
* As a customer, I want to remove armies, as I have stopped using them. (*)
* As a customer I want a add my figures into an army, to plan armies I will use. (*)
* As a customer, I want to view an army list that shows all the figures that are part of that army, so I can see what each are contains. 

(*) = user stories to complete crud functionality 

### My Plan 
* Create a home page that shows the figures you own.
* Add an update and delete button for every figure added (on the home page). 
* Create a add figure page.
* Make a add figure form.
* Create a view army page that shows the armies you own.
* Add an update and delete button for every army added (on the view army page). 
* Create a add army page.
* Make a add army form.
* Create unit tests for all pages as well for the CRUD functions. 
* Create Integration tests for at least one method.

## Architecture
### Database Structure
The picture below shows the entity relationship diagram (ERD) for the project, this is a one-to-many relationship.  This means 1 army could be made up of multiple figures but 1 figure could only be in one army. 


This second picture shows a planned many-to-many relationship between army and figures. Using a child table in the middle which as 2 one-to-many relationships. This would allow figures to be present in multiple armies. This was not able to be implemented in time but can be found in the Future improvements section explaining how I would have created this relationship. 
### CI Pipline


The picture above shows the CI pipeline used for this project. Continuous Integration allows me to automate testing as well as deployment of the website. This increases the speed and precision of the project. In my method, when the code is push to Github, Jenkins will fetch and build the repository, it will then run unit tests as well as integration tests.   This will then send a report to the developer informing of the result.
## Project Tracking
I used Trello for project tracking as free, light-wieght and easy to use. Below are a few images showing different stages of the sprint. The Trello board can be also found: https://trello.com/b/yidIppbC/devops-core-fundamental-project 


The key areas of the Trello:
Project backlog: Show the items not being worked on in the sprint during this sprint

Sprint backlog: Shows the items being worked on this sprint that have not been completed 

Review: Items that have been completed but need to be check if they are working to the set parameters 
Complete: Items that have been finished 

Also, Moscow was implemented on the project using tags (Green means must have, Orange Could have, Red won’t have).

The other colours of tags show which sections are related (e.g. the user story with the task to complete that user story).   

## Risk Assessment 
The risk assessment below shows all the risks involved with this project. 

## Testing 
All test was run using pytest and Jenkins. The first code shows the code used to the run the unit tests (test_unit file under the tests folder) in Jenkins. The second code was to run both the unit tests and integrations tests (both test files in the tests folder) in Jenkins it is also found as test.sh in the application. 

Code 1:
```
#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

export DATABASE_URI
export SECRET_KEY

pip3 install pytest pytest-cov flask_testing 
python3 -m pytest --junitxml=junit/test-results.xml --cov=application 
--cov-report=xml --cov-report=html
```
Code 2:
```
#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip python3-venv chromium-browser wget unzip -y
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip

python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

export DATABASE_URI
export SECRET_KEY
python3 -m pytest --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html
```
### Unit Testing 
This was used to make sure all the webpages and links worked correctly and if the CRUD functions worked as intended.

The image below shows a successful unit test in Jenkins. 

### Integration Testing 
This was used to make sure that the pathway a user would take would work at every step (e.g. button clicks, text entry, redirect).

The image below shows a successful full integrations and unit test test in Jenkins. 

## Front End Design
Below is the home page where you can see the figures you own, links to all the other pages, update and delete buttons for the figures you own. 

Below is the add figure page where you can the form that can filled out to add a figure as well as link to the other pages. 

Below is the view army page where you can see the armies you own, links to all the other pages, update and delete buttons for the armies you own. 

Below is the add amy page where you can the form that can filled out to add a army as well as link to the other pages. 

## Future Improvements 
* Add user logging so people can have their own account and don’t change other people’s data. 
### Project Tracking Improvement 
* Add checks to user stories rather then added them as extra items to reduce the number of items in the Trello broad.
### Web Design Improvement
* Changing the front end so more pleasing to the eye
### Code Improvement
* Create the many-to many relationship between figures and armies by making the child table. Creating a add page for the relationship as well as a form (2 select fields (army and figure) made the same way as the select army in the figures form). Finally making a view page where you can see the full list of all the army with the figures they hold. 
* Implement custom validators to make sure that the figure being added exist.  
* Increasing the number of factions to correct amount (currently 6 out of 22)
### Testing Improvement
* More interaction tests so that all the crud functions as well as other customer interactions are tested 
## Author
David Papworth