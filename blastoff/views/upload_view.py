'''This is the index view'''
import pylw.resource
import cgi
import json
import os


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
        print formdata
        if 'newfile' in formdata and formdata['newfile'].filename != '':

            file_data = formdata['newfile'].file.read()
            filename = formdata['newfile'].filename

            # write the content of the uploaded file to a local file
            target = os.path.join('blastoff','media', filename)
            try:
                f = open(target, 'wb')
                f.write(file_data)
                f.close()
            except Exception as ex:
                print ex

        res = {
                "files": [
                  {
                    "name": "picture1.jpg",
                    "size": 902604,
                    "url": "http:\/\/example.org\/files\/picture1.jpg",
                    "thumbnailUrl": "http:\/\/example.org\/files\/thumbnail\/picture1.jpg",
                    "deleteUrl": "http:\/\/example.org\/files\/picture1.jpg",
                    "deleteType": "DELETE"
                  },
                  {
                    "name": "picture2.jpg",
                    "size": 841946,
                    "url": "http:\/\/example.org\/files\/picture2.jpg",
                    "thumbnailUrl": "http:\/\/example.org\/files\/thumbnail\/picture2.jpg",
                    "deleteUrl": "http:\/\/example.org\/files\/picture2.jpg",
                    "deleteType": "DELETE"
                  }
                ]}
        resp.body = json.dumps(res)
        resp.add_header('Content-Type','application/json')
        resp.status = '200 OK'
