import stock_prediction.alpha_vantage.alpha_vantage_client as alpha_vantage_client
import pytest
from unittest.mock import Mock


def test_get_ibm_stock_data_from_disk():
    app = Mock()
    stock_symbol = "IBM"
    stock_data = alpha_vantage_client.get_stock_data(app, stock_symbol)
    print(stock_data)
    assert stock_symbol in str(stock_data)


def test_getting_wrong_data_from_disk():
    app = Mock()
    stock_symbol = "Corrupt"
    with pytest.raises(Exception, match="validation") as exception:
        alpha_vantage_client.get_stock_data(app, stock_symbol)

    print(exception.value)


def test_get_stock_data_from_alpha_vantage():
    """
    This will call the Alpha Vantage API.
    We are rate limited to 20 a day so keep that in mind
    when running this.
    """
    app = Mock()
    stock_symbol = "AMZN"
    stock_data = alpha_vantage_client.get_stock_data(app, stock_symbol)
    print(stock_data)


def test_get_error_from_alpha_vantage():
    """
    This will call the Alpha Vantage API.
    We are rate limited to 20 a day so keep that in mind
    when running this.
    """
    app = Mock()
    stock_symbol = "NOT_EXISTENT_SYMBOL"
    with pytest.raises(Exception, match="validation") as exception:
        alpha_vantage_client.get_stock_data(app, stock_symbol)
    print(exception.value)
