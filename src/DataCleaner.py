import pandas as pd
from abc import ABC, abstractmethod

class DataCleaner(ABC):
    @abstractmethod
    def clean(self, df):
        pass

class YFinanceCleaner(DataCleaner):
    def clean(self, df):
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)
        df = df.dropna()
        df = df.drop_duplicates()
        df['Open'] = df['Open'].astype(float)
        df['High'] = df['High'].astype(float)
        df['Low'] = df['Low'].astype(float)
        df['Close'] = df['Close'].astype(float)
        df = df.sort_index()
        return df
    
    def restructure(self, df):
        df = df.stack(level="Ticker", future_stack=True)
        df.index.names = ["Date", "Symbol"]
        df = df[["Open", "High", "Low", "Close", "Volume"]]
        df = df.swaplevel(0, 1)
        df = df.sort_index()
        df

        return df