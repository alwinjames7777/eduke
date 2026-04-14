import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/login/'
session = requests.Session()

# 1. Get CSRF token from login
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', dict(name='csrfmiddlewaretoken'))['value']

# 2. Login as admin
login_data = {
    'csrfmiddlewaretoken': csrf_token,
    'email': 'alwin@gmail.com',  # We know this from git log author, wait, let me just check the db
    'password': '1'  # I don't know the password... oops
}
