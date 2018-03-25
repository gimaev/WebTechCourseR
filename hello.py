def app(environ, start_response):

    data = environ['QUERY_STRING']
    d = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

    status = '200 OK'
    response_header = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return d