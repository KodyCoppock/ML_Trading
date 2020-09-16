import alpaca_backtrader_api as Alpaca
import pytz
from datetime import datetime
from local_settings import alpaca_paper

ALPACA_KEY_ID = alpaca_paper['api_key']
ALPACA_SECRET_KEY = alpaca_paper['api_secret']
ALPACA_PAPER = True
