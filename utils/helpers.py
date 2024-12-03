def format_candlestick_data(candlestick): # convert candlestick data into readable dictionar unused
    return {
        "timestamp_msec": candlestick.timestamp_msec,
        "open": candlestick.open,
        "high": candlestick.high,
        "low": candlestick.low,
        "close": candlestick.close,
    }

def validate_candlestick(candlestick): #unused method
    assert candlestick['open'] <= candlestick['high'], "Open price is greater than High price"
    assert candlestick['low'] <= candlestick['high'], "Low price is greater than High price"
    assert candlestick['close'] >= candlestick['low'], "Close price is less than Low price"
