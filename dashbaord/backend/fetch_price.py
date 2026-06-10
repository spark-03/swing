import os
import pyotp

from SmartApi import SmartConnect
from supabase import create_client

API_KEY = os.environ["SMART_API_KEY"]
CLIENT_ID = os.environ["SMART_CLIENT_ID"]
PASSWORD = os.environ["SMART_PASSWORD"]
TOTP_SECRET = os.environ["SMART_TOTP_SECRET"]

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

RELIANCE_TOKEN = os.environ["RELIANCE_TOKEN"]

# Angel One Login
smart = SmartConnect(api_key=API_KEY)

session = smart.generateSession(
    CLIENT_ID,
    PASSWORD,
    pyotp.TOTP(TOTP_SECRET).now()
)

# Fetch LTP
ltp_data = smart.ltpData(
    "NSE",
    "RELIANCE-EQ",
    RELIANCE_TOKEN
)

price = ltp_data["data"]["ltp"]

print(f"Reliance Price: {price}")

# Save to Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

response = supabase.table("stock_prices").insert(
    {
        "symbol": "RELIANCE",
        "price": price
    }
).execute()

print("Saved to Supabase")
