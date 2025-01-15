from flask import request


def parse_and_validate_stock_symbol():
    '''
    Extracts the symbol arguments from the request url.
    '''
    stock_symbol = request.args.get('symbol', default=None, type=str)

    if not stock_symbol:
        return None, "Stock symbol is required."
    
    if not stock_symbol.isalpha():
        return None, "Stock symbol must be alpha_numerical."
    
    return stock_symbol, None