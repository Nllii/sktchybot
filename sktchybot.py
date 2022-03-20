import vote
import home
import describe_image
import requests
import comment
import time
import database
import threading
import user
import re
import toml 
from pathlib import Path

# get the path to the credentials file and read it using toml 
# credentials_path = Path(os.path.dirname(os.path.realpath(__file__)) + "/credentials.toml")
# credentials = toml.load(credentials_path)

credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']




def sktchyBot(account_activity):
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
    if not account_activity.is_set():
        # call f() again in 60 seconds
        threading.Timer(100, sktchyBot, [account_activity]).start()
        posted_content = response.json()['graph/filtered']
        for post in posted_content:
            try:
                _message = post['meta']['h']
                if _message == '!star_all':
                    _idusrID = post['usrID']
                    _id = user.user_filtered(_idusrID)
                    for ids in  _id['graph/filtered']:
                        response = vote.vote_image(ids['_id'])
                        print(response)
                    comment.delete_comment(post['_id'])
                
                if _message == '!remove_stars':
                    _idusrID = post['usrID']
                    _id = user.user_filtered(_idusrID)
                    for ids in  _id['graph/filtered']:
                        response = vote.unvote(img_id=ids['_id'])
                        print(response)
                    comment.delete_comment(post['_id'])

                print(_message)
            except Exception as e:
                print(e)
                continue


account_activity = threading.Event()
sktchyBot(account_activity)




def get_notifications(notifications):
    if not notifications.is_set():
        print("i got called")
        threading.Timer(200, get_notifications, [notifications]).start()
        msg = user.activity()
        for messages in msg['activity/activities']: 
            try:
                database.save_history().previous_notifications.insert_one({"previous_messages": messages})
                print("new notification found")
                _name = re.search(r'(?<=class="usr1">).+?(?=</a>)', messages['msg']).group(0)
                _message = re.search(r'(?<=</a>).*', messages['msg']).group(0)
                _image_id = messages['item']['id']
                _user_id = messages['user']['id']
                # print(_user_id,_name,_message,_image_id)
                if "commented on your inspiration:" in _message:
                    gpt3_response = describe_image.openai_gpt(notification_reply = _message)
                    comment.reply_comment(message = gpt3_response,imgID = _image_id,userID = _user_id,name = _name)
                    # break
                if "commented on your art:" in _message:
                    gpt3_response = describe_image.openai_gpt(notification_reply = _message)
                    comment.reply_comment(message = gpt3_response,imgID = _image_id,userID = _user_id,name = _name)
                    # print(gpt3_response)
                if "mentioned you:" in _message:
                    gpt3_response = describe_image.openai_gpt(notification_reply = _message)
                    comment.reply_comment(message = gpt3_response,imgID = _image_id,userID = _user_id,name = _name)
            except Exception as e:
                print("no new notifications")
                continue

            
            # if messages['_id'] not in previous_message:
            #     pass
            # else:


notifications = threading.Event()
get_notifications(notifications)





def interact_home(landing_page):
    if not landing_page.is_set():
        threading.Timer(300, interact_home, [landing_page]).start()
        for ids in home.userIds():
            print(ids)
            try:
                database.save_history().homeIds.insert_one({"postids": ids['_id']})
                if "5555b3110a5373520990b849" in ids['userID']:
                    vote_art = vote.vote_image(img_id = ids['_id'])
                else:
                    # artwork_id = describe_image.describe_artwork(_id =ids['_id'])
                    # sentences = describe_image.chooch_api(file_name= artwork_id)
                    # gpt3_response = describe_image.openai_gpt(description = sentences)
                    # leave_comment = comment.comment_(reply= gpt3_response,img_id = ids['_id'])
                    vote_art = vote.vote_image(img_id = ids['_id'])


                time.sleep(1)
            except Exception as e:
                print("no new post")
                # print(e)
                continue
        

landing_page = threading.Event()
interact_home(landing_page)
