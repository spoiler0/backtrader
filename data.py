import backtrader as bt
from datetime import date, time, datetime
from backtrader.utils import date2num


class CustomCSVData(bt.CSVDataBase):
    params = (
        ("open", 3),
        ("high", 4),
        ("low", 5),
        ("close", 6),
        ("volume", 7),
    )

    def start(self):
        super(CustomCSVData, self).start()

    def stop(self):
        super(CustomCSVData, self).stop()

    def _loadline(self, linetokens):
        # For Binance_BTCUSDT_minute.csv
        # [unixtime, date time, symbol, open, high, low, close, VolumeBTC, VolumeUSDT, tradecount]

        year, month, day, hour, minute, second = linetokens[1].replace("-", " ").replace(":", " ").split(" ")
        row_date = date(int(year), int(month), int(day))
        row_time = time(int(hour), int(minute), int(second))
        self.lines.datetime[0] = date2num(datetime.combine(row_date, row_time))
        self.lines.open[0] = float(linetokens[self.params.open])
        self.lines.high[0] = float(linetokens[self.params.high])
        self.lines.low[0] = float(linetokens[self.params.low])
        self.lines.close[0] = float(linetokens[self.params.close])
        self.lines.volume[0] = float(linetokens[self.params.volume])

        return True