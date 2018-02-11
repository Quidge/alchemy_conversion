import csv
import urllib.request
import pickle

from flask_sqlalchemy import SQLAlchemy
from time import gmtime, strftime
from flask import redirect, render_template, request, session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

def apology(message, code=400):
	"""Renders message as an apology to users."""

def valid_login(username, plaintext, database):
	"""Returns true if username/password combination is in database."""

def login_required(f):
	"""
	Decorate routes to require login.

	http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
	"""

def lookup(symbol):
    """Look up quote for symbol."""

    # reject symbol if it starts with caret
    if symbol.startswith("^"):
        return None

    # Reject symbol if it contains comma
    if "," in symbol:
        return None

    # Query Yahoo for quote
    # http://stackoverflow.com/a/21351911
    try:

        # GET CSV
        url = f"http://download.finance.yahoo.com/d/quotes.csv?f=snl1&s={symbol}"
        webpage = urllib.request.urlopen(url)

        # Read CSV
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())

        # Parse first row
        row = next(datareader)

        # Ensure stock exists
        try:
            price = float(row[2])
        except:
            return None

        # Return stock's name (as a str), price (as a float), and (uppercased) symbol (as a str)
        return {
            "name": row[1],
            "price": price,
            "symbol": row[0].upper(),
            "source": "Yahoo Finance"
        }

    except:
        pass

    # Query Alpha Vantage for quote instead
    # https://www.alphavantage.co/documentation/
    try:

        # GET CSV
        url = f"https://www.alphavantage.co/query?apikey=NAJXWIA8D6VN6A3K&datatype=csv&function=TIME_SERIES_INTRADAY&interval=1min&symbol={symbol}"
        webpage = urllib.request.urlopen(url)

        # Parse CSV
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())

        # Ignore first row
        next(datareader)

        # Parse second row
        row = next(datareader)

        # Ensure stock exists
        try:
            price = float(row[4])
        except:
            return None

        # Return stock's name (as a str), price (as a float), and (uppercased) symbol (as a str)
        return {
            "name": symbol.upper(),  # for backward compatibility with Yahoo
            "price": price,
            "symbol": symbol.upper(),
            "source": "AlphaVantage"
        }

    except:
        return None


def usd(value):
    """Formats value as USD."""
    return f"${value:,.2f}"

def sell_stock(user_id, symbol, share_price, num_shares):
	"""Creates SELL transaction in transaction table. Credits balance 
	with sale profits."""

def buy_stock(user_id, symbol, share_price, num_shares):
	"""Creates BUY transaction in transaction table. Debits corresponding
        amount from users cash. Assumes ONLY stock symbol and stock price are
        accurate and will return None if other parameters fail validation.

        Returns user's cash balance minus total purchase cost."""

def store_snapshot(user_id, data_table, generation_date):
    """Stores a pickled snapshot of user portfolio to user_portfolio_snapshots.

        If entry already exists in user_portfolio_snapshots for user_id, then
        the old entry is overwritten.

        Returns True if sucessful and False if unsucessful.
        """

def get_snapshot(user_id):
    """Deserializes pickle string snapshot of user portfolio.

    > if snapshot found, returns    {   "data_rows": <data here>,
                                        "fetch_timestamp": <timestamp in GMT seconds>
                                    }
    > else returns                  {   "data_rows": [],
                                        "fetch_timestamp": None
                                    }
    """

def get_updated_portfolio_prices(user_id):
    """Requests current stock prices for all stocks held in portfolio."""

