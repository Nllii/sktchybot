import requests
import siaskynet as skynet
import openai
from pathlib import Path
import toml 


credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']

OPEN_AI_KEY = id_['OPEN_AI_KEY']
chooch_api_key = id_['chooch_api_key']



def openai_gpt(description = None,notification_reply = None):
    if notification_reply != None:
        openai.api_key = OPEN_AI_KEY
        response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=f"Respond\"{notification_reply}\"\n",
        # prompt=f"say something nice \"{description}\"\n",
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text
    else:
        openai.api_key = OPEN_AI_KEY
        response = openai.Completion.create(
        engine="text-babbage-001",
        # prompt=f"Respond\"{description}\"\n",
        prompt=f"say something nice \"{description}\"\n",
        temperature=0.7,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return response.choices[0].text
    


def chooch_api(file_name):
    url = f'https://api.chooch.ai/predict/image?apikey={chooch_api_key}'
    files = {'image': open(f'/Users/admin/sktchyBot/art_images/{file_name}', 'rb')}
    response = requests.post(url, files=files)
    join_sentences  = []            
    for summary in response.json()['predictions']:
        try:
            title_ = summary['class_title']
            object_ = summary['parent_object']
            join_sentences.append(title_ + " " + object_)
        except:
            continue
    # print(join_sentences)
    return join_sentences




def describe_artwork(_id):
    cookies = {

    }
    headers = {
    }
    response = requests.get(f'https://1fb6311c87ad3bea9c8c-c9a53b3ad860ce74916099727efb31e7.ssl.cf2.rackcdn.com/{_id}_t@2x.jpg', headers=headers, cookies=cookies)
    file_name = response.url.split("?")[0].split("/")[-1]
    with open(f'/Users/admin/sktchyBot/art_images/{file_name}', 'wb') as f:
        f.write(response.content)
    return file_name
    

# artwork_id = describe_artwork(_id = "622b7cc37ca60a76e3726b25")
# sentences = chooch_api(file_name= artwork_id)
# gpt3_response = openai_gpt(description = sentences)
# print(gpt3_response)










# def upload_data(data):
#     client = skynet.SkynetClient()
#     skylink_url = client.upload_file(data)
#     print("Upload successful, skylink: " + skylink_url)
#     change_sia_to_https = skylink_url
#     change_sia_to_https = change_sia_to_https.replace("sia://","https://siasky.net/")
#     save_newurl = change_sia_to_https
#     return save_newurl



# def describe_artwork():
#     id_ = "622815b37ca60a678647241e"
#     file_name = get_image(id_)
#     response_ = chooch_api(file_name)







#     # save json file to local
#     with open('/Users/admin/sktchyBot/chooch_api.json', 'w') as f:
#         f.write(response_.text)
#     # upload json file to skynet
#     save_newurl = upload_data('/Users/admin/sktchyBot/chooch_api.json')




    



# describe_artwork()
