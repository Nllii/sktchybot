import requests
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']



def vote_image(img_id):

    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'imgID': f'{img_id}',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],

    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/vote', headers=headers, cookies=cookies, data=data)
    pprint.pprint(response.json())
    return response.json()






def unvote(img_id):
    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'imgID': f'{img_id}',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/unvote', headers=headers, cookies=cookies, data=data)
    pprint.pprint(response.json())




