from coincheck import order, market, account
import os

coincheck_access_key = os.environ.get('COINCHECK_ACCESS_KEY')
coincheck_secret_key = os.environ.get('COINCHECK_SECRET_KEY')

def buy_market(amount_jpy):
   o = order.Order(secret_key=coincheck_secret_key, access_key=coincheck_access_key)
   return o.buy_btc_jpy_market(amount=amount_jpy, rate=0)

def history():
    o = order.Order(secret_key=coincheck_secret_key, access_key=coincheck_access_key)
    return o.history()

print(buy_market(100))
