import blastoff.main as main
from wsgiref import simple_server
import os
from werkzeug.wsgi import SharedDataMiddleware

myapp = main.myapp
myapp = SharedDataMiddleware(myapp, {
    '/static': os.path.join(os.path.dirname(__file__), 'blastoff','static'),
    '/js': os.path.join(os.path.dirname(__file__), 'blastoff','js'),
    '/media': os.path.join(os.path.dirname(__file__), 'blastoff','media')
})




def run():
    #api = myapp.MyAPI()
    httpd = simple_server.make_server('127.0.0.1', 8000, myapp)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
