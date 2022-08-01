import discord
from discord.ext import commands
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

    @commands.command(help = ' - start live ethereum moniter')
    async def liveMoniter(self, ctx, password):
      stop = False
      if password == '32233223p':
        while stop != True:
          try:
            price, date, dateFormat, timeFormat = getPrices()
            await ctx.send(f'__**ETH**__: **{price}** as of {dateFormat}, {timeFormat} (US/Eastern time)')
            await ctx.send(f'NOTE: Graphing will be added later, as soon as I make sure this doesn\'t use up too much recources.')
            await ctx.send(f"""```fix\nTimestamp: {date}```""")

            time.sleep(3600)
            
          except Exception as e:
            await ctx.send(f'ERROR: {e}')
            print(e)
            stop = True
        
      else:
        await ctx.send('wrong password')

def setup(client): 
    client.add_cog(ethereum_moniter(client))