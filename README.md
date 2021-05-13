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
    * [Project Tracking](#Project-Tracking)
    * [Web Design](#Web-Design)
    * [Code](#Code)
    * [Testing](#Testing)
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

### Unit Testing 

### Integration Testing 

## Front End Design

## Future Improvements 

### Project Tracking

### Web Design 

### Code 

### Testing 

## Author
David Papworth