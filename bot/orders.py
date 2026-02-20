from binance.exceptions import BinanceAPIException
from .logging_config import setup_logger

logger = setup_logger()


def place_market_order(client, symbol, side, quantity):
    try:
        logger.info(f"Placing MARKET order | {symbol} | {side} | {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        print("RAW RESPONSE:", order)

        logger.info(f"MARKET Order Response: {order}")
        return order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    try:
        logger.info(f"Placing LIMIT order | {symbol} | {side} | {quantity} | {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        print("RAW RESPONSE:", order)

        logger.info(f"LIMIT Order Response: {order}")
        return order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise


def place_stop_limit_order(client, symbol, side, quantity, price, stop_price):
    try:
        logger.info(
            f"Placing STOP_LIMIT order | {symbol} | {side} | {quantity} | price={price} | stop={stop_price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce="GTC",
        )

        print("RAW RESPONSE:", order)

        logger.info(f"STOP_LIMIT Order Response: {order}")
        return order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise