import requests
import pprint

from pathlib import Path
import toml 


credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']



def userIds():
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
    'pp': '50',
    't': '2',
    'zip': '1'
    }

    response = requests.post('https://api.sktchy.com/api/v1/graph/home', headers=headers, cookies=cookies, data=data)
    posted_content = response.json()['graph/home']
    # print(posted_content)
    home_feed  = []
    for post in posted_content:
        # pprint.pprint(post)
        try:
            _id = post['_id']
            _name = post['meta']['bya']
            _by = post['meta']['by']
            _message = post['meta']['h']
            _userID = post['usrID']
            if 'h' in post['meta']:
                json_ = {

                    'userID': _userID,
                    '_id': _id,
                    '_name': _name,
                    '_by': _by,
                    '_message': _message
                }

                home_feed.append(json_)
            else:
                pass
        except:
            json_ = {
                
                    'userID': _userID,
                    '_id': _id,
                    '_name': _name,
                    '_by': _by,
                    '_message': 'nice'
                }
            home_feed.append(json_)
            continue
    return home_feed

