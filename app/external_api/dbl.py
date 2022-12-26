import os

from dotenv import load_dotenv
from .base import api

load_dotenv()

HOST = lambda: 'https://top.gg/api/'
HEADERS = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Authorization': os.getenv("DBL_TOKEN")
}

dbl_api = api(HOST, HEADERS)


def get_bot_server_count(bot_id: int):
    return dbl_api('get', f'bots/{bot_id}/stats')


def post_bot_server_count(bot_id: int, server_cnt: int):
    payload = {
        "server_count": server_cnt
    }
    return dbl_api('post', f'bots/{bot_id}/stats', payload)
