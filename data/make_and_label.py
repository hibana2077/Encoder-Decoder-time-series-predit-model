'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-05-16 20:52:55
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-05-16 23:12:29
FilePath: /Encoder-Decoder-time-series-predit-model/data/make_and_label.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
# import modin.pandas as pd
from ccxt import binanceusdm
from warnings import filterwarnings
import numpy as np
import logging
import argparse

filterwarnings('ignore')

# Get arguments
args = argparse.ArgumentParser()
args.add_argument('--symbol', type=str, default='BTC/USDT')
args.add_argument('--timeframe', type=str, default='1h')
args.add_argument('--from_date', type=str, default='2024-01-01 00:00:00')
args.add_argument('--to_date', type=str, default='2024-01-31 00:00:00')
args = args.parse_args()

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up ccxt
exchange = binanceusdm({})

if __name__ == '__main__':
    # using while loop to get all data
    symbol:str = args.symbol
    timeframe:str = args.timeframe
    from_date:str = args.from_date
    to_date:str = args.to_date
    since = exchange.parse8601(from_date)
    limit = 500
    data = pd.DataFrame()
    while since < exchange.parse8601(to_date):
        logger.info(f'Fetching data from {exchange.iso8601(since)} to {exchange.iso8601(since + limit * 60 * 1000)}')
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
        data = pd.concat([data, pd.DataFrame(ohlcv)])
        since = ohlcv[-1][0] + 1
    data.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    data.set_index('timestamp', inplace=True)
    data.to_csv(f'{symbol.replace("/", "_")}_{timeframe}.csv')
    logger.info(f'Saved data to data/{symbol.replace("/", "_")}_{timeframe}.csv')