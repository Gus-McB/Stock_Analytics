import yfinance as yf
from src.DataCleaner import YFinanceCleaner
from src.PlotData import PlotData

if __name__ == "__main__":
    df = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
    cleaner = YFinanceCleaner()
    df = cleaner.restructure(df)
    df = cleaner.clean(df)
    plot = PlotData()
    data = {
        "df": df,
        "timeframe": "1d",
        "ticker": "AAPL",
        "title": "AAPL Closing Price",
        "xlabel": "Date",
        "ylabel": "Price"
    }

    plot.plotCandle(**data)