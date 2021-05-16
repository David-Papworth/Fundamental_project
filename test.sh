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
