'''This is the index view'''
import pylw.resource
import cgi


class FormUpload(pylw.resource.DefaultResource):
    '''A page for handling uploads via post'''

    def on_get(self,req,resp,user_objects=None):
        resp.add_header('Content-Type','text/html')
        resp.status = '404 NOT FOUND'
        resp.body = '404 NOT FOUND'

    def on_post(self,req,resp,user_objects=None):
        formdata = cgi.FieldStorage(
            environ=req.raw_env,
            fp=req.raw_env['wsgi.input'])

        if 'newfile' in formdata and formdata['newfile'].filename != '':

        file_data = formdata['newfile'].file.read()
        filename = formdata['newfile'].filename

        # write the content of the uploaded file to a local file
        target = os.path.join('media', filename)
        f = open(target, 'wb')
        f.write(file_data)
        f.close()
