import requests

url = 'https://powerschool.com'

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200
