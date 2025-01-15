from flask import Flask, jsonify, request
from flask_cors import CORS
import stock_prediction.alpha_vantage.alpha_vantage_client as alpha_vantage_client
from stock_prediction.app_logging.logging_setup import setup_logging
from stock_prediction.utils.request_util import parse_and_validate_stock_symbol

# Application factory function
def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)

    # Set up logging
    setup_logging(app)

    # Define routes
    @app.route('/', methods=['GET'])
    def welcome():
        app.logger.info("Got a call to the welcome function.")
        return jsonify("Welcome")

    @app.route('/predict_stock', methods=['GET'])
    def get_stock_prediction():
        stock_symbol, error = parse_and_validate_stock_symbol()

        if error:
            app.logger.error(f"Validation error: {error}")
            return jsonify({"error": error}), 400
        
        app.logger.info(f"Getting stock data for symbol: {stock_symbol}")
        try:
            stock_data = alpha_vantage_client.get_stock_data(app, stock_symbol)
            print(stock_data)
            return jsonify(stock_data.model_dump())
        except Exception as e:
            app.logger.error(f"error getting the data: {e}")
            return jsonify({"error": "Failed to fetch the stock data"}), 500

    return app


# Main entry point
def main():
    app = create_app()
    app.logger.info("Created the app.")
    app.run(debug=True)


# Script execution
if __name__ == '__main__':
    main()
