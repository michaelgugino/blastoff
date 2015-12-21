'''This is the index view'''
import pylw.resource

class Index(pylw.resource.DefaultResource):

    def on_get(self,req,resp,user_objects=None):
        signed_cookies = resp.get_signed_cookie('testk')
        ch = user_objects['ch']
        jtd = user_objects['jtemplate_dict']
        blog_posts = []
        blog_posts.append(jtd['post.html'].render())

        index_dict = {
            'blog_posts' : blog_posts,
            'blog_title' : 'Blog Index',
            'blog_description' : 'Blastoff! blog'
        }
        tempindex = jtd['index.html'].render(**index_dict)
        #print tempindex
        cdict = ch.cache_dict
        #resp.body = cdict['templates:site-header'] + cdict['templates:index'] + cdict['templates:site-footer']
        resp.body = cdict['templates:site-header'] + str(tempindex) + cdict['templates:site-footer']
        resp.add_signed_cookie('testk','value1')
        resp.add_cookie('unsigned_testk','value1')
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'

    def on_post(self,req,resp,user_objects=None):
        self.on_get(req,resp,user_objects)
