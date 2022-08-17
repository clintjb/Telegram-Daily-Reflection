# Import Libraries
import requests
import random

# Import Keys
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
SEND_ID = os.environ['SEND_ID']

reflections = open('reflections2.tsv').read().splitlines()

TOKEN = TELEGRAM_TOKEN
CHAT_ID = SEND_ID
message = random.choice(lines)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
print(requests.get(url).json()) # this sends the message
