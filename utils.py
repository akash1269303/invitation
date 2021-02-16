import requests

import requests
import json

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"O4SZedCcyOvA9AsJAVHwF1LZJptJmUdgPWzIJByqBdIPKFcb87X2kRTDuwli",
    "sender_id": "FSTSMS",
    "message":message,
    "language":"english",
    "route":"q",
    "numbers":contactno}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = response.text
    d1 = json.loads(json_data)

    return d1['return']