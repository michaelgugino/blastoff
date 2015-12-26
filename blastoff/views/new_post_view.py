'''This is the index view'''
import pylw.resource


class NewPost(pylw.resource.DefaultResource):
    '''The index of our site.'''

    def on_get(self,req,resp,user_objects=None):
        signed_cookies = resp.get_signed_cookie('testk')
        ch = user_objects['ch']
        jtd = user_objects['jtemplate_dict']

        tempbody = jtd['upload_widget.html'].render()
        #tempbody = "testing"
        #print tempindex
        cdict = ch.cache_dict
        #resp.body = cdict['templates:site-header'] + cdict['templates:index'] + cdict['templates:site-footer']
        #resp.body = cdict['templates:site-header'] + str(tempbody) + cdict['templates:site-footer']
        try:
            resp.body = cdict['templates:site-header'] + str(tempbody) + cdict['templates:site-footer']
        except Exception as ex:
            print ex
            resp.body = 'bad'
        resp.add_signed_cookie('testk','value1')
        resp.add_cookie('unsigned_testk','value1')
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'

    def on_post(self,req,resp,user_objects=None):
        self.on_get(req,resp,user_objects)
