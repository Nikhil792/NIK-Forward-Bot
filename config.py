

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "10671416"))
    API_HASH = environ.get("API_HASH", "d32e7a9253928d78d7888c0b9998939d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://technik659:8pZAv0q1E4TpzBfW@cluster0.scjdsho.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER = int(environ.get("BOT_OWNER", "6667067260"))
  



class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []


