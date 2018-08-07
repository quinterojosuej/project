import webapp2
from random import shuffle
import jinja2
import os
#import requests
import urllib.request
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCXlRkL8rvN8cEiIV_t69tNAZdtKlbU6vY'
#r = request.get(https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCXlRkL8rvN8cEiIV_t69tNAZdtKlbU6vY, data = {'key':'value')

#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class project(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('css/project.html')
        
        self.response.write(about_template.render())
        
        
        college_select = {
        "UC Berkely": "", 
        "UC Davis": "",
        "UC Santa Cruz": "",
        "UC Irvine": "PG",
        "UC San Diego": "",
        "UC Riverside": "",
        "UCLA": "",
        "UC Merced": "",
        "UC Santa Barbara":"" 
        }


class resulsts(webapp2.RequestHandler):
    def get(self): 
        about_template = the_jinja_env.get_template('css/results.html')
        self.response.write(about_template.render())

    
app = webapp2.WSGIApplication([
    ('/', project),('/resulsts', resulsts),
], debug=True)
