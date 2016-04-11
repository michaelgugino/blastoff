'''This is the index view'''
import pylw.resource
import blastoff.Objects
import cgi
import uuid

class NewPost(pylw.resource.DefaultResource):
    '''The index of our site.'''
    
#TODO: implement categories and tags.

    def on_get(self,req,resp,user_objects=None):

        #Check the session here.
        signed_cookies = resp.get_signed_cookie('testk')
        #check for user logged in session
        username = resp.get_signed_cookie('username')

        if username is None:
            resp.status = '503 Unauthorized'
            resp.body = 'Unauthorized, you must be logged in'
            resp.add_header('Content-Type','text/html')
            #TODO: #SECURITY: get rid of this.
            resp.add_signed_cookie('username','testadmin')
            return

        #Load things from userobjects
        ch = user_objects['ch']
        jtd = user_objects['jtemplate_dict']
        cdict = ch.cache_dict


        editortext = "[b]Enter your job description here[/b]. [color=#B22222]Javascript and HTML are prohibited[/color]. [color=#008000]BBCode is valid.[/color]"
        try:
            upload_widget = jtd['upload_widget.html'].render()
            body_html = jtd['new_post.html'].render(editortext=editortext, upload_widget=upload_widget)
            header_html = jtd['newpost-header.html'].render()
            resp.body = str(header_html) + str(body_html) + cdict['templates:site-footer']
        except Exception as ex:
            print ex
            resp.body = 'bad'
        resp.add_signed_cookie('testk','value1')
        resp.add_cookie('unsigned_testk','value1')
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'

    def on_post(self,req,resp,user_objects=None):
        #Check the session here.
        #check for user logged in session
        username = resp.get_signed_cookie('username')

        if username is None:
            resp.status = '503 Unauthorized'
            resp.body = 'Unauthorized, you must be logged in'
            resp.add_header('Content-Type','text/html')
            #TODO: #SECURITY: get rid of this.
            resp.add_signed_cookie('username','testadmin')
            return

        #Load things from userobjects
        ch = user_objects['ch']
        jtd = user_objects['jtemplate_dict']
        cdict = ch.cache_dict

        formdata = cgi.FieldStorage(
            environ=req.raw_env,
            fp=req.raw_env['wsgi.input'])
        try:
            postuuid = formdata['postuuid'].value
        except:
            postuuid = uuid.uuid4().hex

        try:
            posttext = formdata['posttext'].value
            posttitle = formdata['posttitle'].value
        except:
            #TODO: log something here.
            self.on_get(req,resp,user_objects)

        post_dict = {
            username + '::' + postuuid : posttext,
            username + '::' + postuuid + '::title' : posttitle}

        ch.put_in_cache(post_dict)

        parser = blastoff.Objects.updateParser()
        previewtext = parser.format(posttext)
        editortext = posttext
        try:
            upload_widget = jtd['upload_widget.html'].render()
            body_html = jtd['new_post.html'].render(
                posttitle=posttitle,
                editortext=editortext,
                upload_widget=upload_widget,
                previewtext=previewtext,
                postuuid=postuuid)
            header_html = jtd['newpost-header.html'].render()
            resp.body = str(header_html) + str(body_html) + cdict['templates:site-footer']
        except Exception as ex:
            print ex
            resp.body = 'bad'
        resp.add_header('Content-Type','text/html')
        resp.status = '200 OK'
