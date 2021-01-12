import requests
import webbrowser

url = 'google.com'

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

if website_is_up == False:
    html_content = "<html> <head> </head> <h2> Yes. </h2> <body> <p> Powerschool is down! </p> </body> </html>"

if website_is_up == True:
    html_content = "<html> <head> </head> <h2> No. </h2> <body> <p> Poweschool is up! </p> </body> </html>"

outfile = ("index.html", "w")
outfile.write(html_content)
outfile.close()
