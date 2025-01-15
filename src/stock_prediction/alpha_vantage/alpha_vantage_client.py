from stock_prediction.alpha_vantage.alpha_vantage_data_model import StockData
from stock_prediction.utils.path import path_relative_to_root
import json
import os
import requests
from stock_prediction.time_series.time_series_model import TimeSeries
import urllib.parse

CLOSE = "4. close"
CORRUPT_DATA_FILE_PATH = path_relative_to_root("src/stock_prediction/data/wrong_alpha_vantage_data.json")
IBM_FILE_PATH = path_relative_to_root("src/stock_prediction/data/ibm_alpha_vantage_data.json")
HIGH = "2. high"
LOW = "3. low"
SUCCESS_CODE = 200
TIME_SERIES_DAILY = "Time Series (Daily)"
TIME_SERIES_DAILY_STR = "TIME_SERIES_DAILY"
TIME_FORMAT = "%Y-%m-%d"

STR_ALPHA_ADV = "AlphaVantageAPIKey"
STR_ALPHA_ADV_BASE_URL = "https://www.alphavantage.co/query?"


def get_stock_data(
        app,
        stock_symbol: str
) -> StockData:
    json_data = None

    if stock_symbol == "IBM":
        json_data = get_test_data(IBM_FILE_PATH)
    elif stock_symbol == "Corrupt":
        json_data = get_test_data(CORRUPT_DATA_FILE_PATH)
    else:
        json_data = contact_alpha_vantage(app, stock_symbol)

    try:
        return StockData(**json_data)
    except Exception as e:
        app.logger.info(f"Error in processing stock data. json_data: {json_data}")
        app.logger.info(e)
        raise


def get_test_data(file_path: str) -> json:
    with open(file_path, "r") as file_handle:
        json_data = json.load(file_handle)

    return json_data


def contact_alpha_vantage(
        app,
        stock_symbol: str
) -> json:
    stock_api_key = os.getenv(STR_ALPHA_ADV)
    alpha_adv_args = {
        "function": TIME_SERIES_DAILY_STR,
        "outputsize": "full",
        "symbol": stock_symbol,
        "apikey": stock_api_key,
    }

    url = STR_ALPHA_ADV_BASE_URL + urllib.parse.urlencode(alpha_adv_args)
    app.logger.info("Contacting Alpha Vantage: " + url)
    alpha_adv_response = requests.get(url)

    if alpha_adv_response.status_code != SUCCESS_CODE:
        app.logger.info("Error in getting the data from Alpha Vantage:")
        app.logger.info(
            "Response Status Code: " +
            str(alpha_adv_response.status_code)
        )
        raise RuntimeError()

    return alpha_adv_response.json()


def alpha_vantage_to_time_series(stock_data: StockData) -> TimeSeries:
    time_series = TimeSeries([])

    for date in sorted(stock_data.time_series.keys()):
        daily_prices = stock_data.time_series[date]
        time_series.add_data_point(date, daily_prices.close)

    return time_series
