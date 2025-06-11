import io

import requests
from pprint import pprint
import json
from PIL import Image
from post_pydantic import post_pyd
import urllib3 , ijson
from post import post

def doJob():
    print(requests.__version__)
    uri = 'http://universities.hipolabs.com/search?country=India'
    r_get = requests.get(uri)
    print(f' status = {r_get.status_code}')
    pprint(r_get.headers)
    # leveraging ijson to do stream processing w/o overloading the memory all at once
    for institute in ijson.items(io.StringIO(r_get.text),'item'):
        print(institute)

    #pprint(json.loads(r_get.text)) # will get response as string, so use json.loads to get a dict out of it (or) any other python obj using a objecthook
    #print(r_get.json()) # gets response as json directly. no need to do the json.loads conversion
    user_uri = 'https://jsonplaceholder.typicode.com/users/1'
    user_r_get = requests.get(user_uri)
    pprint(user_r_get.json()['address']['geo'])
    # doing a request with query params
    post_uri = 'https://jsonplaceholder.typicode.com/comments'
    post_params = {'postId':1}
    post_resp = requests.get(url=post_uri,params=post_params)
    print(post_resp.json())

def doPostJob():
    p_uri = 'https://jsonplaceholder.typicode.com/posts/'
    p_data = {
        'userId': 223,
        'id': 1,
        'title': 'my first post',
        'body': 'this is my first post from python code using the urllib3 pkg'
    }
    # can pass dict directly , no need to do json.dumps
    p_res = requests.post(url=p_uri,data=p_data)
    print(p_res.status_code)


def doPostJob_withJson_param():
    p_uri = 'https://jsonplaceholder.typicode.com/posts/'
    p_data = post(userId=242,id=1,title='json post',body='post from python using object that returns json')
    # same as previous example, but i use the json parameter instead of data. underlying info in both is the same though
    p_res = requests.post(url=p_uri,json=p_data.to_dict())
    print(p_res.status_code)

def doPost_with_toDict():
    p_uri = 'https://jsonplaceholder.typicode.com/posts/'
    p_obj = post(userId=142,id=1,title='starting post',body='testing post using class toDict method')
    # using PoolManager of urllib3
    http = urllib3.PoolManager()
    # using a custom toDict() in the class that returns a dict
    # process dict to string using json.dumps and then do utf-8 encoding to get the bytes equivalent
    p_res = http.request(url=p_uri,body=json.dumps(p_obj.to_dict()).encode('utf-8'),method='POST')
    print(p_res.status)

def doPost_with_pyd():
    p_uri = 'https://jsonplaceholder.typicode.com/posts/'
    p_obj = post_pyd(userID=234,id=1,title='pydantic post',body='this is a post using pydantic for schema validation and type hints')
    # using PoolManager of urllib3
    http = urllib3.PoolManager()
    # using pydantic provided json() on the object
    # no need to do a json.dumps(), as i get a stringified json, but  must perform an encode to get the byte equivalent
    p_res = http.request(method='POST',url=p_uri,body=p_obj.model_dump_json().encode('utf-8'))
    # post_pyd.model_validate_json(p_res.json()) # to deserialize the response to pydantic model
    print(p_res.status)

def do_Head_Request():
    h_uri = 'http://example.com'
    # using PoolManager of urllib3
    http = urllib3.PoolManager()
    h_res = http.request(method='HEAD',url=h_uri)
    print(h_res.headers)

def do_put_request():
    # using pydantic
    p_uri = 'https://jsonplaceholder.typicode.com/posts/100'
    p_obj = post_pyd(userID=456,id=1,title='updated post',body='post has been updated in full using put request')
    # requests lib instead of poolManager
    headers = {'c_header':'1'}
    p_res = requests.put(url=p_uri,data=p_obj.model_dump(),headers=headers)
    print(p_res.json())

def do_patch_request():
    # using pydantic
    p_uri = 'https://jsonplaceholder.typicode.com/posts/100'
    p_data = {'body': 'the content modified using patch'}
    http = urllib3.PoolManager()
    res = http.request(method='PATCH',url=p_uri,body=json.dumps(p_data).encode('utf-8'))
    print(res.data.decode('utf-8')) # or simply do res.json() as res.data returns bytes which requires utf-8 decoding explicitly

def do_image_download():
    img_uri = 'https://download.logo.wine/logo/World_Bank/World_Bank-Logo.wine.png'
    try:
        img_res = requests.get(url=img_uri)
        img_res.raise_for_status() # auto raise exceptions
        c_type = img_res.headers.get('content-type').lower()
        if 'image' in c_type:
            img_data = io.BytesIO(img_res.content) # store as bytes IO
            img = Image.open(img_data) # open from bytes IO and store in Image obj. can also directly open from img_res.content
            img.save(fp='tf.png') # save to file . can also save to buffer
    except requests.exceptions.RequestException as e:
        print(f'sorry , errored out with {e}')

def do_image_manipulation():
    try:
        with open('tf.png',mode='rb') as f:
            img_org = Image.open(f) # open from file pointer
            img_org = img_org.resize((100,100)) # resiZing
            buffer = io.BytesIO() # placeholder to write to file
            img_org.save(buffer,format='PNG') # save modified img in buffer
            with open('gf.png',mode='wb') as wf:
                wf.write(buffer.getvalue()) # write the buffer content
    except Exception as e:
        print(f'sorry, some error occured with {e}')

def create_Schema():
    print('the schema of the post_pd api')
    print(post_pyd.model_json_schema())

def do_redirects():
    get_uri = 'https://gmail.com'
    try:
        res_get = requests.get(url=get_uri) # to stop redirects , use allowRedirect = false . for get , its true by default
        # if you want to specify conn timeout and read timeout of resp, use the foll
        # res_get = requests.get(url=get_uri,timeout=(5,10)) # setting timeout = None will effectively wait forever, if only one value is set then conn and read timeout are same
        res_get.raise_for_status()
        # checking for redirects if any
        if res_get.history:
            for res in res_get.history:
                print(res.status_code, res.is_redirect , res.url)
    except requests.exceptions.RequestException as e:
        print('request errored')

if __name__ == '__main__':
    doJob()
    doPostJob()
    doPost_with_toDict()
    doPost_with_pyd()
    do_Head_Request()
    doPostJob_withJson_param()
    do_put_request()
    do_patch_request()
    do_image_download()
    do_image_manipulation()
    create_Schema()
    do_redirects()