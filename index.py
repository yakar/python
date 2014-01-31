def application(environ, start_response):
    import sys
    path = 'YOUR_WWW_ROOT_DIRECTORY'
    if path not in sys.path:
        sys.path.append(path)
    from pyinfo import pyinfo
    output = pyinfo()
    start_response('200 OK', [('Content-type', 'text/html')])
    return [output]
