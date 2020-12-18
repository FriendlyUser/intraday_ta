import yfinance as yf
import matplotlib
import matplotlib.pyplot as plt
import pandas
import pandas_ta
from datetime import date
yf.pdr_override()
from darts import TimeSeries

from darts.models import (
    NaiveSeasonal,
    NaiveDrift,
    Prophet,
    ExponentialSmoothing,
    ARIMA,
    AutoARIMA,
    StandardRegressionModel,
    Theta,
    FFT
)


def get_prices(stock, start_date="2019-03-03", end_date=str(date.today())):
    data = yf.download(stock, start=start_date, end=end_date,
                      group_by="ticker")
    data = data.fillna(method='bfill')
    # Drop columns with no entries
    data = data.dropna(axis='columns', how='all')

    # prices_df = pd.concat([data[ticker]["Close"] for ticker in stocks], axis=1)
    # prices_df.columns = stocks
    return data

# return df and column names of interest
def get_prices_rsi(stock, start_date="2019-03-03", end_date=str(date.today())):
    data = get_prices(stock, start_date="2019-03-03", end_date="2020-12-14")
    data.ta.bbands(length=20, append=True)
    return data


def plot_predictions(ticker: str, predict_range: float = 10, models: list = None, model_labels: list = None):
    """
        ticker - yahoo finance ticker
        ax - matplotlib ax to be passed to darts.plot -> pandas.plot
        models - List of models to pass in
    """
    # Get a more complicated method
    plt.figure()
    ax = plt.gca()
    if models == None:
        models = [NaiveSeasonal(6), NaiveSeasonal(12), NaiveDrift()]
    if model_labels == None:
        model_labels = ['Naive Seasonal (6)', 'Naive Seasonal (12)', 'Drift']
    asset_prices = get_prices(ticker)
    asset_prices['Date'] = asset_prices.index
    series = TimeSeries.from_dataframe(asset_prices, 'Date', ['Close'],  'B')
    series.plot(label='actual', ax=ax)
    # run through models and predict results
    for index, m in enumerate(models):
        m.fit(series)
        forecast = m.predict(predict_range)
        forecast.plot(label=model_labels[index], ax=ax)
    return ax

if __name__ == '__main__':
    fig = plt.plot()
    ax = plt.gca()
    plot_predictions("IDK.CN", ax)