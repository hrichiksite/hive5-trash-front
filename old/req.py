import requests

#todo change url to your server url
url = 'http://3.108.5.205:5000/infer'

def upload_file():
    with open('trash.jpg', 'rb') as f:
        r = requests.post(url, files={'file': f})
        json = r.json()
    return json

