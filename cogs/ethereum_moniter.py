import discord
from discord.ext import commands, tasks
import datetime
import pytz
import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def timeStamp():
  tz = pytz.timezone('US/Eastern')
  time = datetime.datetime.now(tz)
  dateFormatted = time.strftime("%A %d %B %Y")
  timeFormatted = time.strftime("%I:%M %p + %Ss")
  return time, dateFormatted, timeFormatted

def getPrices():
  url = "https://coinmarketcap.com/currencies/ethereum/"
  r = requests.get(url, headers = headers)
  soup = BeautifulSoup(r.text, 'lxml')
  price = soup.find('div', class_ = 'priceValue').findAll('span')[0].text
  
  date, dateFormat, timeFormat = timeStamp()
  return price, date, dateFormat, timeFormat
  
class ethereum_moniter(commands.Cog): 
    def __init__(self, client):
        self.client = client
        self.liveMoniter.start()

    def cog_unload(self):
        self.liveMoniter.cancel()

    # @commands.command()
    @tasks.loop(seconds=300)
    async def liveMoniter(self):
      stop = False
      while stop != True:
        try:
          
          ethMoniter = self.client.get_channel(1002742610160517130)
          price, date, dateFormat, timeFormat = getPrices()
          await ethMoniter.send(f'__**ETH**__: **{price}** as of {dateFormat}, {timeFormat} (US/Eastern time)')
          await ethMoniter.send(f'NOTE: Graphing will be added later, as soon as I make sure this doesn\'t use up too much recources.')
          await ethMoniter.send(f"""```fix\nTimestamp: {date}```""")
          stop = True
          
        except Exception as e:
          await ethMoniter.send(f'ERROR: {e}')
          print(e)
          stop = True
    
    @liveMoniter.before_loop
    async def beforeMoniter(self):
        print('Waiting for bot...')
        await self.client.wait_until_ready()


def setup(client): 
    client.add_cog(ethereum_moniter(client))