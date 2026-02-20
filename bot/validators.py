def validate_symbol(symbol):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")


def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")


def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT.")


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Quantity must be a positive number.")


def validate_price(order_type, price):
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        if price is None:
            raise ValueError("Price is required for LIMIT and STOP_LIMIT orders.")
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
        except ValueError:
            raise ValueError("Price must be a positive number.")


def validate_stop_price(order_type, stop_price):
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValueError("Stop price is required for STOP_LIMIT orders.")
        try:
            stop_price = float(stop_price)
            if stop_price <= 0:
                raise ValueError
        except ValueError:
            raise ValueError("Stop price must be a positive number.")