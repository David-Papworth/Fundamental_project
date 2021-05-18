# Fundamental_project - Warhammer Armies 

## Contents 
* [Introduction](#Introduction)
    * [Requirements](#Requirements)
    * [My Idea](#My-Idea)
    * [User Stories](#User-Stories)
    * [My Plan](#My-Plan)
* [Architecture](#Architecture)
    * [Database Structure](#Database-Structure)
    * [CI Pipeline](#CI-Pipeline)
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
The objective of this project was “To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training”.

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
The first step was to create user stories to plan what was required, as well as getting a better perspective of the project.

* As a customer, I want to add a new set of figures, so I can update my collection. (*)
* As a customer, I want to view my figures, so I know what I own. (*)
* As a customer, I want to change the number of the figures I own, so I can keep up do date with my collection. (*)
* As a customer, I want to remove figures, as I don’t own them anymore. (*)
* As a customer, I want to add a new army, so I can organise the armies I use. (*)
* As a customer, I want to view my armies, to see what armies I have. (*)
* As a customer, I want to change my armies, so I keep my armies up to date. (*)
* As a customer, I want to remove armies, as I have stopped using them. (*)
* As a customer I want a add my figures into an army, to organise armies I will use. (*)
* As a customer, I want to view an army list that shows all the figures that are part of this army, so I can see the contents of each army. 

(*) = user stories to complete crud functionality 

### My Plan 
* Create a home page that shows the figures you own.
* Add an update and delete button for every figure added (on the home page). 
* Create an add figure page.
* Make an add figure form.
* Create a view army page that shows the armies you own.
* Add an update and delete button for every army added (on the view army page).
* Create an add army page.
* Make an add army form.
* Create unit tests for all pages and the CRUD functions. 
* Create Integration tests for at least one method.

## Architecture
### Database Structure
The figure below shows the entity relationship diagram (ERD) for the project, this is a one-to-many relationship.  This means 1 army could be made up of multiple figures but 1 figure/model can only be in one army. 
![Image showing a one to many relationship between Army and Models/Figures](https://i.imgur.com/6Za6sc5.png?1)

This second figure shows a planned many-to-many relationship between army and figures. Using a child table in the middle which has 2 one-to-many relationships. This would allow figures to be present in multiple armies. This was not able to be implemented in time but can be found in the Future improvements section explaining how I would have created this relationship. 
![Image showing a many to many relationship between Army and Models/Figures](https://i.imgur.com/wn0Roh0.png?1)
### CI Pipeline
![Image showing the CI Pipeline for this project](https://i.imgur.com/EtHJZMc.png?1)

The figure above shows the CI pipeline used for this project. Continuous Integration allows me to automate testing as well as deployment of the website. This increases the speed and precision of the project. In my method, when the code is pushed to Github, Jenkins will fetch and build the repository, it will then run unit tests as well as integration tests.   This will then send a report to the developer informing them of the result.
## Project Tracking
I used Trello for project tracking as it is free, light-wieght and easy to use. Below are a few images showing different stages of the sprint. The Trello board can be also found here: https://trello.com/b/yidIppbC/devops-core-fundamental-project 

![Image showing the start of the first sprint](https://i.imgur.com/n0edHb6.png?1)
![Image showing complete website and unit tests with integration tests to be done](https://i.imgur.com/MrlXnHr.png?1)
![Image showing the end of the first sprint](https://i.imgur.com/3CQXO2C.png?1)

Figure 1 is the start of the project with only the database setup of the project

Figure 2 shows the complete website and unit test with only integration tests remaining to complete the first sprint. This figure also shows the integration test that have been added to the Trello since the start of the project. 

Figure 3 is the end of the first sprint with all the items complete in the sprint backlog. 


The key areas of the Trello:

Project backlog: Shows the items not being worked on in the sprint during current sprint

Sprint backlog: Shows the items being worked on this sprint which have not been completed 

Review: Items that have been completed but need to be tested to see if they are working to the set parameters 

Complete: Items that have been finished 

Also, Moscow was implemented on the project using tags (Green means must have, Orange Could have, Red won’t have).

The other colours of tags show which sections are related (e.g. the user story with the task to complete that user story).   

## Risk Assessment 
The risk assessment below shows all the risks involved with this project.
![Image showing the risk assessment for the project](https://i.imgur.com/33nKU2C.png?1)

All item highlighted in grey were risks added during the project sprint. 
## Testing 
All test was run using pytest and Jenkins. Code 1 was used to run the unit tests (test_unit file under the tests folder) in Jenkins. Code 2 was used to run both the unit tests and integrations tests (both test files are stored in the tests folder) in Jenkins it is also found as test.sh in the application. 

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
This was carried out to make sure all the webpages and links worked correctly and if the CRUD functions worked as intended. This was also used to run a coverage report. Coverage shows the number of lines the code reads though and ran to completion in pytest it doesn’t identify whether the code has given the intended output only that it had been run. We checked for the intended output by adding assertions to compare the output with a selected item (text, status code, etc). 

The code below shows a unit test to confirm if going to the home page would return a status 200 (success) meaning the webpage would load correctly. 
```
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
```
The code below shows the unit test for adding an item into the army data and checking if those items appeared on the view army page.
```
class TestCreate(TestBase):
    def test_create_army(self):
        response = self.client.post(url_for('add_army'),
        data=dict(name='new army', description="This is my new army"),
        follow_redirects=True
        )
        self.assertIn(b"This is my new army", response.data)
        self.assertIn(b"new army", response.data)
```
The figure below shows a successful unit test in Jenkins. 
![Image showing a sucessful coverage and unit test in Jenkins](https://i.imgur.com/PVVT8Dw.png?1)
As you can see in the figure above there was improvement in the coverage between test 2 and 3 from about 90% to 100% and all the test passed successfully. 

My code covers all the CRUD functions as well as status 200 for all the webpages and functions used. A few additional unit tests that could be implemented. These could include a test to check if when someone tries to type into the search bar the update page for a item that is not present in the data (e.g /update_army/5 when there are only 4 armies) they would receive a message to tell them to return to the view army page as this item does not exists (this would need some additional code added to the update item function to check if the int number is greater the number of armies in the database and then return the desired text). Another test I could implement is to check when incorrect text is added, an error message would displayed rather than allowing this data to be addded to the database (a custom validator would need to be made to check for these incorrect submissions).
### Integration Testing 
This was used to make sure that the pathway a user takes would work at every step (e.g. button clicks, text entry, redirect).

The code below shows the integration test for adding an army 
```
class TestAddArmy(TestBase):
    TEST_CASES = [("army 1","this is army 1"), ("army 2","this is army 2"), ("army 3","this is army 3")]

    def submit_input(self, name, description):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(description)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        i = 1
        for name, description in self.TEST_CASES:
            self.driver.get(f'http://localhost:{self.TEST_PORT}/add_army')
            self.submit_input(name, description)
            self.assertIn(url_for('view_army'), self.driver.current_url)

            text = self.driver.find_element_by_xpath(f'/html/body/div[{i}]').text
            self.assertIn(name, text)

            text = self.driver.find_element_by_xpath(f'/html/body/div[{i+1}]').text
            self.assertIn(description, text)

            entry = Army.query.filter_by(name=name, description=description).first()
            self.assertNotEqual(entry, None)
            i += 2
```

The image below shows a successful full integration and unit test in Jenkins. 
![Image showing a sucessful integration test in Jenkins](https://i.imgur.com/p4wcUBU.png?1)
My integration tests cover both adding an army and a figure. Additional integration tests that could be implemented include tests for the remaining crud functions, tests for when incorrect data is added to the system and a error message appears (custom validators would need to be added), and if a person went to an incorrect webpage they would be able to return correctly. 
## Front End Design
Below is the home page where you can see the figures you own, links to all the other pages, update and delete buttons for the figures you own. 

![Image showing the home/view figure page](https://i.imgur.com/1UH4dN9.png?1)

Below is the add figure page where you can see the form which is completed to add a figure as well as link to the other pages. 

![Image showing the add figure page](https://i.imgur.com/uUJWvw6.png?1)

Below is the view army page where you can see the armies you own, links to all the other pages, update and delete buttons for the armies you own. 

![Image showing the view army page](https://i.imgur.com/2IdR774.png?1)

Below is the add army page where you can complete the form to add a army as well as link to the other pages. 

![Image showing the add army page](https://i.imgur.com/qe3JD7Z.png?1)

## Future Improvements 
* Add user logging so people can have their own account without changing other people’s data. 
### Project Tracking Improvement 
* Add checks to user stories rather then adding as extra items to reduce the number of items in the Trello broad.
### Web Design Improvement
* Changing the front end so more pleasing to the eye
### Code Improvement
* Create the many-to many relationship between figures and armies by making the child table. Creating an add page for the relationship as well as a form (2 select fields (army and figure) made the same way as the select army in the figures form). Finally make a view page where you can see the full list of all the armies and the figures they hold. 
* Implement custom validators to make sure that the figure being added exist.  
* Increasing the number of factions to correct amount (currently 6 out of 22)
* Use multiple Vcs / implement Gunicorn to reduce loss of service.
* Make the website into a demon process so it can run in the background.
### Testing Improvement
* More integration tests so that all the crud functions as well as other customer interactions are tested 
* Stress tests such as to check if x button is pressed (x times) will the website break, how many user would it take to crash the site and if a button is pressed multiple times (quickly)  will it give the correct response each time.
## Author
David Papworth  
