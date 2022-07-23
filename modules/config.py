import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "1677067"))
API_HASH = getenv("API_HASH", "0d8c8aabe36b01db6a26a7f2780fa660")
BOT_TOKEN = getenv("BOT_TOKEN", "5595298904:AAFQYLz6H4eia8yWykSjTSUVhFK6VWTfa68")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
