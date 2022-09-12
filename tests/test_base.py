import imp
from urllib import response
from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    
    def create_app(self): #this method is required by Flask-Testing
        app.config['TESTING'] = True #set the app in testing mode
        app.config['WTF_CSRF_ENABLED'] = False #disable CSRF protection
        
        return app

    def test_app_exists(self): #test if the app exists
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self): #test if the app is in testing mode
        self.assertTrue(current_app.config['TESTING']) #check if the app is in testing mode

    # def test_index_redirects(self): #test if the index redirects to /hello
    #     response = self.client.get(url_for('index')) #get the response of the index
    #     self.assertRedirects(response, url_for('hello')) #check if the response is a redirect to /hello

    def test_hello_get(self): #test if the hello page is accessible with GET
        response = self.client.get(url_for('hello')) #get the response of /hello
        self.assert200(response) #check if the response is 200 OK
