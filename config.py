import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 21968859

API_HASH = "21a59d21687f01d448530ee88a26b1eb"

BOT_TOKEN = "7841297769:AAHV2MTT_XROcd-UL_WdFmEYYrYWTotWgeM"

BOT_ID = 7841297769

BOT_USERNAME = "@Devil_X_Music_Robot"

OWNER_USERNAME = "@Veron_seller"

BOT_NAME = "˹𝐃ᴇᴠɪʟ ꭙ 𝐌ᴜsɪᴄ˼™"

ASSUSERNAME = "@devilassistsnt"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", "-1002485775078")) 

DISASTER_LOG = -1002485775078

OWNER_ID = 6356050482

SPECIAL_USER = 7774827065

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/VERON_BOTS"

SUPPORT_CHAT = "https://t.me/VERON_SUPPORTS"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQGeps4At9VkBjZajRDWZ5fCK6zt0nxJHi8hAvqfL5yUTJ0UIEepnol_m2w3wYqz9Pnbfg4SGFVZa_mAxQAmw0aXjLwDR0sDDv47fqzkLehd8HT-cpIGGMgNNukH4WN0_VGo8a0TC5t03HMLUcZT7F9NoR6QwHXmooRxy6z-Oyslk_jDL0TajGUcXNBveN_ttXAjezhTJAIYDpqEYRKJygepLG41hJDJYwtzbr3AVJhjIhVIurZtejur7cPnSEa77DmlIKn6j6vNbOMHBWKPJ_pDD58oQEy79-Uv7szsX8eTWppowNH_1ocM7cUsrpSZfiDZWwLi1RYDTPrkBNEAccPWcEp_pgAAAAHB_0VhAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
STATS_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
STREAM_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/G4TN8Tmk/photo-2025-08-02-08-15-45-7533898998311026696.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
