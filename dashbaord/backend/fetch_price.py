
from SmartApi import SmartConnect
from supabase import create_client
from dotenv import load_dotenv
import pyotp
import os

load_dotenv()

API_KEY = os.getenv("SMART_API_KEY")
CLIENT_ID = os.getenv("SMART_CLIENT_ID")
PASSWORD = os.getenv("SMART_PASSWORD")
TOTP_SECRET = os.getenv("SMART_TOTP_SECRET")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

RELIANCE_TOKEN = os.getenv("RELIANCE_TOKEN")

# Angel One Login
smart = SmartConnect(api_key=API_KEY)

session = smart.generateSession(
    CLIENT_ID,
    PASSWORD,
    pyotp.TOTP(TOTP_SECRET).now()
)

# Fetch Reliance LTP
ltp = smart.ltpData(
    exchange="NSE",
    tradingsymbol="RELIANCE-EQ",
    symboltoken=RELIANCE_TOKEN
)

price = ltp["data"]["ltp"]

print("Reliance Price:", price)

# Supabase Connection
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

supabase.table("stock_prices").insert({
    "symbol": "RELIANCE",
    "price": price
}).execute()

print("Saved to Supabase")
