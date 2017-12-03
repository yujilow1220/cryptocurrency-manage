import os
import requests
from poloniex import Poloniex
polo = Poloniex(Key=os.environ.get('POLO_API_KEY'),
                Secret=os.environ.get('POLO_API_SECRET'),
                coach=True)
class Order(object):
    def __init__(self):
        pass

    def buy(self, currency=None, amount=None, price=None):
        if currency == None or amount == None or price == None:
            return

    def sell(self, currency="BTC", amount=0.0, price=0.0):
        pass

class History(object):
    def __init__(self):
        his = polo.returnDepositsWithdrawals()
        self._deposits = his['deposits']
        self._withdrawals = his['withdrawals']
        
    def deposits(self, currency="BTC"):
        return [item for item in self._deposits if item['currency'] == currency]

    def total_deposits(self, currency="BTC"):
        total = 0.0
        for item in self.deposits(currency):
            total += float(item["amount"])
        return total
    
    def yield_by(self, by="year"):
        pass

class Balance(object):
    def __init__(self):
        self.update()

    def update(self):
        self._balance = {key:float(value) for key,value in polo.returnBalances().items() if float(value) > 0}
        self._rates = polo.returnTicker()
        self._btc_jpy = float(requests.get('https://coincheck.com/api/rate/btc_jpy').json()['rate'])

    def get(self):
        return self._balance

    def jpy(self):
        return self._balance_to_jpy()

    def total(self):
        jpy = 0.0
        for value in self.jpy().values():
            jpy += value
        return jpy

    def history(self, history_type="deposits"):
        return polo.returnDepositsWithdrawals()[history_type]

    def _balance_to_jpy(self):
        btc_jpy = self._btc_jpy
        balance = self.get()
        rates = self._rates
        results = {}
        for key, val in balance.items():
            if key == "BTC":
                jpy = val * btc_jpy
            else:
                jpy = (float(rates.get("BTC_%s" % key)['last']) * val) * btc_jpy
            results.update({key: round(jpy)})
        return results

    def _get_btc_jpy(self):
        return self._btc_jpy

