import telebot
import re
import requests
import time
import logging
from bs4 import BeautifulSoup

root_logger= logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('test.log', 'w', 'utf-8') 
formatter = logging.Formatter("%(name)s:%(levelname)s:%(message)s") 
handler.setFormatter(formatter)
root_logger.addHandler(handler)
logging.warning('uwaga') 
logging.error('pizdec') 
logging.critical('sovsempizdec')

bot = telebot.TeleBot(token='1459231293:AAHE9PJMgqjWGChR0wSp0cduuXLhy3kiXm8')
while True:
     try:
         r=requests.get('https://finewords.ru/sluchajnaya')
         res=re.sub('(<.+?>)', '', r.text)
         bot.send_message(-1001865685863,res)
         time.sleep(10)
     except Exception as error:
         logging.critical(error) 