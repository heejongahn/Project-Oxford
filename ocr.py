import requests, json

headers = {
    'Ocp-Apim-Subscription-Key': your-subsciption-key,
    'Content-Type': 'application/json',
        }

r = requests.post('https://api.projectoxford.ai/vision/v1/ocr',
        json = {"Url": your-img-url}, headers = headers)

print (r.text)
