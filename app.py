import streamlit as st
from bot.client import get_binance_client
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
)
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price,
)

st.set_page_config(page_title="Trading Bot UI", layout="centered")

st.title("🚀 Binance Futures Testnet Trading Bot")
st.write("Lightweight UI for placing Futures orders")

# Inputs
symbol = st.text_input("Symbol", value="BTCUSDT").upper()

side = st.selectbox("Side", ["BUY", "SELL"])

order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_LIMIT"])

quantity = st.text_input("Quantity", value="0.01")

price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.text_input("Limit Price")

if order_type == "STOP_LIMIT":
    stop_price = st.text_input("Stop Price")

if st.button("Place Order"):

    try:
        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)
        validate_stop_price(order_type, stop_price)

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

        # Response Handling
        order_id = order.get("orderId") or order.get("algoId")
        status = order.get("status") or order.get("algoStatus")

        st.success("Order Placed Successfully!")

        st.write("### Order Details")
        st.write(f"**Order ID:** {order_id}")
        st.write(f"**Status:** {status}")

        if "executedQty" in order:
            st.write(f"**Executed Quantity:** {order.get('executedQty')}")

        if "avgPrice" in order:
            st.write(f"**Average Price:** {order.get('avgPrice')}")

    except Exception as e:
        st.error(f"Order Failed: {str(e)}")