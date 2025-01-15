from stock_prediction.app_dotenv import load

def test_alpha_vantage_key_exists():
    alpha_vantage_key_str = "AlphaVantageAPIKey"
    env_values = load.get_dotenv()
    assert alpha_vantage_key_str in env_values
