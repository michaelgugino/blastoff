#!/usr/bin/env python

# Copyright 2015 Michael Gugino
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''This is the main script, used to start the application'''
import os, glob
import pylw.app as app
import pylw.routing
import views.index_view
import views.new_post_view
import respmod
import cache_helper
import redis

from jinja2 import Environment, PackageLoader
jenv = Environment(loader=PackageLoader('blastoff', 'jinja_templates'))

def get_templates(jtemplate_dict):
    jtemplatenames = glob.glob(os.path.join('blastoff', 'jinja_templates', '*.html'))
    for temp in jtemplatenames:
        tsplit = temp.split('/')
        ti = tsplit[len(tsplit) - 1]
        jt = jenv.get_template(ti)
        jtemplate_dict[ti] = jt
        

jtemplate_dict = dict()
get_templates(jtemplate_dict)

redpool = redis.ConnectionPool(host='localhost', db=0)
redcon = redis.Redis(connection_pool=redpool)

config_dict = {
    'resp_class' : respmod.BlastOffResponse,
    'router' : pylw.routing.CRouter()
}

ch = cache_helper.CacheHelper(redcon=redcon)
kl = ['templates:site-header','templates:index','templates:site-footer']
ch.load_from_cache(kl)
user_objects = {
    'ch' : ch,
    'jtemplate_dict' : jtemplate_dict
}

myapp = app.App(secret_key="testing", config_dict=config_dict, user_objects=user_objects)

myapp.router = pylw.routing.CRouter()
myapp.router.add_path('/new_post', views.new_post_view.NewPost())
myapp.add_hard_coded_path('/',views.index_view.Index())
