from binance.exceptions import BinanceAPIException
from binance.client import Client
#TESTNET

#API_KEY='7gr7eBfTq9IqaexFkjRVje17t8dTLjE30fck2oVucTURRqOqlYULW8xnKh8rMiZR'
#SECRET_KEY='Ai6F7MpVZvHQBHC0Yb07Djs5I2bmjUqsRVgssjPn3UzcviVn8VbSg5L3ZiC3pYjM'

#ORIGINAL

API_KEY = 'QSOAqPicgAdGuxFrUX3fRyliUKwZvMZz5W2vmozNIZrxUu4hUw5FIRkv1G2TO4F2'
SECRET_KEY = 'vYvmMCee2XSKd5o4asykDoB8lR93XCSvAYYWRjA9Fk4tF0mOtEByijNEMX3TVyCl'

client = Client(api_key=API_KEY,api_secret=SECRET_KEY,)


balance = client.get_account()['balances']
balance=[i for i in balance if i.get('asset')=='USDT'] 
