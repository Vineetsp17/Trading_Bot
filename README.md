# 🚀 Binance Futures Testnet Trading Bot

A modular Python-based trading bot built for **Binance Futures Testnet
(USDT-M)** as part of the Python Developer Application Task.

This application allows users to place Market, Limit, and Stop-Limit
orders using a clean, reusable architecture with proper logging,
validation, and error handling.

------------------------------------------------------------------------

## Description

This project implements a simplified trading bot that interacts with the
Binance Futures Testnet API.

The application:

-   Connects securely using API credentials
-   Places Market and Limit orders (core requirement)
-   Supports BUY and SELL sides
-   Validates CLI input
-   Logs all API interactions
-   Handles exceptions gracefully
-   Extends functionality with Stop-Limit orders
-   Provides both CLI and Web UI interfaces

The system follows clean separation of concerns:

-   API Client Layer
-   Order Execution Layer
-   Validation Layer
-   Logging Layer
-   Interface Layer (CLI + UI)

------------------------------------------------------------------------

## Features

### Core Requirements

-   Market Orders (USDT-M Futures)
-   Limit Orders (USDT-M Futures)
-   BUY and SELL support
-   CLI input via argparse
-   Input validation
-   Clear output summary
-   Order response display (orderId, status, executedQty, avgPrice)
-   Structured modular code
-   Logging to file
-   Exception handling

### Bonus Implemented

-   Stop-Limit Order Support
-   Enhanced CLI UX (interactive mode + confirmation)
-   Lightweight Web UI (Streamlit)

------------------------------------------------------------------------

## Tech Stack

  Tool / Library       Version            Purpose
  -------------------- ------------------ ---------------------------------
  Python               3.10+              Core language
  python-binance       Latest             Binance API integration
  python-dotenv        Latest             Environment variable management
  Streamlit            Latest             Lightweight Web UI
  logging (built-in)   Standard Library   Logging framework
  argparse             Standard Library   CLI parsing

------------------------------------------------------------------------

## Setup

### Getting Started

### Prerequisites

1.  Python 3.x installed
2.  pip installed
3.  Git installed
4.  Binance Futures Testnet account
5.  API Key and Secret

------------------------------------------------------------------------

### Installation

``` bash
git clone <your-repository-url>
cd trading_bot

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

------------------------------------------------------------------------

### Environment Configuration

Create a `.env` file:

``` env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

Testnet Base URL: https://demo.binance.com/en/futures/BTCUSDT

------------------------------------------------------------------------

## Basic Usage

### Market Order

``` bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

``` bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 10000
```

### Stop-Limit Order

``` bash
python -m bot.cli --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.01 --price 65000 --stop_price 65000
```

### Interactive CLI Mode

``` bash
python -m bot.cli
```

------------------------------------------------------------------------

## Web UI (Streamlit)

``` bash
python -m streamlit run app.py
```

Open in browser: http://localhost:8501

------------------------------------------------------------------------

## Project Structure

    trading_bot/
    │
    ├── bot/
    │   ├── __init__.py
    │   ├── client.py
    │   ├── orders.py
    │   ├── validators.py
    │   ├── logging_config.py
    │   ├── cli.py
    │
    ├── logs/
    │   └── trading_bot.log
    │
    ├── app.py
    ├── requirements.txt
    ├── .env
    ├── README.md

------------------------------------------------------------------------

## Logging

All API interactions are logged in:

logs/trading_bot.log

Includes: - Timestamp - Order type - Symbol - Quantity - API response -
Error details

------------------------------------------------------------------------

## Contributing

1.  Fork the repository
2.  Create a feature branch
3.  Commit your changes
4.  Push to your branch
5.  Open a Pull Request

------------------------------------------------------------------------

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files...

------------------------------------------------------------------------

## Conclusion

This project demonstrates:

-   Clean backend architecture
-   Secure Binance Futures Testnet integration
-   CLI + Web UI interfaces
-   Structured logging and validation
-   Advanced Stop-Limit handling

Built as part of the Python Developer Application Task.
