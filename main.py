#!/usr/bin/env python
"""
Example for Facebook Python SDK
Author: Colin Su <littleq0903@gmail.com>
"""
from bottle import Bottle, run, template
from bottle import static_file
from bottle import request
from bottle import jinja2_template
import facebook

import os
import json

# setup these environment variable by adding "heroku.config"
# - FACEBOOK_APP_ID
# - FACEBOOK_SECRET
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']

# WSGI handler
app = Bottle()

# Checkpoint 0
@app.route('/login')
def login():
    template_data = {
        'facebook_app_id': FACEBOOK_APP_ID
    }
    return jinja2_template('index.html', **template_data)

# Checkpoint 1
@app.route('/cp1')
def cp1():
    cookies = request.cookies
    print cookies
    fb_user = facebook.get_user_from_cookie(cookies, FACEBOOK_APP_ID, FACEBOOK_SECRET)

    fb_access_token = fb_user["access_token"]
    fb_graph = facebook.GraphAPI(fb_access_token)
    profile = graph.get_object("me")

    return json.dumps(profile)
    
