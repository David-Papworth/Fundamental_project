from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Figure, Army

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAddArmy(TestBase):
    TEST_CASES = [("army 1","this is army 1")]

    def submit_input(self, name, description):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(description)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_army')
        for name, description in self.TEST_CASES:
            self.submit_input(name, description)
            self.assertIn(url_for('view_army'), self.driver.current_url)

            text = self.driver.find_element_by_xpath('/html/body/div[1]').text
            self.assertEqual(text, name)

            text = self.driver.find_element_by_xpath('/html/body/div[2]').text
            self.assertEqual(text, description)

            entry = Army.query.filter_by(name=name, description=description).first()
            self.assertNotEqual(entry, None)
    
class TestAddFigure(TestBase):
    TEST_CASES = [("Terminators","6","Choas","")]

    def submit_input(self, name, description):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="number_of_models"]').send_keys(description)
        self.driver.find_element_by_xpath('//*[@id="faction"]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="army"]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_figure')
        for name, number_of_models, faction, army in self.TEST_CASES:
            self.submit_input(name, number_of_models, faction, army)
            self.assertIn(url_for('home'), self.driver.current_url)

            text = self.driver.find_element_by_xpath('/html/body/div[1]').text
            self.assertEqual(text, name)

            text = self.driver.find_element_by_xpath('/html/body/div[2]').text
            self.assertEqual(text, number_of_models)

            text = self.driver.find_element_by_xpath('/html/body/div[3]').text
            self.assertEqual(text, faction)

            text = self.driver.find_element_by_xpath('/html/body/div[4]').text
            self.assertEqual(text, army)

            entry = Army.query.filter_by(name=name, number_of_models=number_of_models, faction=faction, army=army).first()
            self.assertNotEqual(entry, None)