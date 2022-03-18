import time
import requests
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']

# you will need to get the user id from the user_filtered function then call this function.
def profile(user_id):
    """
    # you will need to get the user id from the user_filtered function then call this function.

    """


    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'id_': f'{user_id}',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/profile/user', headers=headers, cookies=cookies, data=data)
    # pprint.pprint(response.json())





def user_filtered(usrID):
        
    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'pp': '20',
    't': '2',
    'usrID': f'{usrID}',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/filtered', headers=headers, cookies=cookies, data=data)
    return response.json()
    # pprint.pprint(response.json())
    # for ids in  response.json()['graph/filtered']:
    #     print(ids['_id'])
        # return ids['_id']
    
    # pprint.pprint(response.json())


def activity():

    cookies = {
    }

    headers = {
        'User-Agent': 'SktchyForiPhone/3.0.0 (iPhone; iOS 14.0; Scale/3.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'en-US;q=1',
    }

    data = {
    '_appv': '465',
    'inEmail':id_['inEmail'],
    'inPass': id_['inPass'],
    'lang': 'en-US',
    'pp': '20',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/activity/activities', headers=headers, cookies=cookies, data=data)
    return response.json()

    # pprint.pprint(response.json())



# activity()
