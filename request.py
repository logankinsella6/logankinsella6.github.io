import requests
import webbrowser
import dominate
from dominate.tags import *
url = 'google.com'

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

def create_page():
    doc = dominate.document(title='ispowerschooldown.com')

    with doc:
        with div(clas='containter'):
            h2('Hello, World')
    print(doc)
    
create_page()
