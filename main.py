import backtrader as bt

from data import CustomCSVData
from strategy import PrintClose, MAcrossover


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
cerebro.addstrategy(MAcrossover)

if __name__ == "__main__":
    # Run Cerebro Engine
    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f"Starting Portfolio Value: {start_portfolio_value:2f}")
    print(f"Final Portfolio Value: {end_portfolio_value:2f}")
    print(f"PnL: {pnl:.2f}")
