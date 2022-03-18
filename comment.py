import requests
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']
# 'inEmail':id_['inEmail'],
# 'inPass': id_['inPass'],



def comment_(reply,img_id):
    
    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'h': '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<title></title>\n<meta name="Generator" content="Cocoa HTML Writer">\n<style type="text/css">\np.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 14.0px \'.AppleSystemUIFont\'; color: #545454}\nspan.s1 {font-family: \'.SFUI-Regular\'; font-weight: normal; font-style: normal; font-size: 14.00px}\n</style>\n</head>\n<body>\n<p class="p1"><span class="s1">'+reply+ "       - comment by a bot."+ '.<span class="Apple-converted-space">\xA0</span></span></p>\n</body>\n</html>\n',
    'imgID': f'{img_id}',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/addrichcomment', headers=headers, cookies=cookies, data=data)
    pprint.pprint(response.json())
    return response.json()




def account_comment():
    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'iID': id_['iID'],
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'sort': '1',
    't': '4',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/filtered', headers=headers, cookies=cookies, data=data)
    # pprint.pprint(response.json())




def delete_comment(id):

    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'id': f'{id}',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/delete/comment', headers=headers, cookies=cookies, data=data)
    pprint.pprint(response.json())




def reply_comment(message,imgID,userID,name):
    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'h': '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<title></title>\n<meta name="Generator" content="Cocoa HTML Writer">\n<style type="text/css">\np.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 14.0px \'.AppleSystemUIFont\'; color: #545454}\nspan.s1 {font-family: \'.SFUI-Regular\'; font-weight: normal; font-style: normal; font-size: 14.00px}\n</style>\n</head>\n<body>\n<p class="p1"><span class="s1"><a href="sktchy://user/'+userID+'">'+name+'</a> '+message+'</span></p>\n</body>\n</html>\n',
    'imgID': f'{imgID}',

    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],

    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/addrichcomment', headers=headers, cookies=cookies, data=data)
    pprint.pprint(response.json())




# reply_comment(message = "hello_world",imgID = "622f81a47ca60a0b786496e1",userID = "56ed09bf0a5373ab06cc7a13")
