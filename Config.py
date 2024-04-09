import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27960337"))
    API_HASH = os.environ.get("API_HASH", "22f8e42e48422f83c9aabebba937d0f4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6849991060:AAE4aqmMueKNJFmDwTCoPydX6MJKwkuH6NE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu3ISA8Jl_NKBiMg2UIOOlIOu8Gdbl0oLSv1Em6DOANMnzgvTLQCbE37qg2VH68KEVbAoiHsVn8XBi7C5rBgLDjEozPNmKie5zVprhn8-YeyquPDvS3TUF72mljAtBy8DY91hRvP8pn4nd-jjBTJGIb3hpYbzH2enPvcaZ77LBaxCIODuaq2fD7sZQzY7BmTyNxTiOkK95tROJzcIxPqWFdt0l5CNj5YlPNdL36sbvyLvXD6aBfehxpJ1AFHLPMcPS2dvxy15bD7bQqMkGT0nANmcGuqgPNdE7zfXtrSQqttsPbLvS6CQwameD4IlZG8jWl7P3qppXWDHGAsNapIHpKM=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MA2ZIKABOT")
    SUPPORT = os.environ.get("SUPPORT", "@Cptagon")
    CHANNEL = os.environ.get("CHANNEL", "@Cptagon")
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://graph.org/file/673bd8e51c4fef00c2848.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "6726508431")

