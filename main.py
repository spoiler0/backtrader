import backtrader as bt

from data import CustomCSVData
from strategy import PrintClose


# Instantiate Cerebro engine
cerebro = bt.Cerebro()

data = CustomCSVData(
    dataname="Binance_BTCUSDT_minute_reversed.csv",
    timeframe=bt.TimeFrame.Minutes,
    reversed=True,
    headers=True,
    datetime=1,
    open=3,
    high=4,
    low=5,
    close=6,
    volume=7,
    dtformat=("%Y-%m-%d"),
    tmformat=("%H:%M:%S"),
)

cerebro.adddata(data)

# Add strategy to Cerebro
cerebro.addstrategy(PrintClose)

# Run Cerebro Engine
cerebro.run()
