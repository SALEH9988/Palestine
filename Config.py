import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27960337"))
    API_HASH = os.environ.get("API_HASH", "22f8e42e48422f83c9aabebba937d0f4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6849991060:AAE4aqmMueKNJFmDwTCoPydX6MJKwkuH6NE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAGqpBEAddPQuuWNwPY4g8ZYK2asC2azx-KM-3ZkoE3aM1r3nJSIYsidf-pCVH4edFJj0MqZH5YAUZJK4ccqXGxkAz84_VbkvGUM2-cXF3LMbttXeSQ18tTCVkBKpLChepZQPGjkNylsNBaR5L5PuVemqZOi51dKBo71KNMk03m_-jzRcUVKXrxk1TOFfrX2ewVQfv7XZ4Aa8FxH0qswHKyU9wqBX1seR9zV0z-WOUZBxOiHKjIyUZQ4OTwuKuh1_dGOy2MsPiXxzvR-lKmqDIkFbHrHx_uym4l4SRpd0ULsQGi-NoUEavApKLIy5lfoAX5owa4NVZlY5zmJjE5How7uz4yd9QAAAAGbSZs3AA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MA2ZIKABOT")
    SUPPORT = os.environ.get("SUPPORT", "@Cptagon")
    CHANNEL = os.environ.get("CHANNEL", "@Cptagon")
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "6726508431")

