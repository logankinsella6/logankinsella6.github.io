import requests
import webbrowser

url = 'google.com'
pDownY = 'Yes.'
pDown = 'Powerschool is down.'
pDownN = 'No.'
pDownZ = 'Powerschool is running'

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

if website_is_up == False:
    html_content = f"<html> <head> </head> {pDownY} <body> <h1> </h1><p> {pDown} </p> </body> </html>"
    with open("index.html", "w") as html_file:
        html_file.write(html_content)
if website_is_up == True:
    html_content = f"<html> <head> </head> {pDownN} <body> <p> {pDownZ} </p> </body> </html>"
    with open("index.html", "w") as html_file:
        html_file.write(html_content)
