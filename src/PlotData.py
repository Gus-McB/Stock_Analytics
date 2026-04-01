import pandas as pd
from abc import ABC, abstractmethod
import mplfinance as mpf
import matplotlib.pyplot as plt

class PlotData:
    def plotClosingPrice(self, df, ticker, timeframe, title, xlabel, ylabel):
        plt.figure(figsize=(10, 6))
        plt.grid(alpha=0.5)
        plt.plot(
            df.xs(ticker).index,
            df.xs(ticker)['Close'],
            color='blue',
            linewidth=1.5
        )
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plotVolume(self, df, ticker, timeframe, title, xlabel, ylabel):
        pass

    def plotCandle(self, df, ticker, timeframe, title, xlabel, ylabel):
        mpf.plot(
            df.xs(ticker),
            type='candle',
            style='charles',
            title=title,
            figsize=(14, 7),
            volume=True,
        )

    def plotMAV(self, df, ticker, timeframe, title, xlabel, ylabel):
        pass

    def plotOHLCV(self, df, ticker, timeframe, title, xlabel, ylabel):
        df_latest = df.head(30)

        mpf.plot(
            df_latest.xs(ticker),
            type='candle',
            style='charles',
            title=title,
            figsize=(14, 7),
            volume=True,
        )