from AlgoAPI import AlgoAPIUtil, AlgoAPI_Backtest

class MySmaStrategy:
    def __init__(self):
        self.prices = []
        self.short_window = 5
        self.long_window = 20
        self.position = 0  # 0 = flat, 1 = long

    def start(self, mEvt):
        self.evt = AlgoAPI_Backtest.AlgoEvtHandler(self, mEvt)
        self.evt.start()

    def on_marketdatafeed(self, md, ab):
        symbol = md['symbol']
        price = md['lastPrice']
        self.prices.append(price)

        if len(self.prices) < self.long_window:
            return  # Not enough data yet

        short_ma = sum(self.prices[-self.short_window:]) / self.short_window
        long_ma = sum(self.prices[-self.long_window:]) / self.long_window

        if short_ma > long_ma and self.position == 0:
            ab.placeOrder(symbol, "BUY", 100)
            self.position = 1
            print(f"BUY triggered at {price}")

        elif short_ma < long_ma and self.position == 1:
            ab.placeOrder(symbol, "SELL", 100)
            self.position = 0
            print(f"SELL triggered at {price}")
