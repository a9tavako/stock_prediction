import json
import stock_prediction.alpha_vantage.alpha_vantage_client as alpha_vantage_client

from stock_prediction.alpha_vantage.alpha_vantage_data_model import StockData
from stock_prediction.time_series.time_series_model import TimeDataPoint, TimeSeries
from datetime import date


json_text = """{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2024-08-13",
        "4. Output Size": "Full size",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2024-08-13": {
            "1. open": "190.2900",
            "2. high": "191.3100",
            "3. low": "189.2100",
            "4. close": "190.9900",
            "5. volume": "2178862"
        },
        "2024-08-12": {
            "1. open": "191.2500",
            "2. high": "191.5761",
            "3. low": "189.0001",
            "4. close": "189.4800",
            "5. volume": "2290421"
        },
        "2024-08-09": {
            "1. open": "191.1800",
            "2. high": "192.6300",
            "3. low": "189.0400",
            "4. close": "191.4500",
            "5. volume": "2773706"
        }
    }
}
"""


expected_series = TimeSeries([
    TimeDataPoint(date(2024, 8, 9), 191.4500),
    TimeDataPoint(date(2024, 8, 12), 189.4800),
    TimeDataPoint(date(2024, 8, 13), 190.9900)
])


def test_convert_alpha_vantage_to_time_series():
    json_data = json.loads(json_text)
    stock_data = StockData(**json_data)
    time_series = alpha_vantage_client.alpha_vantage_to_time_series(stock_data)

    assert time_series == expected_series

