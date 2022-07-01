import requests
from bs4 import BeautifulSoup

session = requests.Session()
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
BCA_EBANKING_URL = "https://ibank.klikbca.com"

USERID = "TEST123"
PWD = "STRING"

headers = {
    "User-Agent": USER_AGENT
}
req = session.get(BCA_EBANKING_URL, headers=headers, verify=False)
soup = BeautifulSoup(req.text, "html.parser")

form = soup.find_all("form")
for i in form:
    user_id = i.find(id="user_id")
    password = i.find(id="pswd")

