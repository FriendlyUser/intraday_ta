import yfinance as yf
import matplotlib
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

import matplotlib.pyplot as plt


def get_prices(stock, start_date="2019-03-03", end_date="2020-12-14"):
    data = yf.download(stock, start=start_date, end=end_date,
                      group_by="ticker")
    data = data.fillna(method='ffill')
    # Drop columns with no entries
    data = data.dropna(axis='columns', how='all')

    # prices_df = pd.concat([data[ticker]["Close"] for ticker in stocks], axis=1)
    # prices_df.columns = stocks
    return data


def plot_predictions(ticker: str, ax: matplotlib.axes.Axes, models: list = None):
    """
        ticker - yahoo finance ticker
        ax - matplotlib ax to be passed to darts.plot -> pandas.plot
        models - List of models to pass in
    """
    # Get a more complicated method
    if models == None:
        models = [NaiveSeasonal(6), NaiveSeasonal(12), NaiveDrift()]
    model_labels = ['Naive Seasonal (6)', 'Naive Seasonal (12)', 'Drift']
    asset_prices = get_prices(ticker)
    asset_prices['Date'] = asset_prices.index
    series = TimeSeries.from_dataframe(asset_prices, 'Date', ['Close'],  'B')
    series.plot(label='actual', ax=ax)
    # run through models and predict results
    for index, m in enumerate(models):
        m.fit(series)
        forecast = m.predict(50)
        forecast.plot(label=model_labels[index], ax=ax)
    plt.legend()
    return ax

if __name__ == '__main__':
    fig = plt.plot()
    ax = plt.gca()
    plot_predictions("IDK.CN", ax)