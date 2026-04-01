import yfinance as yf
from src.DataCleaner import YFinanceCleaner
from src.PlotData import PlotData

if __name__ == "__main__":
    df_AAPL = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
    df_TSLA = yf.download("TSLA", start="2020-01-01", end="2021-01-01")
    cleaner = YFinanceCleaner()
    df_AAPL = cleaner.restructure(df_AAPL)
    df_TSLA = cleaner.restructure(df_TSLA)
    df_AAPL = cleaner.clean(df_AAPL)
    df_TSLA = cleaner.clean(df_TSLA)
    plot = PlotData()
    data_AAPL = {
        "df": df_AAPL,
        "timeframe": "1d",
        "ticker": "AAPL",
        "title": "AAPL Closing Price",
        "xlabel": "Date",
        "ylabel": "Price"
    }

    data_TSLA = {
        "df": df_TSLA,
        "timeframe": "1d",
        "ticker": "TSLA",
        "title": "TSLA Closing Price",
        "xlabel": "Date",
        "ylabel": "Price"
    }

    plot.compareClosingPrice(data_AAPL, data_TSLA, title='AAPL vs TSLA - Normalised Closing Price')