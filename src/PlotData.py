import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

class PlotData:
    STYLE = {
        'figsize': (12, 6),
        'figsize_large': (14, 7),
        'figsize_cross': (16, 10),
        'linewidth': 1.5,
        'grid_alpha': 0.5,
        'xticks_rotation': 45,
        'mpf_style': 'yahoo',
        'colors': ['blue', 'orange', 'green', 'red'],
    }

    def plotClosingPrice(self, df, ticker, timeframe, title, xlabel, ylabel):
        s = self.STYLE
        plt.figure(figsize=s['figsize'])
        plt.grid(alpha=s['grid_alpha'])
        plt.plot(
            df.xs(ticker).index,
            df.xs(ticker)['Close'],
            color=s['colors'][0],
            linewidth=s['linewidth']
        )
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=s['xticks_rotation'])
        plt.tight_layout()
        plt.show()

    def plotCandle(self, df, ticker, timeframe, title, xlabel, ylabel):
        s = self.STYLE
        mpf.plot(
            df.xs(ticker),
            type='candle',
            style=s['mpf_style'],
            title=title,
            figsize=s['figsize_large'],
            volume=True,
        )

    def plotMAV(self, df, ticker, timeframe, title, xlabel, ylabel):
        pass

    def plotOHLCV(self, df, ticker, timeframe, title, xlabel, ylabel):
        s = self.STYLE
        df_latest = df.head(30)

        mpf.plot(
            df_latest.xs(ticker),
            type='candle',
            style=s['mpf_style'],
            title=title,
            figsize=s['figsize_large'],
            volume=True,
        )

    def compareClosingPrice(self, df1, df2, title):
        s = self.STYLE
        ticker1 = df1['ticker']
        ticker2 = df2['ticker']
        close1 = df1['df'].xs(ticker1)['Close']
        close2 = df2['df'].xs(ticker2)['Close']

        norm1 = close1 / close1.iloc[0] * 100
        norm2 = close2.reindex(close1.index) / close2.iloc[0] * 100

        plt.figure(figsize=s['figsize'])
        plt.plot(norm1.index, norm1, label=ticker1, color=s['colors'][0], linewidth=s['linewidth'])
        plt.plot(norm2.index, norm2, label=ticker2, color=s['colors'][1], linewidth=s['linewidth'])
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Normalised Close (base 100)')
        plt.legend()
        plt.grid(alpha=s['grid_alpha'])
        plt.xticks(rotation=s['xticks_rotation'])
        plt.tight_layout()
        plt.show()

    def crossPlot(self, df1, df2, plot_type, ticker, title):
        s = self.STYLE
        df1_slice = df1['df'].xs(ticker)
        df2_slice = df2['df'].xs(df2['ticker'])

        fig = mpf.figure(style=s['mpf_style'], figsize=s['figsize_cross'])
        fig.suptitle(title, fontsize=14)

        ax1 = fig.add_subplot(2, 2, 1)
        av1 = fig.add_subplot(2, 2, 3, sharex=ax1)
        ax2 = fig.add_subplot(2, 2, 2)
        av2 = fig.add_subplot(2, 2, 4, sharex=ax2)

        mpf.plot(df1_slice, type=plot_type, ax=ax1, volume=av1)
        mpf.plot(df2_slice, type=plot_type, ax=ax2, volume=av2)
        mpf.make_mpf_style(base_mpf_style=s['mpf_style'], rc={'axes.grid': True})

        ax1.set_title(ticker)
        ax2.set_title(df2['ticker'])

        mpf.show()