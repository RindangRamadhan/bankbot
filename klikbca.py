import requests
from bs4 import BeautifulSoup


class KlikBcaScraper:
    def __init__(self, user_id: str, user_password: str):
        self.session = requests.Session()

        self.login_url = "https://ibank.klikbca.com/authentication.do"
        self.logout_url = "https://ibank.klikbca.com/authentication.do?value(actions)=logout"
        self.account_balance_url = "https://ibank.klikbca.com/balanceinquiry.do"
        self.welcome_url = 'https://ibank.klikbca.com/authentication.do?value(actions)=welcome'

        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

        self.payloads = {
            'value(user_id)': user_id,
            'value(pswd)': user_password,
            'value(Submit)': 'LOGIN',
            'value(actions)': 'login',
            'value(user_ip)': "182.253.87.4",
            'value(mobile)': 'false',
            'value(browser_info)': self.user_agent,
        }

        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ibank.klikbca.com',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            "User-Agent": self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://ibank.klikbca.com/',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8'
        }

    def login(self):
        session = self.session
        session.post(url=self.login_url, headers=self.headers, data=self.payloads, verify=False)
        response = session.get(self.welcome_url)
        return response

    def parse_welcome_messages(self):
        res = self.login()
        soup = BeautifulSoup(res.content, 'html.parser')
        raw_welcome_message = soup.find("font", {
            "face": "Verdana, Arial, Helvetica, sans-serif", "size": 3
        }).text.replace("\n", "")
        welcome_message = " ".join(raw_welcome_message.split())
        return welcome_message
