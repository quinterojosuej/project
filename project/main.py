import webapp2
from random import shuffle
import jinja2
import os
# import urllib
import json 
import requests

# search = raw_input('Type Name: ')

# url = "https://maps.googleapis.com/maps/api/geocode/json"

# params = {
#     'address': search
# }

# headers = {
#     'key': 'AIzaSyCXlRkL8rvN8cEiIV_t69tNAZdtKlbU6vY'
# }

# r = requests.get(url, headers=headers, params=params)

# print r.json()



# # endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
# # api_key = 'AIzaSyCXlRkL8rvN8cEiIV_t69tNAZdtKlbU6vY'

# #libraries for APIs
# from google.appengine.api import urlfetch
# import json


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
         self.response.write(project_template.render())
     def post(self):
         origin = self.request.get('school')
         self.response.write(origin)
#         nav_request = 'school=() & key=()'.format(origin,api_key)
#         request = endpoint + nav_request
#         response = urllib.urlopen(request).read()
#         directions = json.loads(response)
#         print(directions)
        
        
        
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
     ('/results',results)
 ], debug=True)
