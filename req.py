import requests

#todo change url to your server url
url = 'https://hrichiksite-improved-pancake-x45rgq5jjrc99r7-5000.preview.app.github.dev/infer'

def upload_file():
    with open('trash.jpg', 'rb') as f:
        r = requests.post(url, files={'file': f})
        json = r.json()
    return json

