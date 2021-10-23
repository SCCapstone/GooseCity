from wsgiref.simple_server import  make_server
import os
import re

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
def cloth(enviro,response):
    print("cloth page")
    response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return '<h2>welcome to see cloth!!!</h2>'

def shoes(enviro,response):
    print("shoes page")
    response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    data = """
    <h1> here are the one of pictures of our shoes <h1>
         <img src='/static/shoes01.jpeg' />
    <p>more will coming soon ! </p>
    '''     
    """
    return data

def url_distribute():

    urls = {
        '/cloth': cloth,
        '/shoes': shoes,
    }
    return urls
def get_Image(request):
    """
    :param request: /static/images/shoes01.jpeg
    :return:
    """
    print (request)
    print ("------------------")
    img_path=re.sub('/static','/static_data',request)
    img_abs_path="%s%s" %(BASE_DIR,img_path)
    print ("base:  ",BASE_DIR)
    print (img_abs_path)

    if(os.path.isfile(img_abs_path)):
        print("eeeeexist-----")
        f=open(img_abs_path,"rb")
        f_data=f.read()
        return[f_data,0]
    return [None,1]
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
    elif request_url.startswith("/static/"):
        img_data,img_status= get_Image(request_url)
        if img_status==0:
            response("200 OK", [('Content-Type', 'text/jpeg;charset=utf-8')])
            return [img_data,]

    else:
        response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
        return '<h1 style="font-size:50px">404,Page not found! </h1>'


# response("200 OK",[('Content-Type','text/html;charset=utf-8')])
   # return '<h2>dasdasfasfdaf</h2>'

s=make_server('localhost',8003,run_server)
s.serve_forever()