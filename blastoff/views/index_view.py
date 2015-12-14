'''This is the index view'''
import pylw.resource

class Index(pylw.resource.DefaultResource):

    def on_get(self,req,resp,user_objects=None):
        signed_cookies = resp.get_signed_cookie('testk')
        ch = user_objects['ch']
        cdict = ch.cache_dict
        resp.body = cdict['site-header'] + cdict['index-body'] + cdict['site-footer']
        resp.add_signed_cookie('testk','value1')
        resp.add_cookie('unsigned_testk','value1')
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'

    def on_post(self,req,resp,user_objects=None):
        self.on_get(req,resp,user_objects)
