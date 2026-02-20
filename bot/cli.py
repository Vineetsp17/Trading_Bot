import argparse
import sys
from .client import get_binance_client
from .orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
)
from .validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price,
)
from .logging_config import setup_logger

logger = setup_logger()


def interactive_input():
    print("\n🔹 Interactive Trading Mode 🔹\n")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()
    order_type = input("Enter order type (MARKET/LIMIT/STOP_LIMIT): ").strip().upper()
    quantity = input("Enter quantity: ").strip()

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = input("Enter limit price: ").strip()

    if order_type == "STOP_LIMIT":
        stop_price = input("Enter stop price: ").strip()

    return symbol, side, order_type, quantity, price, stop_price


def confirm_order():
    confirm = input("\n⚠️ Confirm order? (yes/no): ").strip().lower()
    return confirm == "yes"


def main():
    parser = argparse.ArgumentParser(
        description="🚀 Binance Futures Testnet Trading Bot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", help="BUY or SELL")
    parser.add_argument("--type", help="MARKET, LIMIT, or STOP_LIMIT")
    parser.add_argument("--quantity", help="Order quantity")
    parser.add_argument("--price", help="Limit price (required for LIMIT & STOP_LIMIT)")
    parser.add_argument("--stop_price", help="Stop price (required for STOP_LIMIT)")

    args = parser.parse_args()

    if not any(vars(args).values()):
        symbol, side, order_type, quantity, price, stop_price = interactive_input()
    else:
        symbol = (args.symbol or "").upper()
        side = (args.side or "").upper()
        order_type = (args.type or "").upper()
        quantity = args.quantity
        price = args.price
        stop_price = args.stop_price

    try:
        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)
        validate_stop_price(order_type, stop_price)

        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Type        : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type in ["LIMIT", "STOP_LIMIT"]:
            print(f"Limit Price : {price}")

        if order_type == "STOP_LIMIT":
            print(f"Stop Price  : {stop_price}")

        print("===================================")

        if not confirm_order():
            print("\n❌ Order cancelled by user.")
            sys.exit(0)

        client = get_binance_client()

        # Order Placement
        if order_type == "MARKET":
            order = place_market_order(client, symbol, side, quantity)

        elif order_type == "LIMIT":
            order = place_limit_order(client, symbol, side, quantity, price)

        elif order_type == "STOP_LIMIT":
            order = place_stop_limit_order(
                client, symbol, side, quantity, price, stop_price
            )

        # Unified Response Handling
        print("\n========== ORDER RESPONSE ==========")

        order_id = order.get("orderId") or order.get("algoId")
        status = order.get("status") or order.get("algoStatus")

        print(f"Order ID        : {order_id}")
        print(f"Status          : {status}")

        if "executedQty" in order:
            print(f"Executed Qty    : {order.get('executedQty')}")

        if "avgPrice" in order:
            print(f"Average Price   : {order.get('avgPrice')}")

        print("====================================")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Order failed: {str(e)}")
        logger.error(str(e))


if __name__ == "__main__":
    main()