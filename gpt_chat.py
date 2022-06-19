import requests

# GPT2.
def generate_text(get_text):

    cookies = {
    }

    json_data = {
        'user_k': '102',
        'user_temp': '1.3371478095650673',
        'key': 'lkjsdf923oihj987asdiohfq98234',
        'user_p': '1.0',
        'text': f'<Dwelling Human>:"{get_text}" \n<Wise Dalai Lama>:"{get_text} "\n<Dwelling Human>:  "{get_text}"',
    }

    response = requests.post('https://zazyzazy.asuscomm.com/generate', cookies=cookies, json=json_data)
    return response.json()['result']

    # pprint.pprint(response.json())
