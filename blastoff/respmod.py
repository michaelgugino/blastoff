import pylw.response

class BlastOffResponse(pylw.response.Response):

    def HTTP404Error(self):
        self.status = '404 Not Found'
        self.body = '<html><body>The page you were looking was not found</body></html>'
        self.add_header('Content-Type','text/html')
