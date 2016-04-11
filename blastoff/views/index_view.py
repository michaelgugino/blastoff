'''This is the index view'''
import pylw.resource


class Index(pylw.resource.DefaultResource):
    '''The index of our site.'''

    def on_get(self,req,resp,user_objects=None):
        signed_cookies = resp.get_signed_cookie('testk')
        ch = user_objects['ch']
        cdict = ch.cache_dict
        jtd = user_objects['jtemplate_dict']
        blog_posts = []
        blog_posts.append(jtd['post.html'].render())
        title = "Blastoff!"
        index_dict = {
            'top_nav' : cdict['top_nav'],
            'blog_posts' : blog_posts,
            'blog_title' : cdict['blog_title'],
            'blog_description' : cdict['blog_description'],
            'sidebar_widgets' : cdict['sidebar_widgets']
        }


        try:
            body_html = jtd['index.html'].render(**index_dict)
            header_html = jtd['site-header.html'].render(title=title)
            resp.body = str(header_html) + str(body_html) + cdict['templates:site-footer']
        except Exception as ex:
            print ex
            resp.body = 'bad'
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'

    def on_post(self,req,resp,user_objects=None):
        self.on_get(req,resp,user_objects)
