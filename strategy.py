import backtrader as bt


class PrintClose(bt.Strategy):
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def log(self, txt, date=None, time=None):
        date = date or self.datas[0].datetime.date(0)
        time = time or self.datas[0].datetime.time(0)
        print(f"{date.isoformat()} {time.isoformat()} {txt}")  # Print date and close

    def next(self):
        self.log(f"Close: {self.dataclose[0]}")
