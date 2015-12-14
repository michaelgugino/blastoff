import blastoff.main as main
from wsgiref import simple_server
myapp = main.myapp
def run():
    #api = myapp.MyAPI()
    httpd = simple_server.make_server('127.0.0.1', 8000, myapp)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
