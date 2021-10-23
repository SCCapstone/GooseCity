from wsgiref.simple_server import  make_server

def cloth(enviro,response):
    print("cloth page")
    response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return '<h2>welcome to see cloth!!!</h2>'

def shoes(enviro,response):
    print("shoes page")
    response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

    return '<h2 style= "color:red">welcome to see shoes!!!</h2>'

def url_distribute():

    urls = {
        '/cloth': cloth,
        '/shoes': shoes,
    }
    return urls
def run_server(arg1,response):
    print('thank you for watch')
   # print(arg1)
    #print (arg2)
    #get the all urls

    url_list=url_distribute()
    request_url=arg1.get("PATH_INFO")
    print ('request url', request_url)

    if request_url in url_list:
        func_data = url_list[request_url](arg1,response)
        return func_data
    else:
        response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
        return '<h1 style="font-size:50px">404,Page not found! </h1>'


# response("200 OK",[('Content-Type','text/html;charset=utf-8')])
   # return '<h2>dasdasfasfdaf</h2>'

s=make_server('localhost',8003,run_server)
s.serve_forever()