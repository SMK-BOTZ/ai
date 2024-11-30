
# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "28243586"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7641984496:AAHgZopQQiDTOje1fjQJAJdM0aZABgLyJiU")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME", "EQUROBOT")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6551906246"))

EVAL = list(map(int, getenv("EVAL", "6551906246").split()))
# ------------------X------------------------------
DEEP_API = os.environ.get("DEEP_API", "96a36c8b-0a06-461a-bce3-851d5d997a60")
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID", "-1002196541223"))
# ------------------------------------------------
GPT_API = os.environ.get("GPT_API", "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")
# ------------------------------------------------
DAXX_API = os.environ.get("DAXX_API", "5163c49d-b696-47f1-8cf9-")
# ------------------------------------------------
MONGO_DB = os.environ.get("CLONEDB", "mongodb+srv://madarazbotz:IMpkK5ZoxUNI89Xu@cluster0.vufqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
