import random
import time
from my_strategy import MySmaStrategy

class MockBacktestEnv:
    def __init__(self, symbol):
        self.symbol = symbol
        self.strategy = MySmaStrategy()

    def run(self):
        self.strategy.start(self)

    def start(self, evtHandler):
        # Simulate 50 ticks of price data
        for i in range(50):
            mock_price = 100 + random.uniform(-5, 5)  # Simulated price around 100
            md = {
                'symbol': self.symbol,
                'lastPrice': mock_price
            }

            ab = self.MockAlgoBridge()
            evtHandler.on_marketdatafeed(md, ab)
            time.sleep(0.1)  # Simulate time gap

    class MockAlgoBridge:
        def placeOrder(self, symbol, action, qty):
            print(f"[ORDER] {action} {qty} shares of {symbol}")

if __name__ == "__main__":
    backtest = MockBacktestEnv(symbol="AAPL")
    backtest.run()
