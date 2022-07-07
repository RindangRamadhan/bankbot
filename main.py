import os

from dotenv import load_dotenv

from klikbca import KlikBcaScraper

load_dotenv()

USERID = os.environ.get("user_id")
PASSWORD = os.environ.get("password")

bca = KlikBcaScraper(user_id=USERID, user_password=PASSWORD)
print(bca.login())
