import requests

url = 'https://classroom.powerschool.com/'

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

if website_is_up == False:
    print('No')

if website_is_up == True:
    print('Yes')
