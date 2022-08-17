# Import Libraries
import requests
import pandas as pd

# Import Keys
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
SEND_ID = os.environ['SEND_ID']

reflections = pd.read_csv('reflections.tsv', delimiter='\t', index_col=False, header=None)

TOKEN = TELEGRAM_TOKEN
CHAT_ID = SEND_ID
message = reflections.sample()
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
print(requests.get(url).json()) # this sends the message
