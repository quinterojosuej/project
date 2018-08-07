import webapp2
from random import shuffle
import jinja2
import os
#import requests
import urllib
import json 
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
        results_template = the_jinja_env.get_template('/project.html')
        #origin = input('What school are you in?')
        #nav_request = 'origin=() & key=()'.format(origin,api_key)
        #request = endpoint + nav_request
        #response= urllib.request.urlopen(request).read()
        #directions = json.loads(response)
        self.response.write(results_template.render())
    def post(self):
        origin = self.request.get('origin')
        self.response.write(origin)
        nav_request = 'origin=() & key=()'.format(origin,api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        directions = json.loads(response)

        
        
        
college_select = {
"UC Berkely": "", 
"UC Davis": "",
"UC Santa Cruz": "",
"UC Irvine": "",
"UC San Diego": "",
"UC Riverside": "",
"UCLA": "",
"UC Merced": "",
"UC Santa Barbara":"" 
}

        
app = webapp2.WSGIApplication([
    ('/', project),
], debug=True)
