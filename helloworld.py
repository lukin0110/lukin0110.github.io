import logging
import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.dist import use_library
#use_library('django', '0.96')
# force to use 0.96 because 1.2 doesnt properly include subtemplates
# http://code.google.com/appengine/docs/python/tools/libraries.html#Django



class IndexPage(webapp.RequestHandler):
    def get(self):
        values = {}
        self.response.out.write(template.render('templates/index.html',values))

          
# loading the mappings
mappings = [('/', IndexPage)]


# initialize the app with the mappings
application = webapp.WSGIApplication(mappings,debug=True)


def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()





